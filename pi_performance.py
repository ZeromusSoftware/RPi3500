import numpy as np
import time 
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

#we are going to calculate pi with an integration of 
#arctan(x)' between 0 and 1 (that calculates pi/4)

def darctan(x) : # we introduce the arctan(x)'function
	result = 1/(1+x**2)
	return result

def pi(n) : # n will be the number of trapeze in the
#calcul of the integrate of arctan'(x)

	tps1 = time.clock() # we look at the time before 
# launching the calcul

# this is the calcul
	pas = 1/n
	somme = 0
	for i in range(n) :
		somme += (4*darctan(i*pas) + 4*darctan((i+1)*pas))*pas
	somme = somme/2

# we look at the time after the calcul
	tps2 = time.clock()
	total_time = tps2 - tps1

	return total_time

# we will be doing measures of the calcul time for different
# values of n
measureNumber = 0

# we want to take mesures equaly spaced for n between two
# powers of 10 (for n<10, take 10 measures spaced by 1, for 
# 10<n<100, spaced by 10...etc.)

n = 37 # number of values that I want
fin = n + n//10 
if fin%10 == 0: fin += 1
limit = [10**i for i in range(1,(fin//10) +2)] # list of powers of 10
k = 0

X = [] # Accuracy
Y = [] # Execute time (s)


while measureNumber < fin :
	pas = limit[k]/10
	for i in range(1,11) :
		if measureNumber < fin :
			X.append(pas*i)
			Y.append(pi(pas*i))
			measureNumber += 1
	if measureNumber%10 == 0 :
		k += 1	
		X.pop()
		Y.pop()

# We fit to the measures a linear model and with the slope, we introduce a peformance
# value : ppf (Pi Performance Factor). The lower the slope is, the higher the ppf is
coefdir,ordorigine = np.polyfit(X,Y,1)
ppf = 1/(10**3*coefdir)
print ("ppf :" + str(ppf))

# We measure the correlation coefficient of the linear model
cor,a = pearsonr(X, Y)
print("Correlation coeff : " + str(cor))

plt.figure(1)
plt.plot(X,Y,'*')

plt.title("PI performance")
plt.xlabel("Accuracy")
plt.ylabel("Time (s)")
plt.grid()
plt.axis()
plt.show()


