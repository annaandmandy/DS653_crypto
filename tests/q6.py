OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q6',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw6_q6().to_bytes(1, 'big') + b'7d45b9e2ceba761bdfa72e727bf53007').digest()) == "
                                               "b'c32b31864ec9dcb8535561402415d238d4c7b8c3b93a731e0b9022ba2c61f669', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
