import hashlib
from urllib.request import urlopen
print("Password Cracker")


def read_word_list(url):
    try:
        wordListFile = urlopen(url).read()
    except Exception as e:
        print("There is some error while reading the Word list", e)
        exit()
    return wordListFile


def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()


def bruteforce(guess_password_list, actual_password_hash):
    for guess_password in guess_password_list:
        if hash(guess_password) == actual_password_hash:
            print("Your password is : ", guess_password)
            print("Please change your password it was easy to guess ;)")
            exit()


url = "https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt"
actual_password = "john"
actual_password_hash = hash(actual_password)

wordlist = read_word_list(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')

bruteforce(guess_password_list, actual_password_hash)
