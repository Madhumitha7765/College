syms t
i=3*t^2-4*t+5;
xi=laplace(i)
ii=(cos(t)^2)+2*exp(-3*t)-7;
xii=laplace(ii)
iii=exp(3*t)*cosh(3*t);
xiii=laplace(iii)
iv=sinh(t)*cos(3*t);
xiv=laplace(iv)
v=((t+1)^2)*exp(3*t);
xv=laplace(v)
