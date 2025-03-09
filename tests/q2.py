OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q2',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw5_q2().to_bytes(1, 'big') + b'1ef4c6e59faa8152bfbef9d5a56413e9').digest()) == "
                                               "b'a4de92d1a1d26beb20656d868b7f0509cec43ae2d800d02914a369204eab1e13', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
