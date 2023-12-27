import requests

import hashlib

import sys


import random

#hashing- encrpting
#k- anonymity
# first 5 characters

# hash function: Is a function that generates a fixed length
# Its one way Algorithm


def RandomPasswd_generator(length):
    res = ""
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    numbers = '0123456789'
    symbols = "~!@#$%^&*,.:;/\|+"

    password = lower + upper + numbers + symbols

    return "".join(random.sample(password, length))


def request_api_data(query_char): #first 5 chars 

    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching :{res.status_code} ,check the api and try again')

    return res


def get_password_leaks_counts(hashes, hash_to_check): #response object , tail chars 
    print(hashes.text)

    hashes = (line.split(':') for line in hashes.text.splitlines())

    # print(hashes)

    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    '''

    check the password if it exits in API response

    '''
    
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # print(sha1_password)
    # print(sha1_password.hexdigest().upper())

    # print("Your Hashpassword is",sha1_password)

    first_5_char, tail = sha1_password[:5], sha1_password[5:]
    # return the hacked list of tailed hash
    # print("First 5 characters",first_5_char)
    # print("after 5 characters",tail)
    
    response = request_api_data(first_5_char) #passing the only header (5 chars)

    # print("Your Response from the API",response)

    return get_password_leaks_counts(response, tail)


# request_api_data('123')

# print(pwned_api_check('aNee18'))


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password } was found {count} times ... you should change it')
        else:
            print(f'{password} not found ! carry on .')
# main('anee18')


def args_test():

    while True:

        print("---- RANDOM PASSWD GENERATOR & HAVE I BEEN CHECKER -----")

        print("        1.Have i Been Pwned checker")

        print("        2.Random Password Generator")

        print("        3. exit")

        ch = int(input("What Would you like to Check :) : "))

        if ch == 1:
            a = input("Enter the password : ").split() #using split on str it will convert to list 
            main(a)
        elif ch == 2:
            b = int(input("Enter the Length : "))
            print(RandomPasswd_generator(b))

        elif ch == 3:
            break
        else:
            print("choose the right one.")
        
        print()
        


args_test()


# import hashlib

# s="aNee18"
# print(s.encode())
# print(hashlib.sha1(s.encode()).hexdigest())
# # E69EFCA75AD27C4818F36F821AA347F89C236614
