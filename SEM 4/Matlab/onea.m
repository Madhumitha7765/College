function correlation()
    x=[70,92,80,74,65,83];
    y=[74,84,63,87,78,90];
    x1=sum(x)/6;
    y1=sum(y)/6;
    for i= 1:6
      r=r+((x1-x(i))*(y1-y(i))/sqrt(power(x1-x(i),2))*sqrt(power(y1-y(i),2)));
    end
    sprintf('%d',r);
end 

%correlation()


    
