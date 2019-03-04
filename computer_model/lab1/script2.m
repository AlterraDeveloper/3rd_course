clc;
t0 = 0;
tf = 2;
y0 = [1 1 1];
[t ,y] = ode45('vdpol2',[t0 tf],y0);
plot(t,y)

A = [1,0,0; -1,1,0; 1,-2,2];
B = [1;1;1] ;
C = A\B;

FtCC1 = (C(1)+C(2)*t+C(3)*t.^2+t.^3./6).*exp(-t);
FtCC2 = -exp(-t).*(C(1)+C(2)*t+C(3)*t.^2+t.^3./6)+exp(-t).*(C(2)+2*C(3).*t+t.^2./2);
FtCC3 = (2*C(3)+t).*exp(-t)-(C(2)+2*C(3).*t+t.^2./2).*exp(-t)-(C(2)+2*C(3).*t+t.^2./2).*exp(-t)+(C(1)+C(2).*t+C(3).*t.^2+t.^3./6).*exp(-t);
hold on;
plot(t,FtCC1,'r*')
plot(t,FtCC2,'g*')
plot(t,FtCC3,'b*'),title('My solution')
