function yprime = vdpol( t,y )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
yprime = [y(2); (-450*t*y(1))/(225*t*t-1)];

end

