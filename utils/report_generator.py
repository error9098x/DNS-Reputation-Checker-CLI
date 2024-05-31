from rich.console import Console
from rich.table import Table

def generate_report(results):
    console = Console()
    for domain, data in results.items():
        if "error" in data:
            console.print(f"[red]{domain}: {data['error']}[/red]")
        else:
            table = Table(title=f"Reputation for {domain}")
            table.add_column("Engine", style="cyan")
            table.add_column("Category", style="magenta")
            table.add_column("Result", style="green")
            
            if 'data' in data and 'attributes' in data['data']:
                for engine, result in data['data']['attributes']['last_analysis_results'].items():
                    category = result['category'] if 'category' in result else 'Unknown'
                    table.add_row(engine, category, result['result'])
            else:
                console.print(f"[yellow]No reputation data found for {domain}[/yellow]")
                
            console.print(table)