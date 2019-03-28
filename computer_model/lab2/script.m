clear all;
clc;

% solution first
t0 = 0;
tf = 5;
y0 = 1;
h = [0.1;0.2;0.05]
my_func = @(t,y)sin(t) - 2*y;
[t ,y] = ode23(my_func,[t0 tf],y0);
figure(1);
plot(t,y,'r');
hold on;
[t2,y] = EilerMethod(my_func,t0,tf,y0,h(1));
plot(t2,y,'*b');


my_func2 = @(t)(6/5)*exp(-2*t)+(2/5)*sin(t)-(1/5)*cos(t);
plot(t2,my_func2(t2),'g*')

kek = sum(abs(y-my_func2(t2)))

% solution second
t0 = 0;
tf = 5;
y0 = [1;1];

my_func = @(t,y) [y(2); sin(t)-2*y(1)-y(2)];
[t,y] = ode45(my_func,[t0 tf],y0);
figure(2);
hold on;
plot(t,y,'r');

[t2,y] = EilerMethod(my_func,t0,tf,y0,h(1));
plot(t2,y,'*b');
