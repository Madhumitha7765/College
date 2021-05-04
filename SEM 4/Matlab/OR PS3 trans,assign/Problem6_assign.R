library(lpSolve)

# Set up cost matrix
a <- matrix(c(80,55,45,45,58,35,70,50,70,50,80,65,90,70,40,80), nrow = 4, byrow = TRUE)
b <- c(1, 1, 1, 1)
cost.mat <- a*b

# Run

lpassign <- lp.assign(cost.mat, direction = "max")
lpassign$solution
lpassign$objval