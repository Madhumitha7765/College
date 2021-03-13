n=3;
 s2='binomial';
 s3='geometric';
 s4='poisson';
for i=1:n
        Type{i} = input('Enter word:\n','s');
        s2='binomial';
        if(strcmp(Type{i},s2))
            n=4;
        end
end
if(strcmp(Type{1},s2))
n1=Type{2};
p1=Type{3};
n=str2num(n1);
p=str2num(p1);
mean=n*p
variance=n*p*(1-p)
end
if(strcmp(Type{1},s3))
    
   p1=Type{2};
   p=str2num(p1);
   mean=1/p
   variance=(1-p)/(p*p)
end
if(strcmp(Type{1},s4))
    lambda1=Type{2};
    lambda=str2num(lambda1);
    mean=lambda
    variance=lambda
end
