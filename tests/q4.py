OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q4',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw2_q4().to_bytes(1, 'big') + b'e635e6e3dc41cca00bee133e132d04bb').digest()) == "
                                               "b'fa4dceb6c19c64ba2f53a2e900386ebc6ac767e0488413e4411bcecd728b45a3', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
