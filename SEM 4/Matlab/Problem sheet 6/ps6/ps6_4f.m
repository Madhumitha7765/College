syms s
f1=4/((s^2+25)^2);
subplot(1,2,1);
ezplot(f1)
f2=ilaplace(f1)
subplot(1,2,2);
ezplot(f2)