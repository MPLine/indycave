import csv

from django.core.management.base import BaseCommand
from publishers.models import Publisher


class Command(BaseCommand):

    help = "Import publishers from a CSV file"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        csv_file = options["csv_file"]

        created_count = 0
        updated_count = 0

        with open(
            csv_file,
            "r",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                name = row["name"].strip()

                if not name:
                    continue

                publisher, created = Publisher.objects.update_or_create(
                    name=name,
                    defaults={
                        "game_types_focus": row.get(
                            "game_types_focus",
                            ""
                        ).strip(),

                        "platforms": row.get(
                            "platforms",
                            ""
                        ).strip(),

                        "pitch_url": row.get(
                            "pitch_url",
                            ""
                        ).strip(),

                        "pitch_email": row.get(
                            "pitch_email",
                            ""
                        ).strip(),

                        "pitch_requirements": row.get(
                            "pitch_requirements",
                            ""
                        ).strip(),

                        "official_website": row.get(
                            "official_website",
                            ""
                        ).strip(),
                    }
                )

                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import complete: "
                f"{created_count} created, "
                f"{updated_count} updated."
            )
        )