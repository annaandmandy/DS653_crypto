OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> def q5_test():\n'
                                               "...     secret_key = ECC.generate(curve='P-256', randfunc=lambda x: b'0' * x)\n"
                                               '...     public_keys = '
                                               "['044d4385fe08e0eb94c524bdd3682c9c5ae358f52402df02418d0ba6cf6889289a27bd56a666df7dc595c98da1f22958009ae17c52fd290185d2e2bf11140a0a5e', "
                                               "'04be4a2555cc8ed29989eeddde3d8e4d41458d02dce047aac2e6af2d58688c5beae7163eb157d1fd3c3d282abab7172b0f0d63274ebe721d31c5d72a83741df170', "
                                               "'04a3fc575afc4ad2ca2cbeed50b52fedf049d317b790aa33e7f8182aec028453082d4c4ffd4c99c7e6d11c134e81020c57ca0fbf0bf3406bf4457dc72d8c994a65', "
                                               "'04abc5bd2786ea5144122ccf43b89a557e1d36e2773c2b8986d9819a22c2e6540b3d5da692504ccc29fbf774435312afdda2a360d5160329cb326f6d47db29f50b', "
                                               "'046a921bed68e07e66f38a5137b3784372cfd4507e6451e1dfe3760f08649750e7891cd30339b730c0280738c60233d3c99eb78454340ff363cafbf1e6f0cfce5e']\n"
                                               '...     blockchain = [gen_block_0(), gen_block_1()]\n'
                                               '...     players_balance = [1, 0, 1, 0, 0]\n'
                                               '...     dishonest_blockchain = generate_dishonest_blockchain()\n'
                                               "...     assert len(dishonest_blockchain) >= 3, 'Dishonest blockchain should contain at least 3 blocks'\n"
                                               '...     for block in dishonest_blockchain:\n'
                                               "...         assert verifyBlock(block) == True, 'Blocks in the dishonest blockchain should be valid'\n"
                                               '...     is_A_to_E_two_coins = False\n'
                                               '...     for (index, block) in enumerate(dishonest_blockchain):\n'
                                               '...         for trans in block.transactions:\n'
                                               '...             payload = trans.transaction_payload\n'
                                               '...             assert not (index == 0 and payload.sender_public_key == public_keys[0] and (payload.receiver_public_key == public_keys[1]) and '
                                               "(payload.amount == 1)), 'Must remove the A->B transaction from the first block'\n"
                                               '...             if payload.sender_public_key == public_keys[0] and payload.receiver_public_key == public_keys[4] and (payload.amount == 2):\n'
                                               '...                 is_A_to_E_two_coins = True\n'
                                               "...     assert is_A_to_E_two_coins == True, 'Must create an A->E transaction that pays 2 coins'\n"
                                               '>>> q5_test()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
