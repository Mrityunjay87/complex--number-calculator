# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:36:01 2020

@author: Mrityunjay1.Pandey
"""

class complex_numbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
            
    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    
    def __add__(self, other): 
         r=self.real + other.real
         i=self.imag + other.imag 
         return complex_numbers(r,i)

    def __sub__(self, other): 
         r=self.real - other.real
         i=self.imag - other.imag 
         return complex_numbers(r,i)
     
    def __mul__(self,other):
        if self.imag!=0:
            r=(self.real*other.real)-(self.imag*other.imag)
            i=(self.imag*other.real)+(self.real*other.imag)
        else:
            r=(self.real*other.real)
            i=(self.imag*other.real)
        return complex_numbers(r,i)
    
    def __truediv__(self,other):
        r=((self.real*other.real)+(self.imag*other.imag))/((other.real**2)+(other.imag**2))
        i=((self.imag*other.real)-(self.real*other.imag))/((other.real**2)+(other.imag**2))
        return complex_numbers(r,i)
        
        
    def absolute(self):
        absolute=(self.real**2+self.imag**2)**(1/2)
        return absolute
    
    def argument(self):
        import numpy as np
        import math
        arg=math.degrees(np.arctan2(self.imag,self.real))
        return arg
    
    def conjugate(self):
        conj_r=self.real
        conj_i=self.imag*-1
        return complex_numbers(conj_r,conj_i)
    
    
comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)

comp_sum=complex_numbers.__add__(comp_1,comp_2)
comp_diff=complex_numbers.__sub__(comp_1,comp_2)
comp_prod=complex_numbers.__mul__(comp_1,comp_2)
comp_quot=complex_numbers.__truediv__(comp_1,comp_2)
comp_abs=complex_numbers.absolute(comp_1)
comp_conj=complex_numbers.conjugate(comp_1)
comp_arg=complex_numbers.argument(comp_1)
print("Complex numbers provided were {} & {}.\n \n==Below are the results of operation==\nAdditon is::{}\nDifference is::{}\nMultiplication is::{}\nDivison is::{}\nAbsolute Value is::{}\nConjugate Value is::{}\nArgument Value is::{}".format(comp_1,comp_2,comp_sum,comp_diff,comp_prod,comp_quot,comp_abs,comp_conj,comp_arg))      
