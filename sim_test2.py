from scipy.integrate import odeint
from pylab import *

R = 1800.0
R10 = 1800.0
C = float(100.0*(10**(-9))); #100nF
t = arange(0, 0.05, 0.00001)

def RealChua(inv,t):
    x = float(inv[0]); #v_1
    y = float(inv[1]); #v_2
    z = float(inv[2]); #i_L

    C1  = float(10*10**(-9));   #10nF
    C2  = float(100*10**(-9));  #100nF
    # R = 1800;           #1.8k Ohms
    G = 1/float(R);

    #Chua Diode*************************************
    R1 = float(220);
    R2 = float(220);
    R3 = float(2200);
    R4 = float(22000);
    R5 = float(22000);
    R6 = float(3300);

    Esat = float(9); #9V batteries
    E1 = R3/(R2+R3)*Esat;
    E2 = R6/(R5+R6)*Esat;

    m12 = -1/R6;
    m02 = 1/R4;
    m01 = 1/R1;
    m11 = -1/R3;

    m1 = m12+m11;

    if(E1>E2):
        m0 = m11 + m02;
    else:
        m0 = m12 + m01;

    mm1 = m01 + m02;
    Emax = max(E1,E2);
    Emin = min(E1,E2);


    if abs(x) < Emin:
        g = x*m1;
    elif abs(x) < Emax:
        g = x*m0;
        if x > 0:
            g = g + Emin*(m1-m0);
        else:
            g = g + Emin*(m0-m1);
    elif abs(x) >= Emax:
        g = x*mm1;
        if x > 0:
            g = g + Emax*(m0-mm1) + Emin*(m1-m0);
        else:
            g = g + Emax*(mm1-m0) +  Emin*(m0-m1);

    #end Chua Diode*************************************

    #Gyrator*********************************
    R7  = float(100);  #100 Ohms
    R8  = float(1000); #1k Ohms
    R9  = float(1000); #1k Ohms
    # R10 = 1800;
    # C   = 100*10^(-9); #100nF
    L = R7*R9*C*R10/R8; #18mH

    print "L = %f" % (L)

    #end Gyrator******************************

    # Chua's Circuit Equations
    xdot = (1/C1)*(G*(y-x)-g);
    ydot = (1/C2)*(G*(x-y)+z);
    zdot  = -(1/L)*y;

    print ("R = %f, R1 = %f, R2 = %f, R3 = %f, R4 = %f, R5 = %f, R6 = %f" % (R,R1,R2,R3,R4,R5,R6))
    print "R7 = %f, R8 = %f, R9 = %f, R10 = %f, C = %f, C1 = %f, C2 = %f, L = %f" % (R7,R8,R9,R10,C,C1,C2,L)

    return [xdot,ydot,zdot];

def plotChua():
    # state = odeint(RealChua, [-0.5,-0.2,0], arange(0,0.05,0.01))
    # state = odeint(chua, [0.7, 0, 0], arange(0, 100, 0.1))
    state = odeint(RealChua, [-0.5, -0.2, 0], t)
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

    return state
