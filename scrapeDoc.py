# print(f'Text from {url}:\n{page_text}\n')

import requests
from bs4 import BeautifulSoup
import time
import sqlite3

# Establish SQLite connection and create table
conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS documents (url TEXT PRIMARY KEY, content TEXT)''')
conn.commit()

def scrape_page(url, visited=set()):
    # Delay to avoid overloading the server
    time.sleep(2)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extracting text from the current page
        page_text = soup.get_text(separator=' ', strip=True)

        print(f'Text from {url}:\n{page_text}\n')
        # Store text in SQLite database
        c.execute("INSERT OR IGNORE INTO documents (url, content) VALUES (?, ?)", (url, page_text))
        conn.commit()
        # Extracting all links on the page
        for link in soup.find_all('a', href=True):
            link_url = link['href']
            # Ignore bookmarks on the same page
            if not link_url.startswith('#'):
                # If the link is relative, make it absolute
                if not link_url.startswith(('http:', 'https:')):
                    link_url = response.url.rsplit('/', 1)[0] + '/' + link_url
                # Avoid visiting the same URL twice
                if link_url not in visited:
                    visited.add(link_url)
                    scrape_page(link_url, visited)
    else:
        print(f'Failed to retrieve page with status code: {response.status_code}')

def display_text():
    for row in c.execute('SELECT content FROM documents'):
        print(row[0])

# Start scraping from input URL
start_url = input('Enter a URL: ')

scrape_page(start_url)
display_text()

# Close SQLite connection
conn.close()
