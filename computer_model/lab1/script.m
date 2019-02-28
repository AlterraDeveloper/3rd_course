clc;
t0 = 1;
tf = 2;
y0 = [14 16];
[t ,y] = ode45('vdpol',[t0 tf],y0);
[t,y];
plot(t,y),title('Van der Pol equation time history')

A = [1 log(8/7) ; 0 -450/224];
B = [14;16] ;
C = A\B;

FtCC = zeros(numel(t),1);
c = 1;
for i = t.'
 FtCC(c,1) = C(1) + C(2)*log((15*i+1)/(15*i-1));
 c = c+1;
end
FtCC;
plot(t,FtCC),title('My solution')