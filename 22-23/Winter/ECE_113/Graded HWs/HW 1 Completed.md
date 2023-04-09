
## ECE 113 Hw 1

#### 1\. Given
$x[n]=\{2,0,-1,6,-3,2,0\}, \; -3 \le n \le 3$
$y[n]=\{8,2,-7,-2,0,1,1\}, \; -5 \le n \le 1$
$w[n]=\{3,6,-1,2,6,6,1\}, \; -2 \le n \le 4$
<br>
  
Find:
a) $c[n]=x[n+3]$
b) $d[n]=y[n-2]$
c) $e[n]=x[-n]$
d) $u[n]=x[n-3]+y[n+3]$
e) $v[n]=y[n-3]\cdot w[n+2]$
f) $s[n]=y[n+4]-w[n-3]$
g) $r[n]=3.9w[n]$

**Answer**
a) $c[n]=\{2,0,-1,6,-3,2,0\}, \; -6 \le n \le 0$
b) $d[n]=\{8,2,-7,-2,0,1,1\}, \; -3 \le n \le 3$
c) $e[n]=\{0,2,-3,6,-1,0,2\}, \; -3 \le n \le 3$
d) $u[n]=\{8,2,-7,-3,0,1,1,0,2,0,-1,6,-3,2,0\}, \; -8 \le n \le 6$
e) $v[n] = \{-8,4,-42,-18,0\}, \; -2 \le n \le 2$
f) $s[n] = \{8,2,-9,-3,0,1,1,0,0,0,-3,-6,1,-2,-6,-6,-1\}, \; -9 \le n \le 7$
g) $r[n] = \{11.7, 23.4, -3.9, 7.8, 23.4, 23.4, 3.9\}, \; -2 \le n \le 4$
  

#### 2\. Determine
The fundamental period of the sinusoidal sequence $x[n] = A\sin(\omega_0n)$ for the following values the angular frequency $\omega_0$:
a) $0.3\pi$
b) $0.48\pi$
c) $0.45\pi$
d) $0.525\pi$
e) $0.7\pi$
f) $0.75\pi$
  
**Answer**

a) If the sinosuid has a fundametal frequency $F_0$,
$A\sin (0.3\pi n) = A\sin(2\pi F_0 n) =A\sin(2\pi\frac{0.3}{2}n)$,
$\therefore F_0 =\frac{0.3}2=\frac{3}{20}$
$N=\frac{k}{f}=\frac{20}3\cdot k=20,$ for $k=3$, since $k\in \R$
$\therefore N=20$

b) If the sinosuid has a fundametal frequency $F_0$,
$A\sin (0.48\pi n) = A\sin(2\pi F_0 n) =A\sin(2\pi\frac{0.48}{2}n)$,
$\therefore F_0 =\frac{0.48}2=\frac{6}{25}$
$N=\frac{k}{f}=\frac{25}6\cdot k=20,$ for $k=6$
$\therefore N=25$

c) If the sinosuid has a fundametal frequency $F_0$,
$A\sin (0.45\pi n) = A\sin(2\pi F_0 n) =A\sin(2\pi\frac{0.45}{2}n)$,
$\therefore F_0 =\frac{0.45}2=\frac{9}{40}$
$N=\frac{k}{f}=\frac{40}9\cdot k=20,$ for $k=9$
$\therefore N=40$

d) If the sinosuid has a fundametal frequency $F_0$,
$A\sin (0.525\pi n) = A\sin(2\pi F_0 n) =A\sin(2\pi\frac{0.525}{2}n)$,
$\therefore F_0 =\frac{0.525}2=\frac{21}{80}$
$N=\frac{k}{f}=\frac{80}{21}\cdot k=80,$ for $k=21$
$\therefore N=80$

e) If the sinosuid has a fundametal frequency $F_0$,
$A\sin (0.7\pi n) = A\sin(2\pi F_0 n) =A\sin(2\pi\frac{0.7}{2}n)$,
$\therefore F_0 =\frac{0.7}2=\frac{7}{20}$
$N=\frac{k}{f}=\frac{20}7\cdot k=20,$ for $k=7$
$\therefore N=20$

f) If the sinosuid has a fundametal frequency $F_0$,
$A\sin (0.75\pi n) = A\sin(2\pi F_0 n) =A\sin(2\pi\frac{0.75}{2}n)$,
$\therefore F_0 =\frac{0.75}2=\frac{3}{8}$
$N=\frac{k}{f}=\frac{4}8\cdot k=8,$ for $k=3$
$\therefore N=8$

  

#### 3\. Determine
The fundamental period of the following periodic sequences:
a) $x_a[n] = e^{j 0.25\pi n}$
b) $x_b[n] = cos(0.6\pi n + 0.3\pi)$
c) $x_c[n] = \Re(e^{j \pi n/8}) + \Im(e^{j\pi n/5})$
d) $x_d[n]=6\sin(0.15\pi n) -\cos(0.12\pi n + 0.1\pi)$
e) $x_e[n]=\sin(0.1\pi n + 0.75\pi)-3\cos(0.8\pi n + 0.2\pi) + \cos(1.3\pi n)$

**Answer**
a) $0.25\pi=2\pi f$
$f=\frac{0.25}2=\frac18$
$N=\frac kf = \frac81\cdot k=8$, for $k=1$
$\therefore N=8$

b) $0.6\pi=2\pi f$
$f=\frac{0.6}2=\frac3{10}$
$N=\frac kf = \frac{10}3\cdot k=10$, for $k=3$
$\therefore N=10$

c) $Re(e^{j \pi n/8}) + \Im(e^{j\pi n/5}) = \cos(\pi n/8) + \sin(\pi n/5)$
$\frac{1}{8}\pi=2\pi f_1$
$f_1=\frac{1}{8\cdot2}=\frac1{16}$
$N_1=\frac {k_1}{f_1} = \frac{16}k_1\cdot k={16}$, for $k=1$
$\frac{1}{5}\pi=2\pi f_2$
$f_2=\frac{1}{5\cdot2}=\frac1{10}$
$N_2=\frac {k_2}{f_2} = \frac{10}k_2\cdot k={10}$, for $k=1$
$\therefore N=LCM(16,10)=80$

d) $6\sin(0.15\pi n) -\cos(0.12\pi n + 0.1\pi) = 6\sin(\frac{3}{20}\pi n) -\cos(\frac{3}{25}\pi n + \frac{3}{40}\pi)$
$\frac{3}{20}\pi=2\pi f_1$
$f_1=\frac{3}{20\cdot2}=\frac{3}{40}$
$N_1=\frac {k_1}{f_1} = \frac{40}{3}k_1=40$, for $k=3$
$\frac{3}{25}\pi=2\pi f_2$
$f_2=\frac{3}{25\cdot2}=\frac{3}{50}$
$N_2=\frac {k_2}{f_2} = \frac{50}{3}k_2=50$, for $k=3$
$\therefore N=LCM(40,50)=200$

e) $\sin(0.1\pi n + 0.75\pi)-3\cos(0.8\pi n + 0.2\pi) + \cos(1.3\pi n) = \sin(\frac{1}{10}\pi n + \frac{3}{4}\pi)-3\cos(\frac{4}{5}\pi n + \frac{2}{10}\pi) + \cos(\frac{13}{10}\pi n)$
$\frac{1}{10}\pi=2\pi f_1$
$f_1=\frac{1}{10\cdot2}=\frac{1}{20}$
$N_1=\frac {k_1}{f_1} = \frac{20}{1}k_1=20$, for $k=1$
$\frac{4}{5}\pi=2\pi f_2$
$f_2=\frac{4}{5\cdot2}=\frac{2}{5}$
$N_2=\frac {k_2}{f_2} = \frac{5}{2}k_2=5$, for $k=2$
$\frac{13}{10}\pi=2\pi f_3$
$f_3=\frac{13}{10\cdot2}=\frac{13}{20}$
$N_3=\frac {k_3}{f_3} = \frac{20}{13}k_3=20$, for $k=13$
$\therefore N=LCM(20,5,20)=20$

#### 4. Assume
$x[n]$ has a period $N$. Are the following periodic?
i) $x[1-2n]$
ii)$x[n]+(-1)^nx[0]$

**Answer**
i) If $x[n]$ is periodic with period $N$, then $x[n]=x[n+N]$
Let $y[n]=x[1-2n]$
$\therefore x[2n]=x[2(n+N)]\qquad x[-2n]=x[-2(n+N)]\qquad x[-2n+1]=x[1-2(n+N)]\qquad y[n]=x[1-2(n+N)] \qquad y[n]=y[n+\frac12N]$
$\therefore x[1-2n]$ is periodic with a period of $LCM(\frac12N,1)=1$
The $\frac12N$ accounts for the $\frac12N$ and the 1 accounts for the discrete nature of the new signal which cannot have a fractional period. In simpler English, x[1-2n] is periodic and if the period $N$ is odd, the period will remain $N$ otherwise it will be $2N$.

ii) If $x[n]$ is periodic with period N, then $x[n]=x[n+N]$
Let $y[n]=(-1)^nx(0)$, and let $z[n]=x[n]+y[n]$
From the problem, we know that $x[n]$ has a period $N$.
To find the period of $y[n]$ we need to find an $N_y$ such that $y[n]=y[n+N_y]$.
Solving $(-1)^Nx[0]=(-1)^{n+N_y}x[0],\quad (-1)^N-(-1)^{n+N_y}=0$
$\therefore(-1)^n((-1)^{N_y}-1)=0,\quad(-1)^{N_y}=1$
$\therefore N_y=2$
$\therefore$ The period of $N_z=LCM(N_x,N_y)=LCM(N,2)$
It is periodic with period $LCM(N,2)$	