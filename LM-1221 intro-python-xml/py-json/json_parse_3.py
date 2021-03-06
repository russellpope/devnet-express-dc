# Examples
food = {"vegetables": ["carrots", "kale", "cucumber", "tomato"]}
print(food["vegetables"][1])
for veg in food["vegetables"]:
    print(veg)

cars = {"sports": {"Porsche": "Volkswagon", "Viper": "Dodge", "Corvette": "Chevy"}}
print(cars["sports"]["Corvette"])
for auto in cars["sports"]:
    print(auto, cars["sports"][auto])

# Add Python code to print out one value for each of the json objects.

dessert = {"iceCream": ["Rocky-Road", "strawberry", "Pistachio-Cashew", "Pecan-Praline"]}

# One of many ways to do this
for i in dessert['iceCream']:
    if i == "Rocky-Road":
        print(i)


soup = {"soup": {"tomato": "healthy", "onion": "bleh!", "vegetable": "goodForYou"}}

ticket = {
    "response": {"serviceTicket": "ST-16891-ugqKRVvCfPJcEaGXnGEN-cas", "idleTimeout": 1800, "sessionTimeout": 21600},
    "version": "1.0"}

network = {"Network": {"router": {"ipaddress": "192.168.1.21", "mac_address": "08:56:27:6f:2b:9c"}}}


hosts = {"response": [
    {"id": "4c60d6a7-4812-40d6-a337-773af2625e56", "hostIp": "65.1.1.86", "hostMac": "00:24:d7:43:59:d8",
     "hostType": "wireless"},
    {"id": "3ef5a7c3-7f74-4e57-a5cb-1448fbda5078", "hostIp": "207.1.10.20", "hostMac": "5c:f9:dd:52:07:78",
     "hostType": "wired"},
    {"id": "12f9c920-24fa-4d32-bf39-4c63813aecd8", "hostIp": "212.1.10.20", "hostMac": "e8:9a:8f:7a:22:99",
     "hostType": "wired"}], "version": "1.0"}

# Here's a way to find the id based on the host IP:
for e,i in enumerate(hosts['response']):
    if i['hostIp'] == "207.1.10.20":
        print(hosts['response'][e])

# I did a couple things here; I enumerated the 'list' (he called it an array but it's actually a list)
# I stored the index that gets enumerated in 'e' and I stored the actual row of data in i
# I think check to see if the field hostIp has what I want then I return the entire row of data via its index ID

devices = {"response": [
    {
        "family": "Switches and Hubs",
        "type": "Cisco Catalyst 2960C-8PC-L Switch",
        "serialNumber": "FOC1637Y3FJ",
        "role": "CORE",
        "reachabilityStatus": "Reachable",
        "instanceUuid": "2dc30cac-072e-4d67-9720-cc302d02695a",
        "id": "2dc30cac-072e-4d67-9720-cc302d02695a"
    },
    {
        "family": "Unified AP",
        "type": "Cisco 3500I Unified Access Point",
        "serialNumber": "FGL1548S2YF",
        "role": "ACCESS",
        "reachabilityStatus": "Reachable",
        "instanceUuid": "17184480-2617-42c3-b267-4fade5f794a9",
        "id": "17184480-2617-42c3-b267-4fade5f794a9"
    }
],
    "version": "1.0"
}
