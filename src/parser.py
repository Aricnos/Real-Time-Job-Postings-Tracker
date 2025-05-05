# parser.py
# Responsible for extracting job data from the parsed HTML (soup)

from bs4 import BeautifulSoup

def parse_jobs(html):
    soup = BeautifulSoup(html, 'html.parser')
    jobs = []

    for elem in soup.find_all('tr', class_='job'):
        title_elem = elem.find('h2')
        company_elem = elem.find('h3')
        location_elem = elem.find('div', class_='location')
        tags_elem = elem.find_all('div', class_='tag')
        date_elem = elem.find('time')

        job = {
            'title': title_elem.get_text(strip=True) if title_elem else 'N/A',
            'company': company_elem.get_text(strip=True) if company_elem else 'N/A',
            'location': location_elem.get_text(strip=True) if location_elem else 'N/A',
            'tags': " ".join(tag.get_text(strip=True) for tag in tags_elem),
            'date_posted': date_elem['datetime'] if date_elem and 'datetime' in date_elem.attrs else 'N/A'
        }
        jobs.append(job)
    return jobs