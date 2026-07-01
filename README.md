# Masterblog

A simple, lightweight blogging web application built with [Flask](https://flask.palletsprojects.com/).
Masterblog lets you create, read, update, and delete blog posts through a clean web interface — a classic **CRUD** application.

## Description

Masterblog is a beginner-friendly full-stack project that demonstrates how to build a
dynamic website with Python and Flask. Posts are stored in a local JSON file, so there is
no need to set up a database to get started.

**What problem does it solve?**
It provides a minimal, easy-to-understand foundation for a personal blog or for learning
how web applications handle data and user input.

**Who is it for?**
Anyone learning web development with Flask, or anyone who wants a small, no-frills blog
they can run and customize themselves.

## Features

- 📋 View all blog posts on the home page
- ✍️ Create new posts (author, title, content)
- 📝 Update existing posts
- 🗑️ Delete posts
- 💾 Data persisted in a simple JSON file

## Tech Stack

- **Python 3**
- **Flask** — web framework
- **Jinja2** — HTML templating (bundled with Flask)
- **HTML / CSS** — frontend
- **JSON** — data storage

## Project Structure

```
Masterblog/
├── app.py                        # Flask app and routes
├── posts.json                    # Stored blog posts
├── storage/
│   └── posts_repository.py       # Read/write logic for posts
├── templates/                    # Jinja2 HTML templates
│   ├── index.html                # List of all posts
│   ├── add.html                  # Form to create a post
│   └── update.html               # Form to edit a post
├── static/
│   └── style.css                 # Stylesheet
├── requirements.txt              # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3 installed on your machine
- `pip` for installing dependencies

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lindaEbbert/Masterblog.git
   cd Masterblog
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the development server:

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

From there you can:

- **View** all posts on the home page.
- **Create** a post by clicking *New post* and filling in the author, title, and content.
- **Edit** a post by clicking *Edit* next to it.
- **Delete** a post by clicking *Delete* next to it.

> **Note:** The app runs in debug mode on port `5000` by default. You can change the host
> and port in `app.py` at the bottom of the file.

## Contributing

Contributions are welcome! If you'd like to improve Masterblog:

1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/my-improvement
   ```
3. Commit your changes with a clear message.
4. Push the branch and open a pull request describing what you changed and why.

For larger changes, please open an issue first to discuss what you would like to change.

## License

This project was created for educational purposes.
