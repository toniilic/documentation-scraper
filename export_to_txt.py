import sqlite3

def export_to_txt():
    # Establish SQLite connection
    conn = sqlite3.connect('scraped_data.db')
    c = conn.cursor()

    with open("exported_data.txt", "w") as f:
        for row in c.execute('SELECT content FROM documents'):
            content = row[0]
            f.write(f"{content}\n") # Content: 
            #f.write("="*50 + "\n")

    # Close SQLite connection
    conn.close()

if __name__ == "__main__":
    export_to_txt()
