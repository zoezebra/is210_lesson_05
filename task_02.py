#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal


# Your functions should not need or take string representations of these values
PSTR = raw_input('What is the amount of your principal?: ')
TSTR = raw_input('For how many years is this loan being borrowed?: ')
QSTR = raw_input('Are you prequalified for this loan?: ')

# Function arguments should not need the following three transformations
P = int(PSTR)
T = int(TSTR)
Q = True if QSTR.lower()[0] == 'y' else False

N = 12
R = None
TOTAL = None

if P >= 0 and P <= 199999:
    if T >= 1 and T <= 15:
        if Q:
            R = "0.0363"
        else:
            R = "0.0465"
    elif T >= 16 and T <= 20:
        if Q:
            R = "0.0404"
        else:
            R = "0.0498"
    elif T >= 21 and T <= 30:
        if Q:
            R = "0.0577"
        else:
            R = "0.0639"
elif P >= 200000 and P <= 999999:
    if T >= 1 and T <= 15:
        if Q:
            R = "0.0302"
        else:
            R = "0.0398"
    elif T >= 16 and T <= 20:
        if Q:
            R = "0.0327"
        else:
            R = "0.0408"
    elif T >= 21 and T <= 30:
        if Q:
            R = "0.0466"
elif P >= 1000000:
    if T >= 1 and T <= 15:
        if Q:
            R = "0.0205"
    elif T >= 16 and T <= 20:
        if Q:
            R = "0.0262"

if R is not None:
    R = decimal.Decimal(R)
    TOTAL = P * ((1 + R/N) ** (N * T))
    TOTAL = int(round(TOTAL))
