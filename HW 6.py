# -------------------------------------------------------------
# ---- HW 6 ---------------------------------------------------
# -------------------------------------------------------------

import sympy as sp
import fractions

# ---- Q1 -----------------------------------------------------

# define the variables for computing the limiting distribution

pi0 = sp.Symbol('pi0')
pi1 = sp.Symbol('pi1')

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq(0.4*pi0 + 0.2*pi1 - pi0),
        sp.Eq(0.6*pi0 + 0.8*pi1 - pi1),
        sp.Eq(pi0 + pi1 - 1)]

# define the variables that we are solving for

varlist = [pi0, pi1]

# solve the system of two equations

sol = sp.solve(eqns, varlist)
sol

# sol has long decimal values so lets see if there's a fractional representation 

for i in sol:
    print(i, fractions.Fraction(float(sol[i])).limit_denominator())

# ---- Q5 -----------------------------------------------------

# define the variables for computing the limiting distribution

pi0 = sp.Symbol('pi0')
pi1 = sp.Symbol('pi1')
pi2 = sp.Symbol('pi2')
pi3 = sp.Symbol('pi3')
pi4 = sp.Symbol('pi4')

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq((1/2)*pi0 + (1/3)*pi1 + (1/4)*pi2 + (1/5)*pi3 - pi0),
        sp.Eq((1/2)*pi0 + (1/3)*pi1 + (1/4)*pi2 + (1/5)*pi3 - pi1),
        sp.Eq((1/3)*pi1 + (1/4)*pi2 + (1/5)*pi3 - pi2),
        sp.Eq((1/4)*pi2 + (1/5)*pi3 - pi3),
        sp.Eq((1/5)*pi3 - pi4),
        sp.Eq(pi0 + pi1 + pi2 + pi3 + pi4 - 1)]

# define the variables that we are solving for

varlist = [pi0, pi1, pi2, pi3, pi4]

# solve the system of two equations

sol = sp.solve(eqns, varlist)
sol

# sol has long decimal values so lets see if there's a fractional representation 

for i in sol:
    print(i, fractions.Fraction(float(sol[i])).limit_denominator())



