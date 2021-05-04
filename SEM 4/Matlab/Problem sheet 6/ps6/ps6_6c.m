t=0:1:12
x=exp(t)
y=exp(-t);
w=conv(x,y)
stem(w,'filled')

