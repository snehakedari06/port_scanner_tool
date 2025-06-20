PORT SCANNER TOOL

OVERVIEW:
This Python-based Port Scanner tool is designed to identify open ports on a target machine. 
It provides information about the associated services and logs results into a file for further analysis. 
This tool is simple, efficient, and user-friendly.

FEATURES:
1. Scans a specified range of ports on a target IP or hostname.
2. Identifies open ports and their associated services.
3. Provides a detailed summary of scan results at the end.
4. Saves the scan results to a file named `scan_results.txt`.

SYSTEM REQUIREMENTS:
1. Python version: 3.7 or later.
2. No external libraries are required (only standard Python libraries).

HOW TO USE:
1. Download or clone the repository containing this tool.
2. Open a terminal and navigate to the folder containing the script.
3. Run the script by typing:
   `python port_scanner.py`
4. Enter the following details when prompted:
   - Target IP or hostname.
   - Starting port.
   - Ending port.
5. View the scan results in the terminal and in the `scan_results.txt` file.

EXAMPLE USAGE:
Input:
Enter target IP or hostname: google.com
Enter starting port: 1
Enter ending port: 90

<h2>Output (Terminal):
Resolved target IP: 142.250.190.78
Scanning target: 142.250.190.78 (Ports 1-90)</h2><br>
[OPEN] Port 80: HTTP - Web traffic on unencrypted websites<br>
[OPEN] Port 443: HTTPS - Secure web traffic with encryption<br>

Scan Summary:
Port 80: HTTP - Web traffic on unencrypted websites
Port 443: HTTPS - Secure web traffic with encryption

<h2>Output (scan_results.txt):
Scanning target: 142.250.190.78 (Ports 1-90)</h2>
<br>
[OPEN] Port 80: HTTP - Web traffic on unencrypted websites<br>
[OPEN] Port 443: HTTPS - Secure web traffic with encryption<br>

DISCLAIMER:
This tool is intended for educational purposes and authorized use only. 
Unauthorized scanning of networks or systems without explicit permission is illegal 
and can lead to serious legal consequences. Use this tool responsibly.

ABOUT THE TOOL:
The Port Scanner is ideal for:
1. Learning about network security and port scanning techniques.
2. Testing your own network or systems for potential vulnerabilities.
3. Understanding the purpose of various ports and their common uses.

LICENSE:
This tool is released under the MIT License, allowing for free usage, modification, 
and distribution with proper attribution.
