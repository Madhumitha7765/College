syms t
f1=sin(3*t)+3*t*cos(3*t);
subplot(1,2,1);
ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)