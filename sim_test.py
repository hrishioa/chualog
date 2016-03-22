from scipy.integrate import odeint
from pylab import *
import sim

def chua(inv, t):

    x = inv[0];
    y = inv[1];
    z = inv[2];

    alpha  = 15.6;
    beta   = 28;
    m0     = -1.143;
    m1     = -0.714;

    h = m1*x+0.5*(m0-m1)*(abs(x+1)-abs(x-1));

    xdot = alpha*(y-x-h);
    ydot = x - y+ z;
    zdot  = -beta*y;

    return [xdot,ydot,zdot]

def Lorenz(state,t):
  # unpack the state vector
  x = state[0]
  y = state[1]
  z = state[2]

  # these are our constants
  sigma = 10.0
  rho = 28.0
  beta = 8.0/3.0

  # compute state derivatives
  xd = sigma * (y-x)
  yd = (rho-z)*x - y
  zd = x*y - beta*z

  # return the state derivatives
  return [xd, yd, zd]

state0 = [-4, -1.5, 1]
# t = arange(0.0, 30.0, 0.01)
t = arange(0,0.05,0.000001)

while(True):
    sim.R = input("Enter a value for R:")
    sim.R10 = input("Enter a value for R10:")

    state = odeint(sim.RealChua, [0.7,1,1], arange(0,100,0.1))
    # state = odeint(chua, [0.7, 0, 0], arange(0, 100, 0.1))

    # state = odeint(Lorenz, state0, t)

    # do some fancy 3D plotting
    from mpl_toolkits.mplot3d import Axes3D
    fig = figure()
    ax = fig.gca(projection='3d')
    ax.plot(state[:,0],state[:,1],state[:,2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    show()
