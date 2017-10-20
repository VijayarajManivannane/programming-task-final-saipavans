import create_ticket as ticketgen
import requests

def getnetworkdevicecount():
    ticket = ticketgen.get_ticket()
    api = "/api/v1/network-device/count"
    controller = 'sandboxapic.cisco.com'
    url = "https://" + controller + api
    header_content = {"content-type": "application/json", "X-Auth-Token": ticket}
    response_val = requests.get(url, headers=header_content, verify=False)
    response_json = response_val.json()
    print("Number of hosts: ", response_json["response"])

getnetworkdevicecount()