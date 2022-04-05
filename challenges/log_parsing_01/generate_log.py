import random
import datetime


OUTFILE = "vendor.log"
ROWS = 10000
STARTDATE = datetime.datetime(2020, 4, 1)

# Vendor Source: https://en.wikipedia.org/wiki/List_of_telephone_operating_companies
VENDORS = [
    "ATT",
    "Verizon Communications",
    "Deutsche Telekom",
    "China Mobile",
    "Nippon Telegraph and Telephone",
    "Comcast",
    "China Telecom",
    "Soft Bank",
    "Vodafone",
    # "América Móvil",
    "America Movil",
    "Orange",
    "Charter Communications",
    # "Telefónica",
    "Telefonica",
    "China Unicom",
    "KDDI",
    "BT Group",
    "Lumen",
    "Gruppo TIM",
    "KT Corporation",
    "Vivendi",
    "Telstra",
    "BCE",
    "China Communications Services",
    "Saudi Telecom",
    "SK Telecom",
    "SFR",
]

random.seed(1)

def genEntry():
    timestamp = moveTime()
    vendor = random.choice(VENDORS)
    amount = random.randint(1, 500)
    return f"{timestamp},{vendor},,{amount}\n"

def moveTime(minM=1, maxM=6*60):
    global STARTDATE
    # Move the date forward a random number of minutes
    minutes = random.randint(minM, maxM)
    STARTDATE += datetime.timedelta(minutes=minutes)
    return STARTDATE
    

with open(OUTFILE, "w") as vendorLog:
    for _ in range(ROWS):
        line = genEntry()
        vendorLog.write(line)
