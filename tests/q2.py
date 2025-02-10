OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q2',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> def q2_public_tests():\n'
                                               "...     secret_key = ECC.generate(curve='P-256', randfunc=lambda x: b'0' * x)\n"
                                               '...     public_keys = '
                                               "['044d4385fe08e0eb94c524bdd3682c9c5ae358f52402df02418d0ba6cf6889289a27bd56a666df7dc595c98da1f22958009ae17c52fd290185d2e2bf11140a0a5e', "
                                               "'04be4a2555cc8ed29989eeddde3d8e4d41458d02dce047aac2e6af2d58688c5beae7163eb157d1fd3c3d282abab7172b0f0d63274ebe721d31c5d72a83741df170', "
                                               "'04a3fc575afc4ad2ca2cbeed50b52fedf049d317b790aa33e7f8182aec028453082d4c4ffd4c99c7e6d11c134e81020c57ca0fbf0bf3406bf4457dc72d8c994a65', "
                                               "'04abc5bd2786ea5144122ccf43b89a557e1d36e2773c2b8986d9819a22c2e6540b3d5da692504ccc29fbf774435312afdda2a360d5160329cb326f6d47db29f50b', "
                                               "'046a921bed68e07e66f38a5137b3784372cfd4507e6451e1dfe3760f08649750e7891cd30339b730c0280738c60233d3c99eb78454340ff363cafbf1e6f0cfce5e']\n"
                                               '...     blockchain = [gen_block_0(), gen_block_1()]\n'
                                               '...     for block in blockchain:\n'
                                               "...         assert verifyBlock(block) == True, 'Should accept a valid block in the provided blockchain'\n"
                                               '...     tx_in_valid_block = Transaction(TransactionPayload(public_keys[0], public_keys[1], 1), '
                                               "'edd6bb60e8486f9747f911a6d7340c275d5a417c3823952715a18a64d3577325413cf544e8f48e6c30a312649200c57b72d7eaa4721abf376dbd0dc799db6c3a')\n"
                                               "...     hash_in_valid_block = '0000000000000000000000000000000000000000000000000000000000000000'\n"
                                               '...     nonce_in_valid_block = 316\n'
                                               '...     valid_block = Block(0, [tx_in_valid_block], hash_in_valid_block, nonce_in_valid_block)\n'
                                               "...     assert verifyBlock(valid_block) == True, 'Should accept a valid block'\n"
                                               '...     tp_in_invalid_block_one = TransactionPayload(public_keys[2], public_keys[4], 3)\n'
                                               '...     sig_in_invalid_block_one = '
                                               "'69d1d28a8b757d038e4bb767cbf69179b2d41081f43c31736667976e106d94ac379e5c4aac2541d5b78eb064d58c42df759148889e31514b23479ed1b7ff9a10'\n"
                                               '...     tx_in_invalid_block_one = Transaction(tp_in_invalid_block_one, sig_in_invalid_block_one)\n'
                                               "...     hash_in_invalid_block_one = '00ada715cd964e14b36d5d18369640d384f64024406171b0937d2521ccc1c1d9'\n"
                                               '...     nonce_in_invalid_block_one = 327\n'
                                               '...     invalid_block_one = Block(2, [tx_in_invalid_block_one], hash_in_invalid_block_one, nonce_in_invalid_block_one)\n'
                                               "...     assert verifyBlock(invalid_block_one) == False, 'Should reject an invalid block'\n"
                                               '...     tx_in_invalid_block_two = Transaction(TransactionPayload(public_keys[0], public_keys[1], 1), '
                                               "'00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')\n"
                                               "...     hash_in_invalid_block_two = '0000000000000000000000000000000000000000000000000000000000000000'\n"
                                               '...     nonce_in_invalid_block_two = 226\n'
                                               '...     invalid_block_two = Block(0, [tx_in_invalid_block_two], hash_in_invalid_block_two, nonce_in_invalid_block_two)\n'
                                               "...     assert verifyBlock(invalid_block_two) == False, 'Should reject an invalid block'\n"
                                               '>>> q2_public_tests()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
