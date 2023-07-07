import prime.constants as constants
import prime.helper as helper

from prime.prime import Prime
from email.email import Email

def main():
    primes = Prime(start=constants.START_VAL, finish=constants.END_VAL)
    prettier_calculated_primes = primes.prettier()
    print(prettier_calculated_primes)

    new_mail = Email()
    new_mail.send()

if __name__ == '__main__':
    main()