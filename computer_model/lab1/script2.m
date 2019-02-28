clc;
t0 = 0;
tf = 2;
y0 = [1 1 1];
[t ,y] = ode45('vdpol2',[t0 tf],y0);
plot(t,y),title('Van der Pol equation time history')

A = [1,0,0; -1,1,0; 1,-2,2];
B = [1;1;1] ;
C = A\B;

FtCC1 = (C(1)+C(2)*t+C(3)*t.^2+t.^3/6).*exp(-t);
% FtCC2 = -C(1).*exp(-t)+C(2).*(-exp(-t).*t+exp(-t))+C(3).*(exp(-t).*t.^2+2.*t.*exp(-t))-(exp(-t).*t.^3)/6+(exp(-t).*t.^2)/2;
% FtCC3 =
hold on;
plot(t,FtCC1,'r*')
% plot(t,FtCC2,'g*'),title('My solution')
% plot(t,FtCC,'*'),title('My solution')
