#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *
class TriangleError(Exception):
    pass
        

       
def triangle(s1,s2,s3):
    if s1 <=0 or s2 <= 0 or s3 <=0 :
        raise TriangleError("side should be greater then 0")
    if (s1+s2 > s3) or (s2+s3 > s1) or (s3+s1 >s2):
        raise TriangleError("sum of any two sides should be greater than the third one")
        
    pass

     

class AboutTriangleProject2(Koan):
    # The first assignment did not talk about how to handle errors. 
    # Let's handle that part now.
    

    def test_illegal_triangles_throw_exceptions(self):
        # All sides should be greater than 0
        with self.assertRaises(TriangleError):
            triangle(0, 0, 0)
        with self.assertRaises(TriangleError):
            triangle(3, 4, -5)

        # The sum of any two sides should be greater than the third one
        with self.assertRaises(TriangleError):
            triangle(1, 1, 3)
        with self.assertRaises(TriangleError):
            triangle(2, 5, 2)


