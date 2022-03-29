import math
import numpy as np
import matplotlib.pyplot as plt
#laserscan dosyasındaki verileri alma

scan= np.loadtxt('laserscan.dat')

angle = np.linspace(-math.pi/2, math.pi/2, np.shape(scan)[0], endpoint='true')

# laser end-poin çizimi için
x=scan*np.cos(angle)#kartezyen koordinat düzlemine aktarma
y=scan*np.sin(angle)
points=np.stack((x,y), axis=-1)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(points[: ,0],points[: ,1], 'o', color='black')
plt.show()
#dünyadan robota
awr=math.pi/4
pwr=[[1.0],[0.5]]
Rwr=np.matrix([[math.cos(awr),-math.sin(awr)],[math.sin(awr),math.cos(awr)]])


#robottan dünyaya

ars =math.pi*4
prs=[[0.2],[0.0]]
Rrs=np.matrix([[math.cos(ars),-math.sin(ars)], [math.sin(ars), math.cos(ars)]])

print("robot merkezinin dünyadaki koordinatları:", pwr)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(pwr[0],pwr[1], '*', color='red')

pws = np.matmul(Rwr, prs)+pwr
plt.plot(pws[0], pws[1], 'o', color='blue')
print("Dünya koordinatlarında sensörün merkezi: " , pws)

pointrf = np.matmul(Rrs, points.T)+prs
pointswf=np.matmul(Rwr, pointsrf)+pwr
pointswf=pointswf.T
plt.plot(pointswf[: ,0],pointswf[: ,1], 'o', color='black')
plt.show()
