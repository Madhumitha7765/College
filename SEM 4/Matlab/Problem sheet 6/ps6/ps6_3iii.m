syms t
f1=sin(2*t)-2*t*cos(2*t);
subplot(1,2,1);
ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)