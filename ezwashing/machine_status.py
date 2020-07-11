from ezwashing import config
import requests
from bs4 import BeautifulSoup

def get_machine_status():
    # Create a dictionary to store each machine's name and status.
    machine_status = {}
    # Process HTML
    request = requests.post(config.url, cookies=config.cookies, data=config.data)
    html_doc = request.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    # Loop through machine status
    for i in config.machine_id_info:
        machine_status.update({soup.find(id=i[0]).text : [soup.find(id=i[1]).text, soup.find(id=i[2]).text]})
    return machine_status

