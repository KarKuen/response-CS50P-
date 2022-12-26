import validator_collection
import validators

def main():
    email = input("What's your email address? ")
    print(response(email))

def response(email):
    if validators.email(email) == True:
        return('Valid')
    else:
        return('Invalid')


if __name__ == '__main__':
    main()