function yprime = vdpol2( t,y )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
yprime = [y(2);y(3); exp(-t)-y(1)-3*y(2)-3*y(3)];

end
