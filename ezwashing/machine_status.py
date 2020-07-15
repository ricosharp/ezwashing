from ezwashing import config
import requests
from bs4 import BeautifulSoup
from threading import Timer

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

def machine_timer():
    # Make status available outside this function with global
    # status is used by the index function in routes, which is passed into the jinja template
    # Next, create a timer to repeatedly call this function
    global status
    status = get_machine_status()
    Timer(30.0, machine_timer).start()

# Start the timer
machine_timer()