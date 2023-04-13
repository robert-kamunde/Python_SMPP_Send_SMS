#Sending SMS using SMPP protocol
This is a Python script for sending SMS using the SMPP (Short Message Peer-to-Peer) protocol. It uses the smpplib library to communicate with an SMSC (Short Message Service Center) to send SMS messages.

#Prerequisites
Before using this script, you need to have the following:

Access to an SMSC that supports the SMPP protocol
A username and password to authenticate your SMPP client with the SMSC
A sender ID that is whitelisted under your account by the SMSC serving you
Destination phone numbers (in international format) for the SMS recipients
Installation
To use this script, you need to install the smpplib library:

#Usage
Update the following variables in the script with your SMSC and account details:

SMSC_IP: The IP address of your SMSC
SMSC_PORT: The port number of your SMSC
SMPP_CLIENT_USERNAME: Your SMPP client username
SMPP_CLIENT_PASSWORD: Your SMPP client password
DESTINATION_ADDRESS_LIST: A list of destination phone numbers for the SMS recipients (in international format)
SENDER_ID: Your whitelisted sender ID

#License
This script is licensed under the MIT License. See the LICENSE file for details.

#Credits
This script uses the smpplib library for communicating with the SMSC.
