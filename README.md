# Pywebscraper

## Description
Pywebscraper is a Python-based web scraping project designed to extract and store structured data from websites into a PostgreSQL database. It is built with scalability, maintainability, and testing in mind, making it suitable for both small experiments and production-level scraping tasks.

## Purpose
The main goals of this project are:
- To demonstrate how to build a clean and modular Python web scraping pipeline.
- To show how to integrate Python scraping code with a PostgreSQL database.
- To provide a ready-to-use project structure that supports testing and containerization.

## Technologies Used
- **Python 3.11+**
- **PostgreSQL** (local or Docker)
- **SQLAlchemy** (ORM)
- **Requests** (HTTP client)
- **BeautifulSoup4** (HTML parsing)
- **pytest** (testing framework)
- **Docker** & **Docker Compose** (optional containerization)

## Installation Guide
1. **Clone the repository**
   ```bash
   git clone https://github.com/abramdarmaputra/Pywebscraper.git
   cd Pywebscraper
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate     # Linux / Mac
   .venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL**

   * Local:

     ```sql
     CREATE ROLE scraper_user WITH LOGIN PASSWORD 'scrape_password';
     CREATE DATABASE scraper_db OWNER scraper_user;
     GRANT ALL PRIVILEGES ON DATABASE scraper_db TO scraper_user;
     ```
   * Docker:

     ```bash
     docker run -d --name pg \
       -e POSTGRES_USER=scraper_user \
       -e POSTGRES_PASSWORD=scrape_password \
       -e POSTGRES_DB=scraper_db \
       -p 5432:5432 postgres:16
     ```

5. **Configure environment variables**
   Create a `.env` file:

   ```
   DATABASE_URL=postgresql://scraper_user:scrape_password_@localhost:5432/scraper_db
   BASE_URL=https://quotes.toscrape.com
   PAGES=3
   ```

6. **Run the scraper**

   ```bash
   python -m src.main --create-tables --pages 3
   ```

## Directory Structure

```
Pywebscraper/
│
├── src/                         # Main application code
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   ├── parser.py
│   ├── scraper.py
│   └── main.py
│
├── tests/                       # Unit & integration tests
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_scraper.py
│   └── test_db.py
│
├── requirements.txt
├── pytest.ini
├── .env
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Testing

Run tests from the project root:

```bash
pytest -q
```

## License

```
This project is licensed under the MIT License.
---
