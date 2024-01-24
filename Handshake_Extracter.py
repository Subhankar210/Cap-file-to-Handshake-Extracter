from scapy.all import rdpcap, wrpcap
from colorama import Fore, Style
import random

def generate_colored_logo():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    selected_color = random.choice(colors)
    logo = f"""
    {selected_color}  _______ _                 _     _______ _           _             {Style.RESET_ALL}
    {selected_color} |__   __| |               | |   |__   __| |         | |            {Style.RESET_ALL}
    {selected_color}    | |  | |__   __ _ _ __ | | __   | |  | |__   __ _| |_ ___  ___ {Style.RESET_ALL}
    {selected_color}    | |  | '_ \ / _` | '_ \| |/ /   | |  | '_ \ / _` | __/ _ \/ __|{Style.RESET_ALL}
    {selected_color}    | |  | | | | (_| | | | |   <    | |  | | | | (_| | ||  __/\__ \\{Style.RESET_ALL}
    {selected_color}    |_|  |_| |_|\__,_|_| |_|_|\_\   |_|  |_| |_|\__,_|\__\___||___/{Style.RESET_ALL}
    """
    return logo

def reduce_and_extract(input_path, output_path):
    # Read and parse the input file
    try:
        packets = rdpcap(input_path)
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    # Filter WiFi packets
    wifi_packets = [pkt for pkt in packets if pkt.haslayer("Dot11")]

    # Extract WPA2 handshakes
    wpa2_handshakes = [pkt for pkt in wifi_packets if pkt.haslayer("EAPOL")]

    if not wpa2_handshakes:
        print("No WPA2 handshakes found in the provided file.")
        return

    # Write to a new file
    try:
        wrpcap(output_path, wpa2_handshakes)
        print(f"Extracted WPA2 handshakes saved to '{output_path}'.")
    except Exception as e:
        print(f"Error while writing to file: {e}")

if __name__ == "__main__":
    # Print the dynamically colored ASCII art logo
    print(generate_colored_logo())

    # Get user input for input and output paths
    input_file = input("Enter the path to the input .cap or .pcap file: ").strip()
    output_file = input("Enter the path for the output file (e.g., extracted_handshakes.cap): ").strip()

    # Call the function with user-provided input
    reduce_and_extract(input_file, output_file)
