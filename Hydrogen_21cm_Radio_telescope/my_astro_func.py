#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.constants as const
import scipy as sci

def rayleigh_crit_degrees(wav,D):
    """This function calculates the rayleigh criterion of a telescope.
    INPUT: wavelength [meters] and aperture diameter [meters]
    OUTPUT:Rayleigh Criterion in degrees [degrees]."""
    
    r_c_radians = (1.22*wav)/D 
    
    r_c_degrees = r_c_radians *(180/np.pi) #converts rayleigh criterion in degrees
    
    return r_c_degrees




def my_data_mod(x_data,y_data,int_of_power): 
    
    """This function returns a polynomial fit data to a model.
    INPUT: The inputs are the axes data, and the polynomial dimension.
    OUTPUT: The output is the polynomial model."""

    polynomial_coefficients = np.polyfit(x_data,y_data,int_of_power)
    polynomial_fit = np.poly1d(polynomial_coefficients)
    data_model = np.polyval(polynomial_fit,x_data)
    
    return data_model

def my_data_mod_eq(x_data,y_data,int_of_power): 
    """This function returns a polynomial fit equation to a model.
    INPUT: The inputs are the axes data, and the polynomial dimension.
    OUTPUT: The output is the polynomial model equation."""
    
    polynomial_coefficients = np.polyfit(x_data,y_data,int_of_power)
    polynomial_fit = np.poly1d(polynomial_coefficients)
    return polynomial_fit

def my_data_mod_coeff(x_data,y_data,int_of_power):
    polynomial_coefficients = np.polyfit(x_data,y_data,int_of_power)
    return polynomial_coefficients

