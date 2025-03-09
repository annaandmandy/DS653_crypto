OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q1',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw5_q1().to_bytes(1, 'big') + b'9d77ce12cbefa73cb00b01b98b7530bb').digest()) == "
                                               "b'46df609ab6035fa6b92af7c7bbe796d3dc28c0ed4e3203470a54048fd71b8f10', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
