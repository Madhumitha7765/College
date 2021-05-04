# T = dollars invested in trade credit
# B = dollars invested in corporate bonds
# G = dollars invested in gold stocks
# C = dollars invested in construction loans
# Objective
# Maximize dollars of interest earned = 0.07 T + 0.11 B + 0.19 G + 0.15 C
# Subject to 
# T ???1,000,000 (max investment in T)
# B ???2,500,000 (max investment in B)
# G ???1,500,000 (max investment in G)
# C ???1,800,000 (max investment in C)
# G+C ??? 0.55 (T+B+G+C) (Board condition 1)
# T ??? 0.15 (T+B+G+C) (Board condition 2)
# T+B+G+C ???5,000,000 (max dollars invested)
# T, B, G, C ??? 0 (non-negativity conditions)

library(lpSolve)

f.obj <- c(0.07,0.11,0.19,0.15)
f.con <- matrix(c(1,0,0,0,
                  0,1,0,0,
                  0,0,1,0,
                  0,0,0,1,
                  0.55,0.55,-0.45,-0.45,
                  -0.85,0.15,0.15,0.15,
                  1,1,1,1),nrow=7,byrow=TRUE)
f.dir <- c("<=","<=","<=","<=","<=","<=","<=")
f.rhs <- c(1000000,2500000,1500000,1800000,0,0,5000000)

lp("max",f.obj,f.con,f.dir,f.rhs)
lp1 <- lp("max",f.obj,f.con,f.dir,f.rhs)
lp1$solution