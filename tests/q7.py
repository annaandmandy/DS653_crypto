OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q7',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> import random\n'
                                               '>>> from os import urandom\n'
                                               '>>> from Cryptodome.Util.strxor import strxor\n'
                                               '>>> def q7_tests():\n'
                                               "...     common_words = [b'all', b'and', b'any', b'but', b'can', b'day', b'for', b'get', b'her', b'him', b'his', b'how', b'its', b'new', b'not', "
                                               "b'now', b'one', b'our', b'out', b'say', b'see', b'she', b'the', b'two', b'use', b'way', b'who', b'you']\n"
                                               '...     def OTP_encrypt(pt, key):\n'
                                               '...         assert len(pt) == 3\n'
                                               '...         assert len(key) == 3\n'
                                               '...         assert type(pt) == bytes\n'
                                               '...         assert type(key) == bytes\n'
                                               '...         return strxor(pt, key)\n'
                                               '...     for _ in range(2000):\n'
                                               '...         [pt1, pt2] = random.sample(common_words, 2)\n'
                                               '...         key = urandom(3)\n'
                                               '...         ct1 = OTP_encrypt(pt1, key)\n'
                                               '...         ct2 = OTP_encrypt(pt2, key)\n'
                                               "...         assert {pt1, pt2} == q7_two_time_pad_attack(ct1, ct2), 'did not find the correct plaintexts'\n"
                                               '>>> q7_tests()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
