import argparse
from api.virustotal import get_reputation
from utils.file_handler import read_domains_from_file, save_report
from utils.report_generator import generate_report

def process_domains(domains):
    results = {}
    for domain in domains:
        print(f"Checking reputation for {domain}...")
        results[domain] = get_reputation(domain)
    return results

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
        domains.extend(read_domains_from_file(args.file))

    if not domains:
        print("Please provide a domain or a file containing a list of domains.")
        return

    results = process_domains(domains)
    report = generate_report(results)
    save_report(report, args.output)
    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
