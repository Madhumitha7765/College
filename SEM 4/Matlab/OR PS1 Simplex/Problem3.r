# LPP MODEL:
# x1: tables
# x2: chairs
# 
# 4x1+3x2 <=240
# 2x1+x2  <=100
# 
# Max Z=7x1+5x2

library(lpSolve)

f.obj <- c(7,5)
f.con <- matrix(c(4,3,2,1),nrow=2,byrow=TRUE)
f.dir <- c("<=","<=")
f.rhs <- c(240,100)

lp("max",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)
lp1$solution



#ANSWER
# Success: the objective function is 410 
# [1] 30 40

