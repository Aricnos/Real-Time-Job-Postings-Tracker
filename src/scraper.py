# this script coordinates fetching, parsing and sacing job listings

import argparse
import time
from bs4 import BeautifulSoup
from src.parser import parser_job_listings
from src.utils import save_to_csv
import requests

def scrape_jobs(url):
    repsonse = requests.get(url)
    repsonse.raise_for_status()
    soup = BeautifulSoup(repsonse.text, 'htmlparser')
    jobs = parser_job_listings(soup)

    time.sleep(2) # be polite to the site

    return jobs


def main():

    parse = argparse.ArgumentParser(description='Scrape remote job listing from a url')
    parse.add_argument('url', type=str, help='The Url for job listing to scrape from')
    parse.add_argument('output_file', type=str, help='The CSV file to save the scrape data to')
    args = parse.parse_argv()

    jobs  = scrape_jobs(args.url)
    save_to_csv(jobs, args.output_file)
    print(f"Scraped {len(jobs)} jobs and saved to {args.output_file}")

if __name__ =='__main__':
    main()