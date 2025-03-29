OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw6_q2().to_bytes(1, 'big') + b'7347546f1bf1c2a5f24951b42a5d7c50').digest()) == "
                                               "b'90c3509fc36f606b625c2b5123ccf20bf9f81b80a182067d670dd0531d2b28d4', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
