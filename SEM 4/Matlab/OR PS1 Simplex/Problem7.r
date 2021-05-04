# LPP MODEL:
# x1: units of A
# x2: units of B
# x3: units of C produced
# x4: units of  destroyed
# 
# 3x1+4x2 <=18
# 3x1+5x2 <=21
# x3<=5
# -3x2+x3+x4=0
# 
# Max Z=3x1+8x2+2x3-x4

library(lpSolve)

f.obj <- c(3,8,2,-1)
f.con <- matrix(c(3,4,0,0,
                  3,5,0,0,
                  0,0,1,0,
                  0,-3,1,1),nrow=4,byrow=TRUE)
f.dir <- c("<=","<=","<=","=")
f.rhs <- c(18,21,5,0)

lp("max",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)
lp1$solution



#ANSWER
#Success: the objective function is 36 
#[1] 2 3 5 4

