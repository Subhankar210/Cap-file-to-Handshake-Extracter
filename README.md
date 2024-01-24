# WiFi Handshake Extractor

  _    _                 _     _           _          ______      _                  _            
 | |  | |               | |   | |         | |        |  ____|    | |                | |           
 | |__| | __ _ _ __   __| |___| |__   __ _| | _____  | |__  __  _| |_ _ __ __ _  ___| |_ ___ _ __ 
 |  __  |/ _` | '_ \ / _` / __| '_ \ / _` | |/ / _ \ |  __| \ \/ | __| '__/ _` |/ __| __/ _ | '__|
 | |  | | (_| | | | | (_| \__ | | | | (_| |   |  __/ | |____ >  <| |_| | | (_| | (__| ||  __| |   
 |_|  |_|\__,_|_| |_|\__,_|___|_| |_|\__,_|_|\_\___| |______/_/\_\\__|_|  \__,_|\___|\__\___|_|

## Overview

This Python script is designed to reduce the size of a .cap or .pcap file and extract WiFi WPA2 handshakes. It uses the `scapy` library to parse the input file, filter WiFi packets, and extract WPA2 handshakes, providing a new output file containing only the extracted handshakes.

## Author

- **Author:** Subhankar Senapati
- **Date:** 24/01/2024

## Usage

1. **Requirements:**
   - Python 3.x
   - Install required library using: `pip install scapy` & also 'pip install colorama'

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using: `python script_name.py`

3. **Input and Output:**
   - When prompted, enter the path to the input .cap or .pcap file.
   - Enter the desired output file path (e.g., extracted_handshakes.cap).

4. **Output:**
   - The script will extract WPA2 handshakes from the input file and save them to the specified output file.

5. **Error Handling:**
   - The script checks if the input file exists and handles exceptions during file operations.

## ASCII Art Logo

