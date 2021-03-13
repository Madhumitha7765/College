function correlation()
    x=[70,92,80,74,65,83];
    y=[74,84,63,87,78,90];
    xm=sum(x)/6;
    ym=sum(y)/6;
    for i= 1:6
      r=r+(xm-x(i))*(ym-y(i))/sqrt(power(xm-x(i),2))*sqrt(power(ym-y(i),2));
    end
    printf('%d',r);
end 
