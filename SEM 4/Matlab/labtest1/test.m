for i=1:1000
    if mod(i,2)==0
        if mod(i,5)==0 && mod(i,7)==0
            if mod(i,3)~=0
                disp(i)
            end
        end
    end
end