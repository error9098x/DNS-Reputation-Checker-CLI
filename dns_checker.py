import requests
import argparse
import json

# Replace 'YOUR_API_KEY_HERE' with your actual API key from VirusTotal or AlienVault OTX
API_KEY = 'YOUR_API_KEY_HERE'
API_URL = 'https://www.virustotal.com/api/v3/domains/'  # Example for VirusTotal

def get_reputation(domain):
    headers = {
        'x-apikey': API_KEY
    }
    response = requests.get(API_URL + domain, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}

def process_domains(domains):
    results = {}
    for domain in domains:
        print(f"Checking reputation for {domain}...")
        results[domain] = get_reputation(domain)
    return results

def save_report(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Report saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="DNS Reputation Checker CLI")
    parser.add_argument("-d", "--domain", help="Single domain to check")
    parser.add_argument("-f", "--file", help="File containing list of domains to check")
    parser.add_argument("-o", "--output", help="Output file to save the report", default="report.json")

    args = parser.parse_args()

    domains = []
    
    if args.domain:
        domains.append(args.domain)

    if args.file:
        with open(args.file, 'r') as f:
            domains.extend([line.strip() for line in f.readlines()])

    if not domains:
        print("Please provide a domain or a file containing a list of domains.")
        return

    results = process_domains(domains)
    save_report(results, args.output)

if __name__ == "__main__":
    main()