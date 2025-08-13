from .config import Settings
from .db import Base, init_engine, get_session
from .models import Author, Quote
from .parser import parse_quotes
from .scraper import build_session, fetch_html
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
import argparse

def get_or_create_author(name, session):
    author = session.execute(select(Author).where(Author.name == name)).scalar_one_or_none()
    if not author:
        author = Author(name=name)
        session.add(author)
        session.flush()
    return author

def save_quotes(quotes, source_url, session):
    for item in quotes:
        author = get_or_create_author(item["author"], session)
        q = Quote(text=item["text"], tags=item["tags"], source_url=source_url, author=author)
        try:
            session.add(q)
            session.commit()
        except IntegrityError:
            session.rollback()

def run(base_url, pages):
    session = get_session()
    http = build_session()
    for p in range(1, pages + 1):
        url = f"{base_url}/page/{p}/"
        html = fetch_html(http, url)
        items = parse_quotes(html)
        if not items:
            break
        save_quotes(items, url, session)

def main():
    st = Settings.load()
    parser = argparse.ArgumentParser()
    parser.add_argument("--create-tables", action="store_true")
    args = parser.parse_args()
    engine = init_engine(st.database_url)
    if args.create_tables:
        Base.metadata.create_all(bind=engine)
    run(st.base_url, st.pages)

if __name__ == "__main__":
    main()
    