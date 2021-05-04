syms t
f1=2*heaviside(t)-2*heaviside(t-4)+(t-1)*heaviside(t-4)-(t-1)*heaviside(t-6);
subplot(1,2,1);
fplot(f1,[-10 10]);%ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)