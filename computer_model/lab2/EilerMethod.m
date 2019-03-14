function [x,y] = EilerMethod(func,t0,tf,y0,h)
%x = zeros((tf-t0)/h);
%length(x)
x(1) = t0;
y(:,1) = y0;
i = 2;
while(x(i-1)< tf)
    x(i) = x(i-1)+h;
    y(:,i) = y(:,i-1)+func(x(i-1),y(:,i-1))*h;
    i = i + 1;
end
end