# No feasible solution

library(lpSolve)

f.obj <- c(1500, 1000)

f.con <- matrix(c(5, 2,
                  5, 3,
                  1, 0,
                  0, 1), nrow = 4, byrow = TRUE)

f.dir <- c("<=", "<=", ">=", ">=")
f.rhs <- c(6000, 7500, 1000, 2000)
lp("max", f.obj, f.con, f.dir, f.rhs)
lp1 <- lp("max", f.obj, f.con, f.dir, f.rhs)
lp1$objval - 1500000
lp1$solution

duals <- lp("max", f.obj, f.con, f.dir, f.rhs, compute.sens = TRUE)$duals
duals[1]
duals[2]