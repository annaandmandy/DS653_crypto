OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw6_q1().to_bytes(1, 'big') + b'f2f3a0aad1b5b2a2e38fd5213f8b9a0d').digest()) == "
                                               "b'e9a0fcdedced4f6963b784ff2cdb42d9802e33e31e91c49d8ddb08d640828bfc', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
