%----------StartRealChua.m----------
%[t,y] = ode45(@RealChua,[0 0.05],[-0.5 -0.2 0]);
[t,y] = lsode("RealChua", [-0.5 -0.2 0], (t=linspace(0,0.001,0.05)')); 
plot3(y(:,1),y(:,2),y(:,3))
grid
