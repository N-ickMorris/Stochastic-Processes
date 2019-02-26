# --------------------------------------------------------------------------------------
# ---- Q2 ------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

require(MASS)

# build transition probability matrix P

P = rbind(c(0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1),
			c(0.0, 0.1, 0.1, 0.1, 0.0, 0.3, 0.2, 0.2),
			c(0.6, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0),
			c(0.0, 0.0, 0.0, 0.3, 0.7, 0.0, 0.0, 0.0),
			c(0.0, 0.0, 0.0, 0.7, 0.3, 0.0, 0.0, 0.0),
			c(0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.4, 0.3),
			c(0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.9),
			c(0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.2, 0.0))

# compute (I - Q)^-1: which is the expected number of visits/returns to transient state j from transient state i
# where Q is all transitions in P of transient ot transient states

transient = 1:3
Q = P[transient, transient]

I = diag(nrow(Q))

I.Q.inv = solve(I - Q)
fractions(I.Q.inv)

# build D: all transition in P of transient states to non-transient states

D = P[transient, -transient]

# build sub-matrix F1, of the fundamanetal matrix of P
# F1 is the probability of ever visiting transient state j from transient state i

F1 = diag(rep(0, nrow(Q)))

diag(F1) = 1 - (1 / diag(I.Q.inv))

F1[1,2] = I.Q.inv[1,2] / I.Q.inv[2,2]
F1[1,3] = I.Q.inv[1,3] / I.Q.inv[3,3]

F1[2,1] = I.Q.inv[2,1] / I.Q.inv[1,1]
F1[2,3] = I.Q.inv[2,3] / I.Q.inv[3,3]

F1[3,1] = I.Q.inv[3,1] / I.Q.inv[1,1]
F1[3,2] = I.Q.inv[3,2] / I.Q.inv[2,2]

fractions(F1)

# compute (I - Q)^-1 * D: which is the probability of ever visiting reccutrent state j from transient state i

fractions(I.Q.inv %*% D)






