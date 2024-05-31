import argparse
from rich import print
from rich.progress import track
from api.virustotal import get_reputation
from utils.file_handler import read_domains_from_file, save_report
from utils.report_generator import generate_report

def process_domains(domains):
    results = {}
    for domain in track(domains, description="Checking domain reputations..."):
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
        print("[red]Please provide a domain or a file containing a list of domains.[/red]")
        return

    results = process_domains(domains)
    generate_report(results)
    save_report(results, args.output)
    print(f"Report saved to [green]{args.output}[/green]")

if __name__ == "__main__":
    main()