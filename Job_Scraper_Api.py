import requests
import json
import time
import random

# API endpoints (example URLs, replace with actual ones if available)
API_URLS = {
    "LinkedIn": "https://api.linkedin.com/v2/jobSearch?q=PostgreSQL",
    "Indeed": "https://api.indeed.com/v2/jobs?q=PostgreSQL",
    "Glassdoor": "https://api.glassdoor.com/api/jobs?q=PostgreSQL"
}

# API Headers (replace with actual API keys or authentication tokens)
HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to fetch job listings from APIs
def fetch_jobs_from_api(api_name, url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            jobs = response.json()
            return jobs
        else:
            print(f"Failed to retrieve jobs from {api_name}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching jobs from {api_name}: {e}")
    return []

# Run job fetching for each platform
def main():
    all_jobs = {}
    for platform, url in API_URLS.items():
        print(f"Fetching jobs from {platform} API...")
        jobs = fetch_jobs_from_api(platform, url)
        all_jobs[platform] = jobs
        time.sleep(random.uniform(2, 5))  # Prevent API rate limiting

    # Save results to a JSON file
    with open("job_listings_api.json", "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, indent=4)
    print("Job listings saved to job_listings_api.json")

if __name__ == "__main__":
    main()
