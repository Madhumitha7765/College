library(lpSolve)

# Set up cost matrix
a <- matrix(c(17,25,31,10,25,16,12,14,11), nrow = 3, byrow = TRUE)
b <- c(1, 1, 1, 1)
cost.mat <- a*b

# Run

lpassign <- lp.assign(cost.mat, direction = "min")
lpassign$solution
lpassign$objval