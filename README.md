# IndyCave

### Your next opportunity is closer than you think.

IndyCave is a platform designed to help independent game developers discover potential publishers, improve their game pitches, and find better opportunities to bring their projects to market.

Our goal is to make the publishing journey easier for indie developers by providing relevant publisher recommendations and practical tools in one place.

> **Project status:** MVP in development.

## 🎯 Our Mission

Independent game developers often struggle to find the right publisher, prepare a professional pitch, and identify publishing opportunities that fit their projects.

IndyCave aims to simplify this process by helping developers discover relevant publishers and prepare their projects for professional outreach.

## ✨ Key Features

### 🔎 Scout — Publisher Discovery
- Match indie games with potentially suitable publishers.
- Filter publishers by game genre, supported platforms, and publishing preferences.
- Rank results according to a matching score.
- Display a focused list of the best matches instead of overwhelming developers with hundreds of results.

### ✍️ Pitch Assistant
- Help developers organize their game information.
- Improve game descriptions and pitch content.
- Guide developers toward clearer, more professional presentations of their projects.

### 📚 Publisher Database
- Maintain a structured database of game publishers.
- Store publisher websites, supported platforms, game genres, and public pitching or contact information.
- Provide the data needed for relevant publisher recommendations.

### 🤖 AI-Assisted Tools
IndyCave is designed to support future AI-powered features that can help developers research opportunities and improve their publishing materials.

AI integration will be introduced progressively as the platform evolves.

## 🛠️ Technology Stack

- **Backend:** Python and Django
- **Database:** SQLite for the MVP
- **Frontend:** HTML, CSS, JavaScript, and Bootstrap
- **Authentication:** Django authentication system
- **Future database migration:** PostgreSQL, when needed

## 🏗️ Architecture

IndyCave is built with Django using a modular application structure. Each application handles a specific part of the platform.

The current project includes modules for:

- Publisher management
- Scout and publisher matching
- Chatbot functionality
- Pitch Assistant
- Developer discovery and management

The architecture is intended to evolve as new features are developed and tested.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git

### Installation

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
cd IndyCave
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

**3. Install dependencies**

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

**4. Apply database migrations**

```bash
python manage.py migrate
```

**5. Start the development server**

```bash
python manage.py runserver
```

Open the local development address displayed by Django in your browser.

> Follow the repository's current configuration if additional environment variables or setup steps are required.

## 🗺️ Roadmap

- [x] Establish the Django project structure
- [x] Create the initial publisher database
- [x] Develop publisher matching and scoring
- [x] Build the initial chatbot and Pitch Assistant
- [ ] Improve publisher matching accuracy
- [ ] Expand and verify the publisher database
- [ ] Improve the developer onboarding experience
- [ ] Introduce AI-assisted research progressively
- [ ] Improve testing, security, and deployment readiness
- [ ] Evaluate PostgreSQL migration as the project grows

## 🤝 Contributing

IndyCave is an evolving project. Suggestions, feedback, bug reports, and contributions are welcome.

Before proposing major changes, please describe the problem you want to solve and the improvement you would like to make.

## 📌 Project Status

IndyCave is currently under active development. Features, architecture, and workflows may change as the MVP is tested and improved.

## 📄 License

A license has not yet been specified. All rights and permissions remain with the respective copyright holders until a license is added.

---

**IndyCave — Helping indie developers find their next opportunity.**


  <center><p style=" color: #055411;"><a href="https://www.paypal.com/donate?token=b6E5gjWGkvWiRgNNu1j35WYAOT6-9aGtuw4-s9dKSBlukApVuBnYca1lcVR-XfRxcvZg9oY-GM5YYkkb" target="_blanc">
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" /><br>  Keep the Project Alive, Make a Donation
    </a></p></center>


