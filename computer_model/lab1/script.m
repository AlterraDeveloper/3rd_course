clear;
clc;
t0 = 1;
tf = 2;
y0 = [14 16];
[t ,y] = ode45('vdpol',[t0 tf],y0);
plot(t,y),title('Van der Pol equation time history')

A = [1 log(8/7) ; 0 -30/224];
B = [14;16] ;
C = A\B;

FtCC1 = C(1) + C(2)*log((15*t+1)./(15*t-1));
FtCC2 = (-30*C(2))./((225*t.^2)-1);
hold on;
plot(t,FtCC1, 'g*')
plot(t,FtCC2, 'b*'),title('My solution')