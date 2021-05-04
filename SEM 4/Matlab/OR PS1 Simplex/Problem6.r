# LPP MODEL:
# x1 : TV
# x2 : paperAD
# x3 : radio type 1
# x4 : radio type 2
#
# x1<=12
# x2<=5
# x3<=25
# x4<=20
# 800x1+925x2+290x3+380x4<=8000
# x3+x4>=5
# 290x3+380x4<=1800
# 
# Max Z=5000x1+8500x2+2400x3+2800x4

library(lpSolve)

f.obj <- c(5000,8500,2400,2800)
f.con <- matrix(c(1,0,0,0,
                  0,1,0,0,
                  0,0,1,0,
                  0,0,0,1,
                  800,925,290,380,
                  0,0,1,1,
                  0,0,290,380),nrow=7,byrow=TRUE)
f.dir <- c("<=","<=","<=","<=","<=",">=","<=")
f.rhs <- c(12,5,25,20,8000,5,1800)

lp("max",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)
lp1$solution


# Success: the objective function is 67240.3 
# [1] 1.968750 5.000000 6.206897 0.000000

