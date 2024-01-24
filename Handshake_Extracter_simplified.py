import os
from scapy.all import rdpcap, wrpcap, Dot11
from colorama import Fore, Style
import random

def generate_colored_logo():
    # Define available colors
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    
    # Select a random color
    selected_color = random.choice(colors)
    
    # Define the author name
    author_name = "By Subhankar"
    
    # Create a colored ASCII art logo with the author name
    logo = f"""
    {selected_color}
  _    _                 _     _           _          ______      _                  _               {author_name}
 | |  | |               | |   | |         | |        |  ____|    | |                | |           
 | |__| | __ _ _ __   __| |___| |__   __ _| | _____  | |__  __  _| |_ _ __ __ _  ___| |_ ___ _ __ 
 |  __  |/ _` | '_ \ / _` / __| '_ \ / _` | |/ / _ \ |  __| \ \/ | __| '__/ _` |/ __| __/ _ | '__|
 | |  | | (_| | | | | (_| \__ | | | | (_| |   |  __/ | |____ >  <| |_| | | (_| | (__| ||  __| |   
 |_|  |_|\__,_|_| |_|\__,_|___|_| |_|\__,_|_|\_\___| |______/_/\_\\__|_|  \__,_|\___|\__\___|_|   
    {Style.RESET_ALL}
    """
    return logo

def reduce_and_extract(input_paths, output_folder):
    for input_path in input_paths:
        try:
            # Read and parse the input file
            packets = rdpcap(input_path)
        except FileNotFoundError:
            print(f"Error: File '{input_path}' not found.")
            continue
        except Exception as e:
            print(f"Error: {e}")
            continue

        # Filter WiFi packets for WEP, WPA, and WPA2
        wep_packets = [pkt for pkt in packets if pkt.haslayer(Dot11) and pkt[Dot11].type == 2]  # WEP
        wpa_packets = [pkt for pkt in packets if pkt.haslayer(Dot11) and pkt[Dot11].type == 2 and pkt[Dot11].subtype == 8]  # WPA
        wpa2_handshakes = [pkt for pkt in packets if pkt.haslayer(Dot11) and pkt[Dot11].type == 2 and pkt[Dot11].subtype == 8 and pkt.haslayer("EAPOL")]  # WPA2

        if not any([wep_packets, wpa_packets, wpa2_handshakes]):
            print(f"No handshakes found in the file: {input_path}")
            continue

        # Create handshake folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Construct the output file path
        output_file = os.path.join(output_folder, f"extracted_handshakes_{os.path.splitext(os.path.basename(input_path))[0]}.cap")

        try:
            # Combine all types of handshakes
            all_handshakes = wep_packets + wpa_packets + wpa2_handshakes
            wrpcap(output_file, all_handshakes)
            print(f"Handshakes from '{input_path}' saved to '{output_file}'.")
        except Exception as e:
            print(f"Error while writing to file: {e}")

if __name__ == "__main__":
    # Display the colored ASCII art logo with the author name
    print(generate_colored_logo())

    # Continuously prompt for input files and extract handshakes
    input_files = []
    while True:
        input_file = input("Enter the path to the input .cap or .pcap file (or type 'exit' to end): ").strip()

        # Check if the user wants to exit
        if input_file.lower() == 'exit':
            print("Exiting the script. Goodbye!")
            break

        input_files.append(input_file)

    # Get user input for output folder
    output_folder = "handshake"

    # Call the function with user-provided input
    reduce_and_extract(input_files, output_folder)
