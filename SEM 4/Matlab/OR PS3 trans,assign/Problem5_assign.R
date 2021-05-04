library(lpSolve)

# Set up cost matrix
a <- matrix(c(10,14,16,13,12,13,15,12,9,12,12,11,14,16,18,16), nrow = 4, byrow = TRUE)
b <- c(1, 1, 1, 1)
cost.mat <- a*b

# Run

lpassign <- lp.assign(cost.mat, direction = "min")
lpassign$solution
lpassign$objval