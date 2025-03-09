OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q3',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> def q3_validity():\n'
                                               '...     consistent_zeros_four_parties = [Value.Zero, Value.Zero, Value.Zero, Value.Zero]\n'
                                               '...     consistent_ones_four_parties = [Value.One, Value.One, Value.One, Value.One]\n'
                                               '...     for input in [consistent_zeros_four_parties, consistent_ones_four_parties]:\n'
                                               '...         for _ in range(5000):\n'
                                               '...             gradecastNetwork = SynchronousNetwork(GradecastParty, 1, 4, input, debug=False)\n'
                                               '...             result = gradecastNetwork.run(2)\n'
                                               '...             for i in range(4):\n'
                                               '...                 if gradecastNetwork.parties[i].is_faulty == False:\n'
                                               '...                     assert result[i] == (input[0], 2)\n'
                                               '...     consistent_zeros_seven_parties = [Value.Zero, Value.Zero, Value.Zero, Value.Zero, Value.Zero, Value.Zero, Value.Zero]\n'
                                               '...     consistent_ones_seven_parties = [Value.One, Value.One, Value.One, Value.One, Value.One, Value.One, Value.One]\n'
                                               '...     for input in [consistent_zeros_seven_parties, consistent_ones_seven_parties]:\n'
                                               '...         for _ in range(5000):\n'
                                               '...             gradecastNetwork = SynchronousNetwork(GradecastParty, 2, 7, input, debug=False)\n'
                                               '...             result = gradecastNetwork.run(2)\n'
                                               '...             for i in range(7):\n'
                                               '...                 if gradecastNetwork.parties[i].is_faulty == False:\n'
                                               "...                     assert result[i] == (input[0], 2), 'failed validity test'\n"
                                               '...     return\n'
                                               '>>> q3_validity()\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> def q3_knowledge_of_agreement():\n'
                                               '...     consistent_zeros = [Value.Zero, Value.Zero, Value.Zero, Value.Zero]\n'
                                               '...     skewed_zeros = [Value.Zero, Value.Zero, Value.Zero, Value.One]\n'
                                               '...     balanced_inputs = [Value.Zero, Value.Zero, Value.One, Value.One]\n'
                                               '...     skewed_ones = [Value.Zero, Value.One, Value.One, Value.One]\n'
                                               '...     consistent_ones = [Value.One, Value.One, Value.One, Value.One]\n'
                                               '...     for input in [consistent_zeros, skewed_zeros, balanced_inputs, skewed_ones, consistent_ones]:\n'
                                               '...         for _ in range(10000):\n'
                                               '...             gradecastNetwork = SynchronousNetwork(GradecastParty, 1, 4, input, debug=False)\n'
                                               '...             result = gradecastNetwork.run(2)\n'
                                               '...             for val in [Value.Zero, Value.One]:\n'
                                               '...                 if (val, 2) in result:\n'
                                               '...                     for i in range(4):\n'
                                               '...                         if gradecastNetwork.parties[i].is_faulty == False:\n'
                                               "...                             assert result[i][0] == val and result[i][1] >= 1, 'failed knowledge of agreement test'\n"
                                               '...     return\n'
                                               '>>> q3_knowledge_of_agreement()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
