
import requests
import xml.etree.ElementTree as ET
from .scoring_service import calculate_potential_score

GITHUB_API_URL = "https://api.github.com/search/repositories"

RSS_SOURCES = {
    "itch.io": "https://itch.io/feed/new.xml",
    "IndieDB": "https://www.indiedb.com/rss",
}


def search_github_games(limit=10):
    results = []
    seen_urls = set()

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "IndieDevScout",
    }

    queries = [
        "indie game",
        "indie game developer",
        "game development",
    ]

    for query in queries:
        if len(results) >= limit:
            break

        try:
            response = requests.get(
                GITHUB_API_URL,
                params={
                    "q": query,
                    "sort": "updated",
                    "order": "desc",
                    "per_page": min(limit, 100),
                },
                headers=headers,
                timeout=15,
            )
            response.raise_for_status()

            repositories = response.json().get("items", [])

        except requests.RequestException:
            continue

        for repo in repositories:
            url = repo.get("html_url")

            if not url or url in seen_urls:
                continue

            seen_urls.add(url)

            results.append({
                "developer_name": (
                    repo.get("owner", {}).get("login", "")
                ),
                "game_name": repo.get("name", ""),
                "platforms": [],
                "website": repo.get("homepage") or "",
                "contact_email": "",
                "source_name": "GitHub",
                "source_url": url,
            })

            if len(results) >= limit:
                break

    return results


def search_rss_source(source_name, feed_url, limit=10):
    results = []

    try:
        response = requests.get(
            feed_url,
            headers={"User-Agent": "IndieDevScout/1.0"},
            timeout=15,
        )
        response.raise_for_status()

        root = ET.fromstring(response.content)

    except (requests.RequestException, ET.ParseError):
        return results

    # RSS 2.0
    items = root.findall(".//item")

    # Atom feeds use a namespace.
    if not items:
        items = root.findall(
            ".//{http://www.w3.org/2005/Atom}entry"
        )

    for item in items[:limit]:
        def get_text(*paths):
            for path in paths:
                element = item.find(path)
                if element is not None and element.text:
                    return element.text.strip()
            return ""

        title = get_text(
            "title",
            "{http://www.w3.org/2005/Atom}title",
        )

        link = get_text(
            "link",
            "{http://www.w3.org/2005/Atom}id",
        )

        # Atom links may store the URL in an href attribute.
        if not link:
            atom_link = item.find(
                "{http://www.w3.org/2005/Atom}link"
            )
            if atom_link is not None:
                link = atom_link.attrib.get("href", "")

        if not title or not link:
            continue

        results.append({
            "developer_name": "",
            "game_name": title,
            "platforms": [],
            "website": "",
            "contact_email": "",
            "source_name": source_name,
            "source_url": link,
        })

    return results


def search_all_sources(limit=50):
    """
    Search GitHub and public RSS feeds.
    Results are leads for manual admin review, not verified developers.
    """
    all_results = []
    seen_urls = set()

    # Divide the limit between sources so one source
    # cannot consume the entire result list.
    source_limit = max(1, limit // (1 + len(RSS_SOURCES)))

    sources = [
        search_github_games(limit=source_limit)
    ]

    for source_name, feed_url in RSS_SOURCES.items():
        sources.append(
            search_rss_source(
                source_name,
                feed_url,
                limit=source_limit,
            )
        )

    
    for source_results in sources:
        for item in source_results:
            url = item["source_url"]

            if url in seen_urls:
                continue

            seen_urls.add(url)

            item["potential_score"] = calculate_potential_score(item)

            all_results.append(item)

            if len(all_results) >= limit:
                return sorted(
                    all_results,
                    key=lambda result: result["potential_score"],
                    reverse=True,
                )

    return sorted(
        all_results,
        key=lambda result: result["potential_score"],
        reverse=True,
    )

   
