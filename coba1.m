clear all;
close all;
clc;

N=11;
dx= (1-0)/(N-1);

x = [0:dx:1];

for i=1:N
    f(i)=x(i)^2
endfor
plot(x,f,'o')
