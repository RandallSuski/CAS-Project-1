# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:44:23 2024

@author: randa
"""

from matplotlib import pyplot

'Returns the next x value based on the logistic equation'
def logEq(x, r):
    return r*x*(1-x)

'2.1 goes over 200 time steps'
totalSteps = 200

'The values we will use that are close to each other'
x01 = 0.500
x02 = 0.501

'r1 is stable, r2 periodic, r3 chaotic'
r1 = 2.500
r2 = 3.452
r3 = 3.780

time = list(range(0, 201))

panelAx01 = list(range(0, 201))
panelAx02 = list(range(0, 201))
panelBx01 = list(range(0, 201))
panelBx02 = list(range(0, 201))
panelCx01 = list(range(0, 201))
panelCx02 = list(range(0, 201))

panelAx01[0] = x01
panelBx01[0] = x01
panelCx01[0] = x01
panelAx02[0] = x02
panelBx02[0] = x02
panelCx02[0] = x02

'Calculate Stable Panel'
for i in range(1, 201):
    panelAx01[i] = logEq(panelAx01[i-1], r1)
    panelAx02[i] = logEq(panelAx02[i-1], r1)
    panelBx01[i] = logEq(panelBx01[i-1], r2)
    panelBx02[i] = logEq(panelBx02[i-1], r2)
    panelCx01[i] = logEq(panelCx01[i-1], r3)
    panelCx02[i] = logEq(panelCx02[i-1], r3)
    
print(time)
print(panelAx01)
print(panelAx02)

pyplot.figure(1)

pyplot.plot(time, panelAx01, label="$x_0$ = 0.500")   
pyplot.plot(time, panelAx02, label="$x_0$ = 0.501")

pyplot.xlabel('Time Steps')
pyplot.ylabel('Relative Population Size')
pyplot.title('Relative Population Over Time for R = 2.500')
pyplot.legend()
pyplot.savefig('PanelA.png', dpi=500, format='png', bbox_inches='tight', pad_inches=0.0,)


pyplot.figure(2)

pyplot.plot(time, panelBx01, label="$x_0$ = 0.500")   
pyplot.plot(time, panelBx02, label="$x_0$ = 0.501")

pyplot.xlabel('Time Steps')
pyplot.ylabel('Relative Population Size')
pyplot.title('Relative Population Over Time for R = 3.452')
pyplot.legend()
pyplot.savefig('PanelB.png', dpi=500, format='png', bbox_inches='tight', pad_inches=0.0,)

pyplot.figure(3)

pyplot.plot(time, panelCx01, label="$x_0$ = 0.500")   
pyplot.plot(time, panelCx02, label="$x_0$ = 0.501")

pyplot.xlabel('Time Steps')
pyplot.ylabel('Relative Population Size')
pyplot.title('Relative Population Over Time for R = 3.780')
pyplot.legend()
pyplot.savefig('PanelC.png', dpi=500, format='png', bbox_inches='tight', pad_inches=0.0,)

pyplot.figure(4)

pyplot.plot(time[0:30], panelAx01[0:30], label="$x_0$ = 0.500")   
pyplot.plot(time[0:30], panelAx02[0:30], label="$x_0$ = 0.501")

pyplot.xlabel('Time Steps')
pyplot.ylabel('Relative Population Size')
pyplot.title('Relative Population Over Time for R = 2.500 Zoomed In')
pyplot.legend()
pyplot.savefig('PanelAZoom.png', dpi=500, format='png', bbox_inches='tight', pad_inches=0.0,)


pyplot.figure(5)

pyplot.plot(time[0:30], panelBx01[0:30], label="$x_0$ = 0.500")   
pyplot.plot(time[0:30], panelBx02[0:30], label="$x_0$ = 0.501")

pyplot.xlabel('Time Steps')
pyplot.ylabel('Relative Population Size')
pyplot.title('Relative Population Over Time for R = 3.452 Zoomed In')
pyplot.legend()
pyplot.savefig('PanelBZoom.png', dpi=500, format='png', bbox_inches='tight', pad_inches=0.0,)

pyplot.figure(6)

pyplot.plot(time[0:30], panelCx01[0:30], label="$x_0$ = 0.500")   
pyplot.plot(time[0:30], panelCx02[0:30], label="$x_0$ = 0.501")

pyplot.xlabel('Time Steps')
pyplot.ylabel('Relative Population Size')
pyplot.title('Relative Population Over Time for R = 3.780 Zoomed In')
pyplot.legend()
pyplot.savefig('PanelCZoom.png', dpi=500, format='png', bbox_inches='tight', pad_inches=0.0,)