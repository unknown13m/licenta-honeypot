import json
import time
import subprocess
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['honeypot_db']
collection = db['attacks']

print("scriptul a pornit...asteptam atacurile")

def process_ssh():
    subprocess.run([
        'docker',
        'cp',
        'licenta-honeypot-ssh-1:/cowrie/cowrie-git/var/log/cowrie/cowrie.json',
        'atacs.json'
    ])

    try:
        with open('atacs.json', 'r') as f:
            for line in f:
                data = json.loads(line)
                if 'eventid' in data and 'login' in data['eventid']:
                    data['type'] = 'SSH'
                    collection.update_one(
                        {
                            'timestamp': data['timestamp'],
                            'src_ip': data['src_ip']
                        },
                        {
                            '$set': data
                        },
                        upsert=True
                    )
    except Exception as e:
        print(f"Eroare SSH: {e}")


def process_medical():
    try:
        result = subprocess.run(
            ['docker', 'logs', 'licenta-honeypot-medical-1'],
            capture_output=True,
            text=True
        )

        for linie in result.stdout.splitlines():
            if linie.strip() and "socat" not in linie and "supports write-only" not in linie:
                timestamp_curent = time.strftime("%Y-%m-%dT%H:%M:%SZ")
                gasit = collection.find_one({"raw_data": linie.strip()})

                if gasit == None:
                    entry = {
                        "timestamp": timestamp_curent,
                        "src_ip": "Detectat pe Port 104",
                        "type": "DICOM/Medical",
                        "raw_data": linie.strip()
                    }

                    collection.insert_one(entry)

    except Exception as e:
        print("Eroare Medical:", e)


while True:
    process_ssh()
    process_medical()
    time.sleep(10)