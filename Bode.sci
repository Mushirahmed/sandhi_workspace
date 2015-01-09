num = 6.87191;
m = 1;
c = 3.30579;
r = 11.6572;

s=%s;
tf = (num/((m*s^2) + (c*s) + r));
tf2 = syslin('c',tf);
bode(tf2,0.01,100);
b = 2;
