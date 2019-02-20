clc;
t0 = 1;
tf = 2;
y0 = [14 16];
[t ,y] = ode45('vdpol',[t0 tf],y0);
plot(t,y),title('Van der Pol equation time history')