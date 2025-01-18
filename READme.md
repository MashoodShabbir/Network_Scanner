# Network Scanner

This Python script is a simple network scanner that identifies the IP and MAC addresses of devices connected to a given network. It uses the Scapy library to send ARP requests and parse responses, providing a list of active devices on the target network.

## Features
- Scans a specified target network or IP range for connected devices.
- Outputs the IP and MAC addresses of detected devices in a clear and readable format.
- Easy to use and customizable for various networking tasks.

## Requirements

To run this script, you need to have the following installed:

- Python 3.6+
- Scapy library

You can install Scapy using pip if it's not already installed:
```bash
pip install scapy
```

## How to Use

1. Clone the repository or download the script:
```bash
git clone https://github.com/MashoodShabbir/Network_Scanner.git
```

2. Navigate to the directory containing the script:
```bash
cd Network_Scanner
```

3. Run the script with Python, providing the target network or IP range using the `-t` or `--target` flag:
```bash
python3 network_scanner.py -t <target-network>
```
Example:
```bash
python network_scanner.py -t 192.168.1.0/24
```

4. The script will display a list of devices found on the network:
```bash
IP               MAC Address
--------------------------------
192.168.1.1     00:11:22:33:44:55
192.168.1.2     66:77:88:99:AA:BB
```

## Arguments
- `-t`, `--target`: Specifies the target network or IP range to scan. This argument is required.

## Example Output
```bash
IP               MAC Address
--------------------------------
192.168.1.1     00:11:22:33:44:55
192.168.1.2     66:77:88:99:AA:BB
192.168.1.3     CC:DD:EE:FF:00:11
```

## Important Notes
- **Run as Administrator**: This script requires administrative privileges to send ARP requests. Make sure to run it with appropriate permissions.
- **Use Responsibly**: Ensure you have permission to scan any network before using this script. Unauthorized network scanning may be illegal.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it responsibly.

## Contributing
Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

## Contact
If you have any questions or feedback, feel free to contact me at [your-email@example.com].

---

Thank you for checking out my project! I hope this helps demonstrate my Python skills and interest in networking and cybersecurity.

