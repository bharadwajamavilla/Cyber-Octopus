import requests

target_url = input("[*] Enter URL: ")
file_name = input("[*] Enter the file containing Directories: ")


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


file = open(file_name, "r")
for line in file:
    directory = line.strip()
    full_url = target_url + "/" + directory
    response = request(full_url)
    if response:
        print("[*] Discovred directory at this path: " + full_url)

