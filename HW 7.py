# -------------------------------------------------------------
# ---- HW 7 ---------------------------------------------------
# -------------------------------------------------------------

import sympy as sp
import fractions

# ---- Q1 -----------------------------------------------------

# ---- Part 1 --------------------

# define the variables for computing the limiting distribution

pi5 = sp.Symbol('pi5')
pi6 = sp.Symbol('pi6')
pi7 = sp.Symbol('pi7')

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq(0.3*pi5 + 0.1*pi6 + 0.8*pi7 - pi5),
        sp.Eq(0.4*pi5 + 0.0*pi6 + 0.2*pi7 - pi6),
        sp.Eq(0.3*pi5 + 0.9*pi6 + 0.0*pi7 - pi7),
        sp.Eq(pi5 + pi6 + pi7 - 1)]

# define the variables that we are solving for

varlist = [pi5, pi6, pi7]

# solve the system of two equations

sol = sp.solve(eqns, varlist)

# sol has long decimal values so lets see if there's a fractional representation 

for i in sol:
    print(i, fractions.Fraction(float(sol[i])).limit_denominator())

# ---- Part 2 --------------------

# define the variables for computing the limiting distribution

u0 = sp.Symbol('u0')
u1 = sp.Symbol('u1')
u2 = sp.Symbol('u2')

# define the system that must be solved based on the transition probability matrix

eqns = [sp.Eq(-u0 + 0.1*u0 + 0.1*u1 + 0.2*u2 + 0.2*1 + 0.1*1 + 0.1*0 + 0.1*0 + 0.1*0),
        sp.Eq(-u1 + 0.0*u0 + 0.1*u1 + 0.1*u2 + 0.1*1 + 0.0*1 + 0.3*0 + 0.2*0 + 0.2*0),
        sp.Eq(-u2 + 0.6*u0 + 0.0*u1 + 0.0*u2 + 0.1*1 + 0.1*1 + 0.1*0 + 0.1*0 + 0.0*0)]

# define the variables that we are solving for

varlist = [u0, u1, u2]

# solve the system of two equations

sol = sp.solve(eqns, varlist)

# sol has long decimal values so lets see if there's a fractional representation 

for i in sol:
    print(i, fractions.Fraction(float(sol[i])).limit_denominator())

for i in sol:
    print(i, 1 - fractions.Fraction(float(sol[i])).limit_denominator())


print(fractions.Fraction(float((53/116) * (1/2))).limit_denominator())

print(fractions.Fraction(float((19/116) * (1/2))).limit_denominator())

print(fractions.Fraction(float((55/116) * (1/2))).limit_denominator())



print(fractions.Fraction(float((63/116) * (41/97))).limit_denominator())

print(fractions.Fraction(float((97/116) * (41/97))).limit_denominator())

print(fractions.Fraction(float((61/116) * (41/97))).limit_denominator())



print(fractions.Fraction(float((63/116) * (23/97))).limit_denominator())

print(fractions.Fraction(float((97/116) * (23/97))).limit_denominator())

print(fractions.Fraction(float((61/116) * (23/97))).limit_denominator())



print(fractions.Fraction(float((63/116) * (33/97))).limit_denominator())

print(fractions.Fraction(float((97/116) * (33/97))).limit_denominator())

print(fractions.Fraction(float((61/116) * (33/97))).limit_denominator())


(53/232) + (53/232) + (2583/11252) + (1449/11252) + (2079/11252)

(19/232) + (19/232) + (41/116) + (23/116) + (33/116)

(55/232) + (55/232) + (2501/11252) + (1403/11252) + (2013/11252)









