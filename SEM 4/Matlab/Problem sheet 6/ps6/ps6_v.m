syms t
f1=t*exp(-2*t)*cos(3*t);
subplot(1,2,1);
ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)