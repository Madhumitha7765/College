t=-8*pi:1:8*pi
x=cos(2*t)
y=sin(3*t);
w=conv(x,y)
stem(w,'filled')

