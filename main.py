from bs4 import BeautifulSoup
import requests
import csv

# Fetch the webpage
response = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes and authors
produse = soup.findAll("div", attrs={"class": "caption"})
#authors = soup.findAll("small", attrs={"class": "author"})

# Open a CSV file to write the data
with open('produse.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # (Optional) Write a header row
    writer.writerow(['produse'])

    # Iterate over the quotes and authors and write them to the CSV
    for produs in produse:
        produs_text = produs.get_text(strip=True)
      #  author_text = author.get_text(strip=True)

        # Print to console
        print(f"{produs_text}")

        # Write to CSV
        writer.writerow([produs_text])

