<!-- Header -->
<div id="top" align="center">
  <br />

  <!-- Logo -->
  <img src="https://git.zakscode.com/repo-avatars/941ba5e37b669fb4ca722ec226b10b9206c2d65006641d0dd77d6a122ee64aff" alt="Logo" width="200" height="200">

  <!-- Title -->
  ### Password Hasher

  <!-- Description -->
  Python Password Hasher

  <!-- Repo badges -->
  [![Version](https://img.shields.io/badge/dynamic/json.svg?label=Version&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/password-hasher/tags&query=$[0].name)](https://git.zakscode.com/ztimson/password-hasher/tags)
  [![Pull Requests](https://img.shields.io/badge/dynamic/json.svg?label=Pull%20Requests&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/password-hasher&query=open_pr_counter)](https://git.zakscode.com/ztimson/password-hasher/pulls)
  [![Issues](https://img.shields.io/badge/dynamic/json.svg?label=Issues&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/password-hasher&query=open_issues_count)](https://git.zakscode.com/ztimson/password-hasher/issues)

  <!-- Links -->

  ---
  <div>
    <a href="https://git.zakscode.com/ztimson/password-hasher/releases" target="_blank">Release Notes</a>
    • <a href="https://git.zakscode.com/ztimson/password-hasher/issues/new?template=.github%2fissue_template%2fbug.md" target="_blank">Report a Bug</a>
    • <a href="https://git.zakscode.com/ztimson/password-hasher/issues/new?template=.github%2fissue_template%2fenhancement.md" target="_blank">Request a Feature</a>
  </div>

  ---
</div>

## Table of Contents
- [Password Hasher](#top)
    - [About](#about)
        - [Built With](#built-with)
    - [Setup](#setup)
        - [Production](#production)
    - [License](#license)

## About

Python utility to hash passwords. Often when creating a user, a hashed password is needed. This cammond line utility can simply hash the password or multiple parameters can be passed to replicated. password, salt, hashing algorithm, pass+salt concatination order, and number of iterations can all be specified.

```
Usage: password_hash.py [OPTIONS] <PASSWORD>

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


### Built With
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python)](https://www.python.org/)

## Setup

<details>
<summary>
  <h3 id="production" style="display: inline">
    Production
  </h3>
</summary>

#### Prerequisites
- [Python](https://www.python.org/downloads/)

#### Instructions
1. Download script: `curl https://git.zakscode.com/ztimson/password-hasher/raw/branch/master/password_hash.py`
2. Run python script: `python3 password_hasher.py [OPTIONS] <PASSWORD>`

</details>

## License
Copyright © 2007 Zakary Timson | Available under the GNU General Public License

See the [license](./LICENSE) for more information.
