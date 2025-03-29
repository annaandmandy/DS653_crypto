OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q4',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw6_q4().to_bytes(1, 'big') + b'8a822fd9fb4cf3f0ebd50a183ba59f39').digest()) == "
                                               "b'4899fc0a12f0b7d2ecaf9ce2d17c921f0e30d7dee1dba18c8163b887a8eb65e0', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
