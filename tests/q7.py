OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q7',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> from cryptos.keys import PublicKey\n'
                                               '>>> def test_hw2_q7():\n'
                                               '...     assert PublicKey.from_sk(q7_recover_sk_reuse(m_1, m_2)) == public_key_q7\n'
                                               "...     assert PublicKey.from_sk(q7_recover_sk_reuse(m_1, m_2)).address(net='test', compressed=False) == 'mmyNVmFJi73DEAginQFB6r7dLe4Jz5X67f'\n"
                                               "...     assert PublicKey.from_sk(q7_recover_sk_reuse(m_1, m_2)).address(net='test', compressed=True) == 'mpeX1woW86S6zkhP3YYjRXtDnWVQyNv2kW'\n"
                                               '...     return\n'
                                               '>>> test_hw2_q7()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
