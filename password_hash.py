"""
Author: Zakary Timson
Date: 2015-05-06
Description: Hashes passwords
"""

# Imports
import hashlib
from optparse import OptionParser
from random import choice, randrange
from string import digits, ascii_letters
from sys import argv


def salt_gen(size=64, chars=ascii_letters + digits):
    """
    Generate random char sequence
    :param size: length of sequence (Default of 64)
    :param chars: characters to use in sequence (Defaults to letters and numbers)
    :return: returns string of of random characters
    """
    return ''.join(choice(chars) for _ in range(size))


def salt_format(password, salt, order):
    """
    Concatenates the password and salt together based on a specified order. s's will be replaced with the salt and p's
    will be replaced with the password. Ex. "sps" will concat salt + pass + salt
    :param password: password to be concatenated
    :param salt: salt to be concatenated
    :param order: order the password and salt should be concatenated.
    :return: the concatenated password
    """
    return order.replace("p", "{0}").replace("s", "{1}").format(password, salt)


def hash_pass(password, salt, iterations, hash_algorithm, order):
    """
    Hash password and salt together a specified amount of times
    :param password: password to hash
    :param salt: salt to hash with password
    :param iterations: number of times to hash together (Default is a random amount between 5000 and 10000)
    :param hash_algorithm: hashing algorithm to use
    :param order: order that the password and salt are concatenated
    :return: new hashed password
    """
    hash_algorithm = getattr(hashlib, hash_algorithm)
    for i in range(iterations):
        password = hash_algorithm(salt_format(password, salt, order).encode()).hexdigest()
    return password


def available_hashes():
    """
    Display available hash algorithms
    :return: None
    """
    print("Available hash algorithms:\n", "\n".join(hashlib.algorithms_available))
    exit(0)


def output(password, salt, iterations, hash_algorithm):
    """
    Output generated data to standard output
    :param password: hashed password
    :param salt: salt used in hash
    :param iterations: iterations made on password
    :param hash_algorithm: hashing algorithm to use
    :return: None
    """
    print("Password: %s\nSalt: %s\nIterations: %d\nHash: %s" % (password, salt, iterations, hash_algorithm))


# Specify flags
parser = OptionParser(usage="usage: %prog [options] PASSWORD")
parser.add_option("-s", "--salt", help="specify salt")
parser.add_option("-i", "--iterations", help="specify number of iterations to hash password")
parser.add_option("-o", "--order", help="order the password and salt ex. \"ps\" to append salt")
parser.add_option("--hash", help="hash algorithm to be used")
parser.add_option("--hash-algorithms", help="display available hash algorithms and exit", action="callback",
                  callback=available_hashes)
(flags, opts) = parser.parse_args()

# set arguments
password = argv[len(argv) - 1]
salt = salt_gen()
if flags.salt is not None:
    salt = flags.salt
iterations = randrange(5000, 10000)
if flags.iterations is not None:
    iterations = flags.iterations
hash_algorithm = "sha1"
if flags.hash is not None:
    hash_algorithm = flags.hash
order = "ps"
if flags.order is not None:
    order = flags.order

# Output newly generated password and relevant data
output(hash_pass(password, salt, iterations, hash_algorithm, order), salt, iterations, hash_algorithm)
exit(0)
