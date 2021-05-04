syms t
f1=sin(t)*heaviside(t-(2*pi));
subplot(1,2,1);
fplot(f1,[-4*pi 4*pi]);%ezplot(f1)
f2=laplace(f1)
subplot(1,2,2);
ezplot(f2)