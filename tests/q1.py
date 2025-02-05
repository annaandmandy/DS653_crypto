OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw2_q1().to_bytes(1, 'big') + b'5d7a504fb283632efeed2d5c56ef6015').digest()) == "
                                               "b'49cf57774e3dd060aadad260750b3b88ded31c8199855ed311ff3bfd00ab0ee9', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
