OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> from os import urandom\n'
                                               '>>> from binascii import hexlify\n'
                                               '>>> from hashlib import sha256\n'
                                               ">>> assert hexlify(sha256(hw2_q3().to_bytes(1, 'big') + b'cf2ce0ad91027197eab2403951c2d081').digest()) == "
                                               "b'5ec1ea9692764a68d1fcb7e6a0a759dd27bdf14fad32ee5df5cd2c07ada08e13', 'incorrect response, try again'\n",
                                       'failure_message': 'Try again',
                                       'hidden': False,
                                       'locked': False,
                                       'success_message': 'Satisfactory'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
