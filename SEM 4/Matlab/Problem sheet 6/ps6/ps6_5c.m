syms t
f1=15*t*heaviside(t)-15*t*heaviside(t-3);
subplot(1,2,1);
fplot(f1,[-4 4]);%ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)