#!/usr/bin/env python

from ephem_test import *

# Determine whether dates behave reasonably.

class date_suite(unittest.TestCase):
    def setUp(self):
        self.date = date('2004/09/04 00:17:15.8')

    def test_date_constructor(self):
        std = ('2004/09/04 00:17:15.8',)
        pairs = [std, ('2004.67489614324023472',),
                 std, ('2004/9/4.0119884259259257',),
                 std, ('2004/9/4 0.28772222222222221',),
                 std, ('2004/9/4 0:17.263333333333332',),
                 std, ('2004/9/4 0:17:15.8',),
                 ('2004',), ((2004,),),
                 ('2004/09',), ((2004, 9),),
                 std, ((2004, 9, 4.0119884259259257),),
                 std, ((2004, 9, 4, 0.28772222222222221),),
                 std, ((2004, 9, 4, 0, 17.263333333333332),),
                 std, ((2004, 9, 4, 0, 17, 15.8),),
                 ]
        for i in range(0, len(pairs), 2):
            args1, args2 = pairs[i:i+2]
            d1, d2 = date(*args1), date(*args2)
            self.assert_(-1e-15 < (d1 / d2 - 1) < 1e-15,
                         'dates not equal:\n %r = date%r\n %r = date%r'
                         % (d1.tuple(), args1, d2.tuple(), args2))

    def test_date_string_value(self):
        self.assertEqual(str(self.date), '2004/9/4 00:17:15')

    def test_date_triple_value(self):
        self.assertEqual(self.date.triple(), (2004, 9, 4.0119884259256651))

    def test_date_triple_value(self):
        self.assertEqual(self.date.tuple(),
                         (2004, 9, 4, 0, 17, 15.799999977461994))