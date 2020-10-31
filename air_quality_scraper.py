import xml.etree.ElementTree as ET
import requests
import pandas as pd 

url = 'https://apps.des.qld.gov.au/air-quality/xml/feed.php?category=1&region=ALL'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)

root = ET.fromstring(response.content)
listo = []

for station in root.iter('station'):
    dicto = {'station': f"{station.attrib['name']}", "longitude": f"{station.attrib['longitude']}", "latitude": f"{station.attrib['latitude']}"}
    for thingy in station:
        reading = {f"{thingy.attrib['name']}":f"{thingy.attrib['index']}"}

        dicto.update(reading)
    listo.append(dicto)



df = pd.DataFrame(listo)

with open("air_qualtiy.csv", "w") as f:
    df.to_csv(f,index=False)
