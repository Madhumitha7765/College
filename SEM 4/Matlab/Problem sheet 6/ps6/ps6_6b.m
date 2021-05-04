t=0:1:4*pi;
x=[1];
y=sin(2*t);
w=conv(x,y)
plot(t,w)

