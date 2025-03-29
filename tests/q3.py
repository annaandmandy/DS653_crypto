OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw6_q3().to_bytes(1, 'big') + b'36405025172ab66aa708f469d2735813').digest()) == "
                                               "b'14aeaed0ecb8a7030bd6f2be9ee8a77473890f4cd8f917848091810652a534c8', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
