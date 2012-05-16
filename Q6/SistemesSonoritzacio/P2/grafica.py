#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author:  Marc Pomar Torres - P2 - Sistemes de Sornorització
Desc:    Genera una gráfica con los resultados medidos en los acelerómetros
'''
import array
import numpy
import pylab
import operator

freq = (6.05, 7.03, 8.01, 8.98, 9.96, 10.94, 11.91, 13.09, 15.04, 16.99,
		 18.95, 21.09, 22.07, 23.05, 24.02, 25, 25.98, 26.95, 28.91, 31.05)
acc1 = (56.72, 60.30, 62.99, 66.82, 74.70, 66.38, 69.04, 71.25, 75.58, 81.73,
		 85.93, 94.87, 96.48, 94.87, 93.09, 90.15, 87.49, 86, 84.56, 84.37)
acc2 = (60.51, 65.84, 71.28, 78.37, 95.52, 84.91, 78.87, 76.51, 76.05, 78.83,
		80.16, 86.12, 86.60, 84.01, 81.35, 77.68, 74.40, 71.78, 68.45, 66.26)
def main():
	fig = pylab.gcf()
	pylab.plot(freq,acc1)
	pylab.plot(freq,acc2)
	pylab.xlabel('Frecuencia (Hz)')
	pylab.ylabel('dB')
	pylab.legend(('Acc1','Acc2',), loc='best')
	fig.savefig("grafica.png")
	
	pylab.clf()
	
	fig2 = pylab.gcf()
        pylab.plot(freq,tuple(map(operator.div,acc2,acc1)))
        pylab.xlabel('Frecuencia (Hz)')
        pylab.ylabel('C')
        pylab.legend(('Acc2/Acc1',), loc='best')
        fig2.savefig("grafica_x2_x1.png")
	



if __name__ == "__main__": main()
