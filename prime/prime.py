from prime.helper import *

class Prime:

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def calculate_primes(self):
        primes = []
        for i in range(self.start, self.finish):
            if is_prime(i):
                primes.append(i)
        return primes
    
    def prettier(self):
        body = ''
        for result in self.calculate_primes():
            body += f"This is a prime number {result} \n"
        return body