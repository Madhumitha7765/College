# LPP MODEL
# x1:TV
# x2:Mag
#
# 5x1+2x2>=24
# x1+6x2>=18
# 3x1+3x2>=24
#
# Min 600x1+500x2


library(lpSolve)

f.obj <- c(600,500)
f.con <- matrix(c(5,2,1,6,3,3),nrow=3,byrow=TRUE)
f.dir <- c(">=",">=",">=")
f.rhs <- c(24,18,24)

lp("min",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("min",f.obj,f.con,f.dir,f.rhs)
lp1$solution


# ANSWER
# Success: the objective function is 4266.667 
#[1] 2.666667 5.333333