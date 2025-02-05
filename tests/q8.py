OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q8',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> def test_hw2_q8():\n'
                                               '...     secret_key_q8 = q8_recover_sk_weak(public_key_q8, sig_3)\n'
                                               "...     sig_4 = sign(secret_key_q8, b'message_4', 1)\n"
                                               "...     sig_5 = sign(secret_key_q8, b'hello_world', 2)\n"
                                               "...     assert verify(public_key_q8, b'message_4', sig_4) == True\n"
                                               "...     assert verify(public_key_q8, b'hello_world', sig_5) == True\n"
                                               '...     return\n'
                                               '>>> test_hw2_q8()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
