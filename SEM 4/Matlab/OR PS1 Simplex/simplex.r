#Import lpsolve
library(lpSolve)

#set coeff of z
#objective (obj) of f
f.obj <- c(4,5)
#c(x,y)-- creating vector keyword


#matrix coresponding to coeff
f.con <- matrix(c(1,2,
                  6,6,
                  1,0),nrow=3,byrow=TRUE)

# set inequalities
f.dir <- c("<=","<=","<=")
#dir- direction of constraint

#rhs 
f.rhs <- c(10,36,4)

lp("max",f.obj,f.con,f.dir,f.rhs)

lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)

#vals stored in variable solution
#vals of soln displayed
lp1$solution