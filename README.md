# NetReconner
A Network Intrusion Detection System is used to monitor networks for attacks or intrusions and report these intrusions to a network administrator of the organization.
The NetReconner continuously monitors the incoming and outgoing traffic on the network using a bash script with minimal downtime. This system is designed to analyze network traffic and identify potential intrusion attempts by matching packet signatures using Regular Expressions against a pre-defined database of signatures. This README file provides an overview of the system, installation instructions, configuration details, and usage guidelines.

## Features
* Packet signature matching using Regular Expressions
* Existing signature database for detecting known intrusion patterns
* A GUI form for network administrators to add new signatures to the existing database
* Real-time network traffic analysis
* Linux-based application for network reconnaissance
* Minimal downtime while capturing packets from the network

## Assumption
Most application servers in organizations are managed using a Linux-based administration. Hence this application uses Linux-based tools and commands such as `tcpdump` that are compatible with a Linux environment. It is recommended to install this application on a Linux-based OS such as Mac, Linux, or Unix or run using a virtual machine. 

## Installation
To install the NetReconner, follow these steps:
1. Clone the repository: `$ git clone https://github.com/radgupte/NetReconner.git`
2. Navigate to the project directory.
3. Install the required dependencies: `$ npm install`

## Usage
Once NetReconner is installed, you can use it to either analyze network traffic and detect potential intrusion attempts or, as an admin, add new signatures to the existing database. 
### To monitor the network, follow these steps to run the system:
1. Open the terminal.
2. Navigate to the project directory `$ cd NetReconner`.
3. Type the following command in the terminal to begin the network monitor: `./shell.sh`.
4. It will be visible on the terminal that the script runs continuously.
5. In case of a network intrusion attack, a file with the name of the attack gets populated with the payload of those malicious packets.

### To add new signatures to an existing attack type, follow these steps:
1. Open the terminal.
2. Type the following command in the terminal: `python admin_form.py`
3. A GUI form opens as a window, enter the Regular Expression for the attack in the `Regex` field and the abbreviation of the type of attack in the `Attack Type` field, then click on the `Add to data` button to submit the form.
4. A new line in the corresponding file gets added with the Regular Expression you entered in the form.
