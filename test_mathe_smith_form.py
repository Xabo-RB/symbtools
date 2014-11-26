# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 11:25:00 2014

@author: Carsten Knoll
"""

import unittest
import sympy as sp
from sympy import sin, cos
import symb_tools as st

from mathe_smith_form import solve_bezout_eq

from IPython import embed as IPS


class BezoutTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_regular1(self):
        s = sp.Symbol("s")

        w1 = (s+5)*(s+3)
        w2 = (s+1)*(s+2)*s
        c1 , c2 = solve_bezout_eq(w1, w2, s)
        r = sp.simplify(c1*w1+c2*w2)
        self.assertEquals(r, 1)

        w1 = 0
        w2 = (s+1)*(s+2)*s
        self.assertRaises(ValueError, solve_bezout_eq, w1, w2, s)

        w1 = s
        w2 = 7*s**5-13.4*s**4-4.7*s**3 + 9
        c1 , c2 = solve_bezout_eq(w1, w2, s)
        r = sp.simplify(c1*w1+c2*w2)
        # remove numerical noise in the coeffs
        r = st.clean_numbers(r)
        self.assertEquals(r, 1)

        w1 = 18.91
        w2 = 7*s**5-13.4*s**4-4.7*s**3 + 9
        c1 , c2 = solve_bezout_eq(w1, w2, s)
        r = sp.simplify(c1*w1+c2*w2)
        self.assertEquals(r, 1)

    def test_regular2(self):
        s = sp.Symbol("s")
        a, b, c = sp.symbols("a, b, c")

        w1 = (s+a)*(s+1)
        w2 = (s+b)*(s+2)
        w3 = (s+c)*(s+1)
        w4 = (s+a)*(s+3)
        w04 = a
        w05 = b

        c1 , c2 = solve_bezout_eq(w1, w2, s)
        r = sp.simplify(c1*w1+c2*w2)
        self.assertEquals(r, 1)

        self.assertRaises(ValueError, solve_bezout_eq, w1, w3, s)
        self.assertRaises(ValueError, solve_bezout_eq, w1, w4, s)
        self.assertRaises(ValueError, solve_bezout_eq, w1*0, w4*0, s)
        self.assertRaises(ValueError, solve_bezout_eq, w1, w4*0, s)

        c1 , c2 = solve_bezout_eq(w04, w05, s)
        r = sp.simplify(c1*w04+c2*w05)
        self.assertEquals(r, 1)

        c1 , c2 = solve_bezout_eq(w04*0, w05, s)
        r = sp.simplify(c1*w04+c2*w05)
        self.assertEquals(r, 1)

        c1 , c2 = solve_bezout_eq(w04, w05*0, s)
        r = sp.simplify(c1*w04+c2*w05)
        self.assertEquals(r, 1)

    def test_regular3(self):
        s = sp.Symbol("s")

        import random
        random.seed(0)

        for i in xrange(2):
            w1 = sp.random_poly(s, i, -10, 10)
            w2 = sp.random_poly(s, i+1, -10, 10)
            c1 , c2 = solve_bezout_eq(w1, w2, s)
            r = sp.simplify(c1*w1+c2*w2)
            self.assertEquals(r, 1)

    def test_regular4(self):
        s = sp.Symbol("s")
        a, b, c = sp.symbols("a, b, c")

        w1 = a+b*s**2
        w2 = c*s**2

        c1 , c2 = solve_bezout_eq(w1, w2, s)
        r = sp.simplify(c1*w1+c2*w2)
        self.assertEquals(r, 1)



def main():
    unittest.main()

if __name__ == '__main__':
    main()