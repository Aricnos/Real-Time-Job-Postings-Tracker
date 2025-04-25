# 🧰 RemoteOK Job Scraper

A modular Python project to scrape remote job listings from [RemoteOK.com](https://remoteok.com) and save them into a structured CSV file. Designed for real-world practice, portfolio showcasing, and easy extension.

---

## 📦 Project Structure

remoteok-job-scraper/ 
├── src/ 
│ ├── scraper.py # Entry point: orchestrates the scraping 
│ ├── parser.py # Contains HTML parsing logic 
│ └── utils.py # Utilities like saving CSV 
├── data/ 
│ └── jobs.csv # Output CSV with scraped jobs 
├── README.md # Project documentation 
├── requirements.txt # List of Python dependencies 
└── .gitignore # Prevents committing unnecessary files


---

## 🚀 Features

- Extracts:  
  ✅ Job title  
  ✅ Company name  
  ✅ Location  
  ✅ Tags (e.g., Python, Remote)  
  ✅ Posting date  

- Uses:
  - `requests` for HTTP requests
  - `BeautifulSoup` for HTML parsing
  - `csv` for structured output
  - `os` for file-safe directory handling

- Includes:
  - Robust network error handling
  - Modular structure for reusability

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/remoteok-job-scraper.git
cd remoteok-job-scraper

\### 2. Install Dependencies
pip install -r requirements.txt

\### 3. Run the scraper
python src/scraper.py

\### 4.Output location
data/jobs.csv

