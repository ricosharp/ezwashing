import requests
import os

username = os.getenv("EZWASHING_USERNAME")
password = os.getenv("EZWASHING_PASSWORD")

url = 'http://www.mylaundryaware.com/washingtoncommercial/Default.aspx'
cookies = {
    'DATABASE_ID' : 'A29AB91C76D274E555DE3610F44116C938250C210AE2867C397A3AF6AC875ACD437035B76F2F63296839C59A8AB14D8D',
    'GROUP_ID' : '49D47B06801900B2266BA3CF7652BDDB30CFFFE855482F1BF3A2654C7F28460E3DBD0D48CFA15E6DE031A5502EBF6687',
}
data = {
    '__LASTFOCUS' : 'ctl00_ToolkitScriptManager1_HiddenField: ;;AjaxControlToolkit, Version=3.0.30512.20315, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:2a404968-beb9-41c5-98fb-26019e941d81:e2e86ef9:1df13a87:8ccd9c1b:9ea3f0e2:9e8e87e9:4c9865be:ba594826:757f92c2:fde3863c',
    '__EVENTTARGET' : '',
    '__EVENTARGUMENT' : '',
    '__VIEWSTATE' : '/wEPDwULLTEzMzIzMDY4MDcPZBYCZg9kFgICAw9kFgICBQ9kFgICAw9kFgRmD2QWAgIDD2QWAgIED2QWAgIBD2QWAmYPEGQPFglmAgECAgIDAgQCBQIGAgcCCBYJEAUSLSBDaG9vc2UgQ2FycmllciAtBRItIENob29zZSBDYXJyaWVyIC1nEAUEQVQmVAULdHh0LmF0dC5uZXRnEAUMQm9vc3QgTW9iaWxlBRFteWJvb3N0bW9iaWxlLmNvbWcQBQZOZXh0ZWwFFG1lc3NhZ2luZy5uZXh0ZWwuY29tZxAFBlNwcmludAUXbWVzc2FnaW5nLnNwcmludHBjcy5jb21nEAUIVC1Nb2JpbGUFC3Rtb21haWwubmV0ZxAFB1Zlcml6b24FCXZ0ZXh0LmNvbWcQBQ1WaXJnaW4gTW9iaWxlBQl2bW9ibC5jb21nEAUGQWxsdGVsBRJtZXNzYWdlLmFsbHRlbC5jb21nZGQCAQ9kFgICAQ9kFgJmD2QWAmYPZBYCAgEPDxYCHgRUZXh0BSNXYXNoaW5ndG9uIENvbW1lcmNpYWwgTGF1bmRyeSBBd2FyZWRkGAEFGmN0bDAwJGNwaF9wcmltYXJ5JG12U2lnbnVwDw9kZmSvEN2d+wNzt/jIEV1PJMVlYHgq/47vKWyyGAOs7JbPzA==',
    '__VIEWSTATEGENERATOR' : '7AD11452',
    '__PREVIOUSPAGE' : 'JuZWDQ9exHYiy7B7GqufJLbIhI9nMp37JluDtH_s5qozm2UZb6ssUiUo__sgg_6qD4rY4SQ45SbOAdPbBxofwVBYjoo1FBoEvMHn5w5KE7gghsx0qbmSP94d7pzw0U_q0',
    '__EVENTVALIDATION' : '/wEdAB08oo1PVymsAgaektEupReqoMHUIT8p3om0z2RmJP4QVfiNmq/ComCF0+SFbNy1Ha4ivUGcvaV4zFETK0Yb/DdIJDQl/RaNetl0hTJUvd2kveCunH4cR+Ncn+RLtWc29f/JykxWXZMg0cuLE3SGOOerhrT4ccJYlkH6CIeldoGbYYRWCE0im0Pbke/rsxezwhspL+h1mPyA+nMRHyBWaE/ney4BDRbyT3nWdrirX1/KzbG0x6c99wzheNMEHcWIldW9hOLgsQqzMyAp6hcDxf7f3cqtBkcjO/GlLVW3LWW/0p4IhyNkaUxpprSMceNCMK+k9kKxRvXBragPLlFQkBjCsrGVLAHPSXasrpGoBEKJza9bMpaJtFA3Lq4zhiIKEDNEV0sqH6DdWugPdERNu3rJkP9tF8Z/QOnux+UrlpNoN95+q8uf7Oy/KZbcHDnJ53QuRsBoFHUkzmeDMIQLCShWhaHupdhPzqoYyx/VFufP9tUKknRw+NNMlefvZilAkGAPSXVKgNPL77hM9170rdbtJSpA3ZnyaTqab2PhFMTG9HycXDb+mXY2QhSU3AFqRICeiLUzupj4p+eLHhrUQx+hovFi6Q/o/31vyIWSixOSdRXUxV6YsZJspYxrk8ipvtOjhb5DgCkshxCO8E/+1CVD',
    'ctl00$cph_primary$txtLoginEmail' : username,
    'ctl00$cph_primary$txtLoginPassword' : password,
    'ctl00$cph_primary$btnLogIn' : 'Log In',
}

# These are just the HTML id's of each machine's name, status and availability. Can probably be coded better to be grabbed automatically.
machine_id_info = [
    # Washer 1
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl03_lblMachineName','ctl00_ctl00_cph_primary_cph_secondary_ctl03_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl03_lblTimeRemainig'],
    # Washer 2
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl04_lblMachineName','ctl00_ctl00_cph_primary_cph_secondary_ctl04_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl04_lblTimeRemainig'],
    # Washer 3
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl05_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl05_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl05_lblTimeRemainig'],
    # Washer 4
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl06_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl06_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl06_lblTimeRemainig'],
    # Washer 5
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl07_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl07_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl07_lblTimeRemainig'],
    # Washer 6
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl08_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl08_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl08_lblTimeRemainig'],
    # Washer 7
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl09_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl09_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl09_lblTimeRemainig'],
    # Big Dryer 01
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl10_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl10_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl10_lblTimeRemainig'],
    # Dryer 03
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl11_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl11_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl11_lblTimeRemainig'],
    # Dryer 05
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl12_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl12_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl12_lblTimeRemainig'],
    # Dryer 06
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl13_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl13_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl13_lblTimeRemainig'],
    # Dryer 07
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl14_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl14_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl14_lblTimeRemainig'],
    # Dryer 08
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl15_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl15_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl15_lblTimeRemainig'],
    # Dryer 04
    ['ctl00_ctl00_cph_primary_cph_secondary_ctl16_lblMachineName', 'ctl00_ctl00_cph_primary_cph_secondary_ctl16_lblAvailability', 'ctl00_ctl00_cph_primary_cph_secondary_ctl16_lblTimeRemainig']
]
