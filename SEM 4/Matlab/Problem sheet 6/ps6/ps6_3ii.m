syms t
f1=t*sin(3*t)-2;
subplot(1,2,1);
ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)