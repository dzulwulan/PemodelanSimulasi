import math
import matplotlib.pyplot as plt

x, y, vy = [],[],[]
a = -9.8
print('Masukkan x(0)', end=': ')
x.append(int(input()))
print('Masukkan y(0)', end=': ')
y.append(int(input()))
print('Masukkan v(0)', end=': ')
v0 = int(input())
print('Masukkan theta', end=': ')
teta = math.radians(int(input()))
print('Masukkan delta T', end=': ')
delta = float(input())

vx = v0*math.cos(teta)
vy.append(v0*math.sin(teta))
vy.append(vy[0] + (a*delta))
i = 0

while (y[i] + (vy[i+1]*delta)) >= 0:
     y.append(y[i] + (vy[i+1]*delta))
     x.append(x[i] + (vx*delta))
     vy.append(vy[i] + (a*delta))
     i += 1

print(x[len(x)-1])
print(max(y))
plt.plot(x,y)
plt.axis([0, 30, 0, 30])
plt.grid()
plt.show()