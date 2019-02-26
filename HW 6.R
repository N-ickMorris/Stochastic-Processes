
require(MASS)

# --------------------------------------------------------------------------------------
# ---- Q2 ------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

# define the probability matrix P

P = cbind(c(1, .5, 0, 0), c(0, .25, .5, 0), c(0, .25, .25, 0), c(0, 0, .25, 1))
P

# define the absorbing states

A = c(1, 4)

# define the non-absorbing states

Ac = c(2, 3)

# extract Q and B from transition probability matrix P
	# Q corresponds to all probabilities of a non-absorbing state transitioning to a non-absorbing state
	# B corresponds to all probabilities of a non-absorbing state transitioning to an absorbing state
	
Q = P[Ac, Ac]
Q

B = P[Ac, A]
B

# R corresponds to the expected number of returns to a state j given that the initial state was i
# compute the R component for transient state pairs (ie. matrix Q)

R1 = solve(diag(rep(1, nrow(Q))) - Q)
R1

# F corresponds to the first passage probability, the probability of eventually reaching a state j at least once given that the initial state was i
# compute the F component for a transient state visiting a recurrent state (ie. matrix B)

F1 = R1 %*% B
F1













