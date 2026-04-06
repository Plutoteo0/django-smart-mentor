import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

def scrape_django_docs(urls, output_csv='data/django_data.csv'):
    result = []

    for url in urls:
        print(f"[INFO] Scraping {url}...")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        main_content = soup.find('main')
        
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return
    


        if not main_content:
            print("Main content not found.")
            return
    
        current_topic = "Intro"
        current_content = ""
        current_code = ""

        all_elements = main_content.find_all(['h1', 'h2', 'h3', 'p', 'div'])

        for el in all_elements:
            if el.name in ['h1', 'h2', 'h3']:
                if current_content.strip() or current_code.strip():
                    result.append({
                        'Source': url.split('/')[-2],
                        'Topic': current_topic.replace('¶', '').strip(),
                        'Content': current_content.strip(),
                        'Code': current_code.strip()
                })
            
                current_topic = el.get_text().replace('¶', '').strip()
                current_content = ""
                current_code = ""

            elif el.name == 'div' and 'highlight' in el.get('class', []):
                current_code += el.get_text() + "\n\n"

            elif el.name == 'p':
                if not el.find_parent('div', class_='highlight'):
                    current_content += el.get_text() + "\n\n"

    
    result.append({
        'Source': url.split('/')[-2],
        'Topic': current_topic,
        'Content': current_content.strip(),
        'Code': current_code.strip()
    })

    time.sleep(1)

    df = pd.DataFrame(result)
    df = df[df['Content'] != '']

    df.to_csv(output_csv, mode='a', header=not os.path.exists('django_data.csv') ,index=False, encoding='utf-8')
    print(f"[SUCCESS] Data scraped and saved to {output_csv}")

# Past the Django docs Urls you want to scrape here
urls = [
    "https://docs.djangoproject.com/en/6.0/topics/db/models/",
    "https://docs.djangoproject.com/en/6.0/topics/db/queries/",
    "https://docs.djangoproject.com/en/6.0/topics/db/aggregation/",
]

scrape_django_docs(urls)