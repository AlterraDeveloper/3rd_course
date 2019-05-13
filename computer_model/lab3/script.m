clc;
clear all;
%Задание передаточных функций элементов
k1=.19;
k2=.19;
k3=.19;
k4=.19;
ksi=.19;
T1=.19;
T2=.19;
T3=.19;
T4=.19;

 
num1=[k1]; 
den1=[T1^2 2*ksi*T1 1];
num2=[k2]; 
den2=[T2 1];
num3=[k3]; 
den3=[1];
num4=[k4]; 
den4=[T4^2 2*ksi*T4 1];

%Последовательное соединение систем W2 и W3.
[num23,den23] = series(num2,den2,num3,den3);

%Последовательное соединение систем W3 и W2 и W4.
[num34,den34]=series(num23,den23,num4,den4);

%Параллельное соединение систем W1 и W3.
[num1_3,den1_3]=parallel(num1,den1,num3,den3);

%Параллельное соединение систем W1W3+W3W4 и W4.
[num_y1,den_y1]=parallel(num1_3,den1_3,num34,den34);


%Вывод на экран найденых передаточных функций 
disp('Wy_u1');
printsys(num_y1,den_y1,'p');
disp('Wy_u2');
printsys(num4,den4,'p');

%Plot step response
subplot(221),step(num_y1,den_y1);
title('Step response u1-y')
t=0:1:60;
subplot(222);
step(num4,den4,t);
title('Step response u2-y'),

%Решение задачи для систем, заданных моделями в состояниях.
%Transfer function to state space conversion
% [a1,b1,c1,d1]=tf2ss(num1,den1);
% [a2,b2,c2,d2]=tf2ss(num2,den2);
% [a3,b3,c3,d3]=tf2ss(num3,den3);
% [a4,b4,c4,d4]=tf2ss(num4,den4);
% 
% %Series system connection
% %Connection of W1 and W3 systems
% [a13,b13,c13,d13]=series(a1,b1,c1,d1,a3,b3,c3,d3);
% %Connection of W3 and W4 systems
% [a34,b34,c34,d34]=series(a4,b4,c4,d4,a3,b3,c3,d3);
% 
% %Parallel system connection
% %Connection of W1W3 and W3W4 systems
% [a13_34,b13_34,c13_34,d13_34]=parallel(a34,b34,c34,d34,a13,b13,c13,d13);
% %Connection of W1W3+W3W4 and W4 systems
% [au2_y,bu2_y,cu2_y,du2_y]=parallel(a13_34,b13_34,c13_34,d13_34,a4,b4,c4,d4);
% 
% %Вывод на экран найденых моделей в состояниях 
% disp('Wy_u1,State space model'); 
% au1_y=a3;bu1_y=b3;cu1_y=c3;du1_y=d3;
% printsys(au1_y,bu1_y,cu1_y,du1_y);
% disp('Wy_u2,State space model'); 
% printsys(au2_y,bu2_y,cu2_y,du2_y);
% 
% %Вычисление установившегося значения коэффициента усиления системы
% %State-space model gain
% disp('The steady state gain of the state-space model')
% kstate=dcgain(au2_y,bu2_y,cu2_y,du2_y)
% %Transfer function model gain
% disp('The steady state gain of the transfer function model')
% ktrfun=dcgain(numy_u2,deny_u2)
% 
% %Plot step response
% subplot(223),step(a3,b3,c3,d3,1);
% title('Step response u1-y,state model')
% t=0:1:60;
% subplot(224);
% step(au2_y,bu2_y,cu2_y,du2_y,1,t);
% title('Step response u2-y,state model'),pause(3)
% 
% %Создание нового графического окна
% figure(2)
% %Импульсная реакция системы
% t=1:1:100;
% subplot(223),impulse(a3,b3,c3,d3,1,t);
% title('impulse response u1-y,state model')
% subplot(224);impulse(au2_y,bu2_y,cu2_y,du2_y,1,t);
% title('impulse response u2-y,state model')
% subplot(221),impulse(num3,den3,t);
% title('impulse response u1-y')
% subplot(222);impulse(numy_u2,deny_u2,t);
% title('impulse response u2-y'),
% 
% %Реакция системы на произвольный сигнал
% %Создание нового графического окна
% figure(3)
% %Графики реакции на сигнал вида r/t, где r-константа
% t=1:1:100;
% subplot(223),lsim(a3,b3,c3,d3,.2./t,t);
% title('r/t response u1-y,state model')
% subplot(224);
% lsim(au2_y,bu2_y,cu2_y,du2_y,.2./t,t);
% title('r/t response u2-y,state model')
% subplot(221),lsim(num3,den3,.2./t,t);
% title('r/t response u1-y')
% subplot(222);
% lsim(numy_u2,deny_u2,.2./t,t);
% title('r/t response u2-y'),pause(3);
