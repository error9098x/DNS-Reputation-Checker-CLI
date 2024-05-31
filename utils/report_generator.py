def generate_report(results):
    report = []
    for domain, data in results.items():
        report.append({
            'domain': domain,
            'reputation': data
        })
    return report
