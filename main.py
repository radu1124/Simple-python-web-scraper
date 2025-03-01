from bs4 import BeautifulSoup
import requests
import csv

# Fetch the webpage
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes and authors
quotes = soup.findAll("span", class_="text")
authors = soup.findAll("small", class_="author")

# Open a CSV file to write the data
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write a header row
    writer.writerow(['Quote', 'Author'])

    # Iterate over quotes and authors and write them to the CSV
    for quote, author in zip(quotes, authors):
        quote_text = quote.get_text(strip=True)
        author_text = author.get_text(strip=True)

        # Print to console
        print(f'{quote_text} - {author_text}')

        # Write to CSV
        writer.writerow([quote_text, author_text])

print("Scraping completed. Data saved to quotes.csv.")
