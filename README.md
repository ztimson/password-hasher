# password_hasher
Python utility to hash passwords. Often when creating a user, a hashed password is needed. This cammond line utility can simply hash the password or multiple parameters can be passed to replicated. password, salt, hashing algorithm, pass+salt concatination order, and number of iterations can all be specified.

## help
```
Usage: password_hash.py [options] PASSWORD

Options:
  -h, --help            show this help message and exit
  -s SALT, --salt=SALT  specify salt
  -i ITERATIONS, --iterations=ITERATIONS
                        specify number of iterations to hash password
  -o ORDER, --order=ORDER
                        order the password and salt ex. "ps" to append salt
  --hash=HASH           hash algorithm to be used
  --hash-algorithms     display available hash algorithms and exit
```
