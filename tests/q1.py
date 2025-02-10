OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q1',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> def q1_public_tests():\n'
                                               '...     tx = Transaction(TransactionPayload(public_keys[0], public_keys[1], 1), '
                                               "'edd6bb60e8486f9747f911a6d7340c275d5a417c3823952715a18a64d3577325413cf544e8f48e6c30a312649200c57b72d7eaa4721abf376dbd0dc799db6c3a')\n"
                                               "...     assert isValidTransaction(tx) == True, 'Should accept a valid transaction'\n"
                                               '...     tx.signature = '
                                               "'00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'\n"
                                               "...     assert isValidTransaction(tx) == False, 'Should reject an invalid signature'\n"
                                               '...     tx = Transaction(TransactionPayload(public_keys[2], public_keys[3], 1), '
                                               "'33bcaaa920207125ec72ea7f9e5fbddb993479dbe7122c6dfcf0a96f2e646dd90ff73c90c784f473480e32fd2fb68735af86458bc0434e5958f025cc9e0ddd59')\n"
                                               "...     assert isValidTransaction(tx) == True, 'Should accept a valid transaction'\n"
                                               "...     tx.signature = '2222222222222222222222222222222222222222222222222222222222222222'\n"
                                               "...     assert isValidTransaction(tx) == False, 'Should reject a signature that is invalid and of the incorrect length'\n"
                                               '>>> q1_public_tests()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
