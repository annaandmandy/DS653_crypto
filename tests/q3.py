OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q3',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> def q3_public_tests(blockchain):\n'
                                               "...     secret_key = ECC.generate(curve='P-256', randfunc=lambda x: b'0' * x)\n"
                                               '...     public_keys = '
                                               "['044d4385fe08e0eb94c524bdd3682c9c5ae358f52402df02418d0ba6cf6889289a27bd56a666df7dc595c98da1f22958009ae17c52fd290185d2e2bf11140a0a5e', "
                                               "'04be4a2555cc8ed29989eeddde3d8e4d41458d02dce047aac2e6af2d58688c5beae7163eb157d1fd3c3d282abab7172b0f0d63274ebe721d31c5d72a83741df170', "
                                               "'04a3fc575afc4ad2ca2cbeed50b52fedf049d317b790aa33e7f8182aec028453082d4c4ffd4c99c7e6d11c134e81020c57ca0fbf0bf3406bf4457dc72d8c994a65', "
                                               "'04abc5bd2786ea5144122ccf43b89a557e1d36e2773c2b8986d9819a22c2e6540b3d5da692504ccc29fbf774435312afdda2a360d5160329cb326f6d47db29f50b', "
                                               "'046a921bed68e07e66f38a5137b3784372cfd4507e6451e1dfe3760f08649750e7891cd30339b730c0280738c60233d3c99eb78454340ff363cafbf1e6f0cfce5e']\n"
                                               '...     blockchain = [gen_block_0(), gen_block_1()]\n'
                                               '...     players_balance = [1, 0, 1, 0, 0]\n'
                                               "...     assert findBalance(blockchain, players_balance) == [1, 1, 0, 0, 0], 'Should return final balance [1, 1, 0, 0, 0] for the provided blockchain'\n"
                                               '...     players_balance = [1, 0, 1, 0, 0]\n'
                                               '...     invalid_blockchain = [gen_block_0(), gen_block_1()]\n'
                                               "...     invalid_blockchain[1].previous_hash = '2222222222222222222122222122222222222222222222222222222222222222'\n"
                                               '...     assert findBalance(invalid_blockchain, players_balance) == False, "Should return \'False\' for an invalid blockchain"\n'
                                               '>>> q3_public_tests(blockchain)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> def q3_hidden_test6():\n'
                                               "...     secret_key = ECC.generate(curve='P-256', randfunc=lambda x: '0'.encode('ascii') * x)\n"
                                               '...     public_keys = '
                                               "['044d4385fe08e0eb94c524bdd3682c9c5ae358f52402df02418d0ba6cf6889289a27bd56a666df7dc595c98da1f22958009ae17c52fd290185d2e2bf11140a0a5e', "
                                               "'04be4a2555cc8ed29989eeddde3d8e4d41458d02dce047aac2e6af2d58688c5beae7163eb157d1fd3c3d282abab7172b0f0d63274ebe721d31c5d72a83741df170', "
                                               "'04a3fc575afc4ad2ca2cbeed50b52fedf049d317b790aa33e7f8182aec028453082d4c4ffd4c99c7e6d11c134e81020c57ca0fbf0bf3406bf4457dc72d8c994a65', "
                                               "'04abc5bd2786ea5144122ccf43b89a557e1d36e2773c2b8986d9819a22c2e6540b3d5da692504ccc29fbf774435312afdda2a360d5160329cb326f6d47db29f50b', "
                                               "'046a921bed68e07e66f38a5137b3784372cfd4507e6451e1dfe3760f08649750e7891cd30339b730c0280738c60233d3c99eb78454340ff363cafbf1e6f0cfce5e']\n"
                                               '...     blockchain = [gen_block_0(), gen_block_1()]\n'
                                               '...     players_balance = [3, 3, 3, 3, 3]\n'
                                               '...     t1 = TransactionPayload(public_keys[4], public_keys[3], 1)\n'
                                               '...     t1_signature = '
                                               "'8440dced32858d9b4ec8780822e41b4daf29b8221bd59cb1811dcf11a866be42b726f7d5cf5ec9d848f66ef9b0d8790073306c37e8cc38d3db013e67c0541fee'\n"
                                               '...     t1_signed = Transaction(t1, t1_signature)\n'
                                               '...     t2 = TransactionPayload(public_keys[1], public_keys[0], 1)\n'
                                               '...     t2_signature = '
                                               "'63bf7685ef20d44489e7028fbc8756b04f8f56e124d4c2231f9eac0f08657558cb6737436c130693d6eda861b4228dc433d6d266182a00e265d0fe936620bc14'\n"
                                               '...     t2_signed = Transaction(t2, t2_signature)\n'
                                               "...     previous_hash = '0000000000000000000000000000000000000000000000000000000000000000'\n"
                                               '...     b1 = Block(0, [t1_signed, t2_signed], previous_hash, 668)\n'
                                               '...     t3 = TransactionPayload(public_keys[0], public_keys[2], 2)\n'
                                               '...     t3_signature = '
                                               "'c41bacc86d6ad9ba02a9d6bd6f1041545ccde2f9ef78a6a82a770e8d63b06f17523e4d51bdc1367e8a1c77d78ff5e91b3cdd8d529d6c9cb67edb230059c39897'\n"
                                               '...     t3_signed = Transaction(t3, t3_signature)\n'
                                               "...     previous_hash = '006f607314121303c805ac82b77cc0ad3706574fba76d415511c4015b2692f05'\n"
                                               '...     b2 = Block(1, [t3_signed], previous_hash, 202)\n'
                                               '...     blockchain_valid = [b1, b2]\n'
                                               '...     return findBalance(blockchain_valid, players_balance)\n'
                                               ">>> assert q3_hidden_test6() == [2, 2, 5, 4, 2], 'Should accept a valid blockchain and reach the correct final balance'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
