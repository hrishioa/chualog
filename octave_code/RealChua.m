%----------RealChua.m----------
function out = RealChua(t,in)

x = in(1); %v_1
y = in(2); %v_2
z = in(3); %i_L



C1  = 10*10^(-9);   %10nF
C2  = 100*10^(-9);  %100nF
R = 1800;           %1.8k Ohms
G = 1/R;

%Chua Diode*************************************
R1 = 220;
R2 = 220;
R3 = 2200;
R4 = 22000;
R5 = 22000;
R6 = 3300;

Esat = 9; %9V batteries
E1 = R3/(R2+R3)*Esat;
E2 = R6/(R5+R6)*Esat;

m12 = -1/R6;
m02 = 1/R4;
m01 = 1/R1;
m11 = -1/R3;

m1 = m12+m11;

if(E1>E2)
m0 = m11 + m02;
else
m0 = m12 + m01;   
end

mm1 = m01 + m02;
Emax = max([E1 E2]);
Emin = min([E1 E2]);


if abs(x) < Emin
   g = x*m1;     
elseif abs(x) < Emax 
    g = x*m0;
    if x > 0
    g = g + Emin*(m1-m0);    
    else
    g = g + Emin*(m0-m1);  
    end
    
elseif abs(x) >= Emax
    g = x*mm1;    
    if x > 0
        g = g + Emax*(m0-mm1) + Emin*(m1-m0);
    else
        g = g + Emax*(mm1-m0) +  Emin*(m0-m1);
    end
end

%end Chua Diode*************************************

%Gyrator*********************************
R7  = 100;  %100 Ohms
R8  = 1000; %1k Ohms
R9  = 1000; %1k Ohms
R10 = 1800;
C   = 100*10^(-9); %100nF
L = R7*R9*C*R10/R8; %18mH 

%end Gyrator******************************

% Chua's Circuit Equations
xdot = (1/C1)*(G*(y-x)-g);
ydot = (1/C2)*(G*(x-y)+z);
zdot  = -(1/L)*y;

out = [xdot ydot zdot]';
