syms t
f1=2*heaviside(t)-3*heaviside(t-2)+1*heaviside(t-3);
subplot(1,2,1);
fplot(f1,[-4 4]);%ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)