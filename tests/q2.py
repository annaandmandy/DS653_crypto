OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw2_q2().to_bytes(1, 'big') + b'4e45d6c17751c168bc833d203cbe10da').digest()) == "
                                               "b'6bc32f928b1d45d8ba797bb9a6e4057b1e7a2dd9e0e9f72f0f9a329bc23e2497', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
