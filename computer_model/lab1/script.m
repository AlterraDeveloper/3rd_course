clc;
t0 = 1;
tf = 2;
y0 = [14 16];
[t ,y] = ode45('vdpol',[t0 tf],y0);
[t,y]
plot(t,y),title('Van der Pol equation time history')


% clc
% 
% A = [1 log(8/7) ; 0 -450/224]
% B = [14 16]
% 
% B*inv(A)