# LPP MODEL: 
# x1 : notebook computers
# x2 : desktop computers
# 
# x1+x2 <= 10000
# x1+2x2 <= 15000
# 4x1+3x2<=25000
# 
# Max z = 750x1+1000x2

library(lpSolve)

f.obj <- c(750,1000)
f.con <- matrix(c(1,1,1,2,4,3),nrow=3,byrow=TRUE)
f.dir <- c("<=","<=","<=")
f.rhs <- c(10000,15000,25000)

lp("max",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)
lp1$solution


#ANSWER:
#Success: the objective function is 7750000 
#[1] 1000 7000