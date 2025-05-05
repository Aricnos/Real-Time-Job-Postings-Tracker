# Selenium Job Scraper

A real-world web scraping project built with Selenium and BeautifulSoup to scrape remote job listings from [remoteok.com](https://remoteok.com), using the Brave browser.

## 🔧 Features

- Uses Selenium for dynamic content rendering
- Parses HTML with BeautifulSoup
- Modular structure: `scraper.py`, `parser.py`, `utils.py`, `config.py`
- Saves data to `output/jobs.csv`
- GitHub-ready with proper structure and documentation

## 📦 Project Structure

remoteok-job-scraper/ 
├── src/ 
│ ├── scraper.py # Entry point: orchestrates the scraping 
│ ├── parser.py # Contains HTML parsing logic
│ ├── config.py # Contains browser and chromedriver path in local
│ ├── main.py # Main function of the project
│ └── utils.py # Utilities like saving CSV 
├── output/ 
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
python src/main.py

\### 4.Output location
data/jobs.csv

