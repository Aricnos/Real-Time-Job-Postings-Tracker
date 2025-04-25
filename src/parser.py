from bs4 import BeautifulSoup

# defining the job parsing function
def parser_job_listings(html):
    soup = BeautifulSoup(html, 'html.parser')
    job_rows = soup.find_all('tr', class_ = 'job')

    jobs = []

    for job in job_rows:
        title_tag = job.find('h3')
        company_tag = job.find('h2')
        location_tag = job.find('div', class_='location')
        tags = job.find_all('div', class_ = 'tag')
        date_tag = job.find('time')

        data = {
            'title':title_tag.get_text(strip=True) if title_tag else 'N/A', 
            'company': company_tag.get_text(strip=True)if company_tag else 'N/A', 
            'loaction': location_tag.get_text(strip=True) if location_tag else 'N/A',
            'tag':', '.join(tag.get_text(strip=True) for tag in tags),
            'date_posted': date_tag['datetime'] if date_tag and date_tag.has_attr('datetime') else 'N/A'
        }
        jobs.append(data)

    return jobs