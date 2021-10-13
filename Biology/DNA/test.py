
import numpy as np
from matplotlib import pyplot as plt

# pick some points for the secant line
a=3
b=5

# create a buffered interval about [a,b]
e = 4
x = np.linspace(a-e,b+e,num=10000)


# define your function here
def f(x):
  return x**3-7*x**2+2*x-3

# compute the slope of the secant line
m = (f(b)-f(a))/(b-a)


# set up the plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
plt.grid(True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# plot your function and secant line
ax.plot(x,f(x))
ax.plot(x,f(a)+m*(x-a))
ax.plot(a,f(a),'bo')
ax.plot(b,f(b),'bo')

# label secant line with slope
plt.annotate("secant slope = %.3f"%((f(b)-f(a))/(b-a)),(a+.5*(b-a),f(a)+.5*(f(b)-f(a))))