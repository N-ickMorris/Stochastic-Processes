# -------------------------------------------------------------
# ---- HW 5 ---------------------------------------------------
# -------------------------------------------------------------

import sympy as sp
import fractions

# ---- Q1 -----------------------------------------------------

# define the variables for computing the limiting distribution

pi0 = sp.Symbol('pi0')
pi1 = sp.Symbol('pi1')
pi2 = sp.Symbol('pi2')
pi3 = sp.Symbol('pi3')

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq(0.7*pi0 + 0.0*pi1 + 0.5*pi2 + 0.0*pi3 - pi0),
        sp.Eq(0.3*pi0 + 0.0*pi1 + 0.5*pi2 + 0.0*pi3 - pi1),
        sp.Eq(0.0*pi0 + 0.4*pi1 + 0.0*pi2 + 0.2*pi3 - pi2),
        sp.Eq(0.0*pi0 + 0.6*pi1 + 0.0*pi2 + 0.8*pi3 - pi3),
        sp.Eq(pi0 + pi1 + pi2 + pi3 - 1)]

# define the variables that we are solving for

varlist = [pi0, pi1, pi2, pi3]

# solve the system of two equations

sol = sp.solve(eqns, varlist)
sol

9/20
3/20
3/20
5/20

2/5

# ---- Q2 -----------------------------------------------------

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq(0.8*pi1 + 0.6*pi2 + 0.4*pi3 - pi1),
        sp.Eq(0.1*pi1 + 0.2*pi2 + 0.3*pi3 - pi2),
        sp.Eq(0.1*pi1 + 0.2*pi2 + 0.3*pi3 - pi3),
        sp.Eq(pi1 + pi2 + pi3 - 1)]

# define the variables that we are solving for

varlist = [pi1, pi2, pi3]

# solve the system of two equations

sol = sp.solve(eqns, varlist)
sol

# sol has long decimal values so lets see if there's a fractional representation 

for i in sol:
    print(i, fractions.Fraction(float(sol[i])).limit_denominator())

# ---- Q3 -----------------------------------------------------

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq(0*pi0 + (1/4)*pi1 + (1/4)*pi2 - pi0),
        sp.Eq((1/2)*pi0 + (1/2)*pi1 + (1/4)*pi2 - pi1),
        sp.Eq((1/2)*pi0 + (1/4)*pi1 + (1/2)*pi2 - pi2),
        sp.Eq(pi0 + pi1 + pi2 - 1)]

# define the variables that we are solving for

varlist = [pi0, pi1, pi2]

# solve the system of two equations

sol = sp.solve(eqns, varlist)
sol

# sol has long decimal values so lets see if there's a fractional representation 

for i in sol:
    print(i, fractions.Fraction(float(sol[i])).limit_denominator())

# ---- Q4 -----------------------------------------------------

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq(0.4*pi0 + 0.6*pi1 + 0.4*pi2 - pi0),
        sp.Eq(0.4*pi0 + 0.2*pi1 + 0.2*pi2 - pi1),
        sp.Eq(0.2*pi0 + 0.2*pi1 + 0.4*pi2 - pi2),
        sp.Eq(pi0 + pi1 + pi2 - 1)]

# define the variables that we are solving for

varlist = [pi0, pi1, pi2]

# solve the system of two equations

sol = sp.solve(eqns, varlist)
sol

# sol has long decimal values so lets see if there's a fractional representation 

for i in sol:
    print(i, fractions.Fraction(float(sol[i])).limit_denominator())

x = ((0.2) * (1/4)) / (7/24)
print(fractions.Fraction(x).limit_denominator())


