import matplotlib.pyplot as plt
import numpy as np
def lorenz(x,y,z):
	sigma=  10.0
	ro=  28.0
	beta=	8/3

	f1= sigma*(y-x)
	f2= x*(ro-z)-y
	f3= x*y- beta*z

	return f1,f2,f3

#this function returns the solution of cde at netxt time step
def rk2(x,y,z):
	delta_t= 0.001
	xx,yy,zz= lorenz(x,y,z)

	k1x= delta_t*xx
	k1y= delta_t*yy
	k1z= delta_t*zz

	xx_,yy_,zz_= lorenz(x+k1x/2,y+k1y/2,z+k1z/2)
	k2x= delta_t*xx_
	k2y= delta_t*yy_
	k2z= delta_t*zz_

	x_= x+k2x
	y_= y+k2y
	z_= z+k2z

	return x_,y_,z_

x_0, y_0, z_0= 1,1,1
xyz= []
temp= rk2(x_0,y_0,z_0)
xyz.append(temp)
for i in range(10000):
	x_,y_,z_= xyz[-1]
	temp= rk2(x_,y_,z_)
	xyz.append(temp)

xyz= np.array(xyz)
X= xyz[:,0]
Y= xyz[:,1]
Z= xyz[:,2]

plt.plot(X)
plt.show()
