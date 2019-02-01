clear all;
close all;
clc;

N = 21;
T = 5;
v = 1;
G = 9.8;
dt = (T-0)/(N-1);

t = [0:dt:T];
y = 100;
y(1) = y;
y(2) = y(1) + dt*v;
for i=3:N
  y(i) = (2*y(i-1)) - y(i-2) - (G*(dt^2))
endfor

plot(t,y,'o')
