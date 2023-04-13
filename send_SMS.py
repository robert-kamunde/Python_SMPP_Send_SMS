import logging
import sys
import smpplib.gsm
import smpplib.client
import smpplib.consts


message = "TEST SMS"
SMSC_IP = ''
SMSC_PORT = ''
SMPP_CLIENT_USERNAME = ''
SMPP_CLIENT_PASSWORD = ''
DESTINATION_ADDRESS_LIST = ['','']  
#destination address is receivers' phone numbers
SENDER_ID = ''
#sender ID should be whitelisted under your account by SMSC serving you


client = smpplib.client.Client(SMSC_IP, SMSC_PORT, allow_unknown_opt_params=True)

client.set_message_sent_handler(
    lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
client.set_message_received_handler(
    lambda pdu: sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id)))

client.connect()

client.bind_transceiver(system_id=SMPP_CLIENT_USERNAME, password=SMPP_CLIENT_PASSWORD)

parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(message)
destination_addresses = DESTINATION_ADDRESS_LIST
for address in destination_addresses:
    for part in parts:
            pdu = client.send_message(
            source_addr_ton=smpplib.consts.SMPP_TON_INTL,
            source_addr=SENDER_ID,

            dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
            destination_addr=address,
            short_message=part,

            data_coding=encoding_flag,
            esm_class=msg_type_flag,
            registered_delivery=True,
            )

print('SMS sent successfully')

client.unbind()
client.disconnect()
