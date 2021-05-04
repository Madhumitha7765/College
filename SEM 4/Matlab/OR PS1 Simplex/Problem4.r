# LPP MODEL:
# x1: ModelM
# x2: ModelN
# 
# 4x1+2x2 <=80
# 2x1+5x2 <=180
# 
# Max Z=3x1+4x2

library(lpSolve)

f.obj <- c(3,4)
f.con <- matrix(c(4,2,2,5),nrow=2,byrow=TRUE)
f.dir <- c("<=","<=")
f.rhs <- c(80,180)

lp("max",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)
lp1$solution



#ANSWER
# Success: the objective function is 147.5 
# [1]  2.5 35.0

