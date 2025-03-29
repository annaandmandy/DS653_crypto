OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q5',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw6_q5().to_bytes(1, 'big') + b'59d1d350beb5f7df006367280f335ffd').digest()) == "
                                               "b'd2d9a00119112afb6792bb41faebc81d520782bf7184acf074909a4813ce6969', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
