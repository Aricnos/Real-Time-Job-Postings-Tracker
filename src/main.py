from scraper import fetch_page_source
from parser import parse_jobs
from utils import save_to_csv

def main():
    url = "https://remoteok.com"
    html = fetch_page_source(url)
    jobs = parse_jobs(html)
    print(f"Scraper {len(jobs)} jobs.")
    save_to_csv(jobs)

if __name__ =='__main__':
    main()
