import math
import matplotlib.pyplot as plt

# Menghitung x(t)
def x_t(v0,t,teta):
    return (v0*math.cos(teta)*t)

# Menghitug y(t)
def y_t(v0,t,teta):
    return ((-9.8*t**2)/2) + (v0*math.sin(teta)*t)

# Menghitung t total
def t_tot(v0,teta):
    return -2*v0*math.sin(teta)/-9.8

# Menghitung x total
def x_tot(v0,teta):
    return v0*math.cos(teta)*t_tot(v0,teta)

# Menghitung y total
def y_tot(v0,teta):
    return (v0**2 * math.sin(teta)**2) / (-2*-9.8)

# Modifikasi perulangan supaya bisa bertipe float
def loop_range(start, stop, inc):
    while start < stop :
        yield start
        start += inc

v0 = 20 # Inisialisasi v0
teta = 45 # Inisialisasi teta
x = [] # Inisialisasi array x untuk menampung x(t)
y = [] # Inisialisasi array y untuk menampung y(t)
t_total = t_tot(v0,teta) # Menghitug t total untuk patokan perulangan
for t in loop_range(0, t_total, 0.01): # Melakukan perulangan dengan range 0 - t_total dengan beda 0,01
    x.append(x_t(v0,t,teta)) # Menghitung dan menambahkan x(t) ke dalam array x
    y.append(y_t(v0,t,teta)) # Menghitung dan menambahkan y(t) ke dalam array y

plt.plot(x,y) # Membuat grafik
plt.axis([0, x_tot(v0,teta)+1, 0, y_tot(v0,teta)+1]) # Menentukan batasan x_axis dan y_axis
plt.show() # Menampilkan grafik
