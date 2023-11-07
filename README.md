# Documentation Scraper

## Description
This project consists of two Python scripts designed to scrape documentation or textual content from websites and export the collected data to a text file. The `scrapeDoc.py` script scrapes content from specified URLs and stores it in a SQLite database, while the `export_to_txt.py` script exports the content from the database to a `.txt` file.

## Installation
To run these scripts, you will need Python installed on your system. You will also need to install the required libraries:

```bash
pip install requests beautifulsoup4 sqlite3
```

Clone the repository to your local machine:
```bash
git clone https://github.com/toniilic/documentation-scraper.git
cd documentation-scraper
```

## Usage

First, run the scraper to collect data from web pages:

```bash
python scrapeDoc.py
```

Once you have collected enough data, you can export it to a text file:
```bash
python export_to_txt.py
```
