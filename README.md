# Traffic Analyzer

### Purpose and Features

Welcome to Traffic Analyzer! This is a program designed for network analysis using Nmap. It allows you to:
- Monitor network connections.
- Generate reports.
- Send notification emails for services that are registered in the system's local and remote

Use Traffic Analyzer responsibly and follow the documentation on GitHub for instructions.
### Requirements

Here is the section with the requirements and instructions on how to create a virtual environment in English:
Requirements

Before running Traffic Analyzer, make sure you have the following dependencies installed:

    python-nmap
    psutil
    ip2geotools
    pandas
    pyarrow
    PyQt5
    python-dotenv

You can install these dependencies manually using pip:
```
pip install python-nmap psutil ip2geotools pandas pyarrow PyQt5 python-dotenv
```

Or
```
pip install requirements.txt
```
### Creating a Virtual Environment
It is recommended to create a virtual environment to install dependencies in isolation and avoid conflicts with other applications. Follow these steps to create and activate a virtual environment:
1. Install virtualenv if you don't have it already:
```
pip install virtualenv
```

2. Create a new directory for your project and navigate into it:

```
mkdir traffic_analyzer_project
cd traffic_analyzer_project
```
3. Create a virtual environment within the project directory:
```
virtualenv venv
```
4. Start env

On Windows:
```
venv\Scripts\activate
```

On macOS and Linux:
```
source venv/bin/activate
```


### Usage

1. Clone the repository:

```
git clone https://github.com/JoseLeviRivera/Traffic-Analyzer.git
```
2. Navigate to the project directory:
```
cd Traffic-Analyzer
```
3. Running the Script
```
python3 traffic_analyzer.py [options]
```

### Options
    -h, --help: Show the help message and exit.
    -ip: Specify the target IP address to scan.
    -p, --port: Specify a single port to scan.
    -r, --range: Specify a range of ports to scan.
    --run-cve: Run CVE script for a specific port.
    --network-monitor: Monitor network connections and display details.
    --output-file: Specify the output file for analysis results.
    --email: Enable email report sending.
    --username: Username for email login.
    --password: Password for email login.
    --recipient: Email address of the recipient.

Thank you for using Traffic Analyzer. Happy analyzing!