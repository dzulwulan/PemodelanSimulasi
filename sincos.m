clear all;
close all;
clc;

N = 101;
dx= (2*pi)/(N-1);

x = [0:dx:(2*pi)];

for i=1:N
    f(i) = sin(x(i))
    g(i) = cos(x(i))
endfor
plot(x,f,'o')
hold on
plot(x,g)
hold off
