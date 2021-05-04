syms s
f1=s/((s^2-9)^2);
subplot(1,2,1);
ezplot(f1)
f2=ilaplace(f1)
subplot(1,2,2);
ezplot(f2)