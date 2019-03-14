clear;
clc;
t0 = 0;
tf = 5;
y0 = 1;
h = [0.1;0.2;0.05]
my_func = @(t,y)0.5*sin(5*t)-0.1*y;
[t ,y] = ode45(my_func,[t0 tf],y0);
figure(1);
plot(t,y,'r');
hold on;
[t,y] = EilerMethod(my_func,t0,tf,y0,h(3));
plot(t,y,'*b');
