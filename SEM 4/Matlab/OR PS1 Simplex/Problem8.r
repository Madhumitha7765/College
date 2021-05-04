# LPP MODEL:
# x1: trainees in week1
# x2: trainees in week2
# x3: trainees in week3
# x4: trainees in week4
# x5: trainees in week5
# 
# x1<=60
# x1+x2 <=6
# 3x1-x2-x3>=15
# 3x1+3x2-x3-x4>=180
# 3x1+3x2+3x3-x4-x5>=300
# x1+X2+x3+x4+x5=150
# Max Z=5x1+4x2+3x3+2x4+x5

library(lpSolve)

f.obj <- c(5,4,3,2,1)
f.con <- matrix(c(1,0,0,0,0,
                  1,1,0,0,0,
                  3,-1,-1,0,0,
                  3,3,-1,-1,0,
                  3,3,3,-1,-1,
                  1,1,1,1,1),nrow=6,byrow=TRUE)
f.dir <- c("<=","<=",">=",">=",">=","=")
f.rhs <- c(60,6,15,180,300,150)

lp("max",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)
lp1$solution



#ANSWER


