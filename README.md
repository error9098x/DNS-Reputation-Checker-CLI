## DNS Reputation Checker

This Python script allows you to quickly check the reputation of domains using the VirusTotal API. It provides a user-friendly command-line interface for both single domain and batch processing, generating a JSON report of the results.

### Features

- **Single Domain Check:** Quickly analyze the reputation of a single domain.
- **Batch Processing:** Efficiently check a list of domains from a file.
- **Custom Output:** Save the report to a file with a custom name.
- **API Integration:** Uses the VirusTotal API (can be switched to other services).
- **CLI Interface:** Easy-to-use command-line arguments for flexibility.
- **JSON Report:** Generates a structured JSON file for easy analysis and sharing.

### How to Run

**1. Install dependencies:**

```bash
pip install -r requirements.txt
```

**2. Configure API key:**

- Create a file named `config.py` in the same directory as the script.
- Add your VirusTotal API key to the file:

```python
API_KEY = 'YOUR_VIRUSTOTAL_API_KEY'
API_URL = 'https://www.virustotal.com/api/v3/domains/'
```

**3. Run the script:**

**Single Domain Check:**

```bash
python dns_reputation_checker.py -d example.com
```

![Screenshot from 2024-05-31 19-35-39](https://github.com/error9098x/DNS-Reputation-Checker-CLI/assets/43810146/cad065e6-4cdc-42f9-a858-aba1949ed7ed)


**Batch Processing:**

```bash
python dns_reputation_checker.py -f domain_list.txt
```

![Screenshot from 2024-05-31 19-37-05](https://github.com/error9098x/DNS-Reputation-Checker-CLI/assets/43810146/6b567f30-8cea-49cb-84be-7319597098fe)

**Custom Output File:**

```bash
python dns_reputation_checker.py -d example.com -o custom_report.json
```

### Explanation

- **`-d`:** Specifies the domain to check (single domain check).
- **`-f`:** Specifies the file containing a list of domains (batch processing).
- **`-o`:** Specifies the name of the output JSON file.

### Requirements

- Python 3
- `requests` library (installed via `requirements.txt`)
- VirusTotal API key (sign up for free at https://www.virustotal.com/)

### Usage

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Get your VirusTotal API key:** https://www.virustotal.com/
3. **Configure API key in `config.py`:**  `API_KEY = 'YOUR_VIRUSTOTAL_API_KEY'`
4. **Run the script:** Use the provided commands above.
5. **Analyze the report:** The generated JSON file will contain details about the domain's reputation.

### Contributing

Feel free to contribute to this project by:

- **Improving the code:** Add new features, fix bugs, or enhance the existing code.
- **Suggesting improvements:** Submit ideas for new features or improvements.

### License

This project is licensed under the MIT License.

### Acknowledgements

- This project is inspired by the need for a simple and efficient tool to assess domain reputation.
- Thanks to VirusTotal for providing their valuable API.

### Disclaimer

This project is provided for educational purposes only. The author is not responsible for any misuse of this script.
