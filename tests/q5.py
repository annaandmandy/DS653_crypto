OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw2_q5().to_bytes(1, 'big') + b'6e12018d726a6d4a19f910eb0054923b').digest()) == "
                                               "b'f4ee37b1012e0888aeab4585f2ee00a48d550302210bc4f735a5d84c025d0233', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
