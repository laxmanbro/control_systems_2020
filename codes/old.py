# License
'''
Code by Laxman Reddy
April 22,2020
Released under GNU GPL
'''
from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.lti([75,0.2*75], [1, 16 ,100,0]) #Transfer Function = 75(1+0.2s)/s(s^2+16s+100)
w, mag, phase = signal.bode(s1)#bode plot signal

#code for mag plot
# plt.figure()
# plt.semilogx(w, mag)    #magnitude plot
# plt.grid()
# plt.title("Magnitude Plot")
# plt.axhline(y = 0,xmin=0,xmax= .35,color = 'r',linestyle='dashed')
# plt.axvline(x = .22,ymin=0,color='k',linestyle='dashed')
# plt.plot(.22,0,'o')
# plt.text(0.757,0, '({}, {})'.format(0.757,-220.15))
# plt.show()

#code for phase Plot 
plt.figure()
plt.semilogx(w, phase)  #phase plot
plt.grid()
plt.title("Phase Plot")
plt.axhline(y = -180,xmin=0,color = 'r',linestyle='dashed')

plt.show()
