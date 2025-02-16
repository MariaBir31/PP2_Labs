import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format(
    "DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Parse JSON and print rows
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print("{:<50} {:<20} {:<10} {:<10}".format(dn, descr, speed, mtu))