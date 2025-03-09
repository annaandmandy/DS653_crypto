OK_FORMAT = True

test = {   'all_or_nothing': True,
    'name': 'q4',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> def q4_tests():\n'
                                               '...     leader_zero = [Value.Zero, Value.One, Value.One, Value.One]\n'
                                               '...     leader_one = [Value.One, Value.Zero, Value.Zero, Value.Zero]\n'
                                               '...     for input in [leader_zero, leader_one]:\n'
                                               '...         for _ in range(10000):\n'
                                               '...             phaseking = SynchronousNetwork(PhaseKingParty, 1, 4, input, debug=False)\n'
                                               '...             result = phaseking.run(6)\n'
                                               '...             if phaseking.parties[0].is_faulty == False:\n'
                                               '...                 expected_output = input[0]\n'
                                               '...             else:\n'
                                               '...                 expected_output = result[1]\n'
                                               '...             for i in range(4):\n'
                                               '...                 if phaseking.parties[i].is_faulty == False:\n'
                                               "...                     assert result[i] == expected_output, 'incorrect implementation of phase-king'\n"
                                               '...     return\n'
                                               '>>> q4_tests()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
