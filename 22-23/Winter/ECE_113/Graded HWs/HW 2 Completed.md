## ECE 113 Hw 1



#### 1\. Determine 

the even and odd parts of the following signals:

a) $x_1[n]=u[n-3]$

b) $x_2[n]=\alpha^nu[n-1]$

c) $x_3[n]=n\alpha^nu[n+1]$

d) $x_4[n]=\alpha^{|n|}$

**Answer**

General Formula: 
$x_e[n]=\frac{x[n]+x[-n]}2$
$x_o[n]=\frac{x[n]-x[-n]}2$

**a)** $x_1[n]=u[n-3]$

$x_e[n]=\frac{u[n-3]+u[(-n)-3]}2$
$x_e[n]=\frac{u[n-3]+u[-n-3]}2$

$x_e[n]=\begin{cases}0&-3<n<3\\0.5&else\end{cases}$


$x_o[n]=\frac{u[n-3]-u[(-n)-3]}2$
$x_o[n]=\frac{u[n-3]-u[-n-3]}2$

$x_o[n]=\begin{cases}-0.5&n<-3\\0&-3\leq n \leq 3\\0.5& n>3\end{cases}$

**b)** $x_2[n]=\alpha^nu[n-1]$

$x_e[n]=\frac{\alpha^nu[n-1]+\alpha^{-n}u[(-n)-1]}2$
$x_e[n]=\frac{\alpha^nu[n-1]+\alpha^{-n}u[-n-1]}2$

$x_e[n]=\begin{cases}\alpha^{-n}&n<-1\\0&-1\leq n \leq 1\\\alpha^n&n>1\end{cases}$

$x_o[n]=\frac{\alpha^nu[n-1]-\alpha^{-n}u[(-n)-1]}2$
$x_o[n]=\frac{\alpha^nu[n-1]-\alpha^{-n}u[-n-1]}2$

$x_o[n]=\begin{cases}-\alpha^{-n}&n<-1\\0&-1\leq n \leq 1\\\alpha^{n}&n>1\end{cases}$

**c)** $x_3[n]=n\alpha^nu[n+1]$

$x_e[n]=\frac{n\alpha^nu[n+1]+(-n)\alpha^{-n}u[(-n)+1]}2$
$x_e[n]=\frac{n\alpha^nu[n+1]-n\alpha^{-n}u[-n+1]}2$

$x_e[n]=\begin{cases}-n\alpha^{-n}&n<-1\\n\alpha^n-n\alpha^{-n}&-1\leq n \leq 1\\n\alpha^n&n>1\end{cases}$

$x_o[n]=\frac{n\alpha^nu[n+1]-(-n)\alpha^{-n}u[(-n)+1]}2$
$x_o[n]=\frac{n\alpha^nu[n+1]+n\alpha^{-n}u[-n+1]}2$

$x_o[n]=\begin{cases}n\alpha^{-n}&n<-1\\n\alpha^n+n\alpha^{-n}&-1\leq n \leq 1\\n\alpha^n&n>1\end{cases}$

**d)** $x_4[n]=\alpha^{|n|}$

$x_e[n]=\frac{\alpha^{|n|}+\alpha^{|(-n)|}}2$
$x_e[n]=\frac{\alpha^{|n|}+\alpha^{|n|}}2$
$x_e[n]=\alpha^{|n|}$

$x_o[n]=\frac{\alpha^{|n|}-\alpha^{|(-n)|}}2$
$x_o[n]=\frac{\alpha^{|n|}-\alpha^{|n|}}2$
$x_o[n]=0$

#### 2\. True or False

a) A power sequence is necessarily an energy sequence.

b) Every energy sequence has zero average power.

c) If $x[n]$ is an energy sequence, then $x[n]\to0$ as $n\to\infty$

d) There does not exist a sequence with infinite average power.


**Answer**

a) False. A power sequence cannot be an energy sequence, since the energy of a power sequence is infinite. Ex a simple sinusoid:
$x[n]=sin(\frac{\pi}2 n)$ is a power sequence, with Power = $\frac1{N-1}\sum\limits_{n=0}^{n=N}(\sin(\frac{\pi}2 n))^2 = \frac12$ , Energy= $\sum\limits_{n=0}^{n=N}(\sin(\frac{\pi}2 n))^2 =\infty$.

b) True. Since the energy of the sequence is finite, the power has to be $\frac1{T_0}E$ therefore making it zero.

c) True. If a sequence does not converge to zero, then the sum of the squares of the sequence will be infinite, making it a non-energy sequence.

d) False. A sequence with infinite average power would be possible. Ex: ReLU. $\lim\limits_{m\to \infty}\frac1{2m+1}\sum\limits_{n=-m}^{n=m}(n)^2=\infty$



#### 3\. System Stability
$I$ is defined by $y[n] = \ln(|x[n-1|)$ and $II$ is defined by $y[n] = e^{x[2n]}$. Which of the following statements is true?

a) Both systems are BIBO stable.

b) Both systems are BIBO unstable.

c) System $I$ is BIBO unstable and system $II$ is BIBO stable.

d) Both systems are time-invariant.


**Answer**

For $I$, If $|x[n]|<B$, then $|y[n]|=\ln(B)$ is not bounded, for all B, since at $B\to 0$, $y[n]\to -\infty$. Therefore, $I$ is not BIBO stable. 

For $II$, if $|x[n]|<B$, then $|y[n]|<e^B$ is bounded, for all B. As long as not $B\to \infty$, $y[n]$ is bounded. Therefore, $II$ is BIBO stable.

**a)** False. $I$ is not BIBO stable.

**b)** False. $II$ is BIBO stable.

**c)** True. $I$ is not BIBO stable and $II$ is BIBO stable.

$I$. $y[n] = \ln(|x[n-1|)$
Let input be $z[n]$, therefore output is $y[n] = \ln(|z[n-1|)$.
For Delayed input $z[n-1]$, output is $\ln(|z[n-2|)$.

For Delayed output $y[n-1] = \ln(|z[n-2|)$
Therefore delayed input = delayed output, Therefore it is time-invariant.

$II$. $y[n] = e^{x[2n]}$.
Let input be $z[n]$, therefore output is $y[n] = e^{z[2n]}$.

For Delayed input $z[n-1]$, output is $e^{z[2(n-1)]}$.

For Delayed output $y[n-1] = e^{z[2n-1]}$.

Therefore delayed input $\neq$ delayed output, Therefore it is not time-invariant.

**d)** False. $I$ is time-invariant and $II$ is not time-invariant.




#### 4\. Determine
whether each of the following systems is linear or not, time-invariant or not, and BIBO stable or not, relaxed or not.

a) $y[n] = ln(|x[n]| + 1)$

b) $y[n] = y[n-1] + x[n]$, $\;y[-1]=0$

c) $y[n] = y[n-1] + x[n]$, $\;y[-1]=1$

d) $y[n] = 2 + x[n]$


**Answer**

a)
$y[n] = ln(|x[n]| + 1)$

Linearity:
Applying input $a\cdot x_1[n] + b\cdot x_2[n]$, output is $a\cdot \ln(|x_1[n]| + 1) + b\cdot \ln(|x_2[n]| + 1)$, $=a\cdot y[x_1[n]] + b\cdot y[x_2[n]]$, therefore it is linear.

Time-invariance:
Let input be $z[n]$, therefore output is $y[n] = \ln(|z[n]| + 1)$.
For Delayed input $z[n-1]$, output is $\ln(|z[n-1]| + 1)$.
For Delayed output $y[n-1] = \ln(|z[n-1]| + 1)$.
Therefore delayed input = delayed output, Therefore it is time-invariant.

Causality:
$y[n] = \ln(|x[n]| + 1)$, since it does not depend on future values of $x[n]$, it is causal.

BIBO Stability:
If $|x[n]|<B$, then $|y[n]|<\ln(B+1)$ is bounded, for all B. As long as not $B\to \infty$, $y[n]$ is bounded. Since the +1 term is in the input, it does not $\to \infty$ as $|x[n]|$ $\to 0$. Therefore, it is BIBO stable. 

Relaxed:
At $t_0$, $y[n] = ln(|0|+1) = 0$, therefore it is relaxed system.


**a)** Linear, Time-invariant, BIBO stable, relaxed.

b)
$y[n] = y[n-1] + x[n]$, $\;y[-1]=0$

Linearity:
$y[n] = y[n-1] + x[n]$, we can rewrite it as $y[n] = \sum\limits_{k=0}^{n}x[k]$, therefore it is linear.
Applying input $a\cdot x_1[n] + b\cdot x_2[n]$, output is $a\cdot y[n-1] + a\cdot x[n] + b\cdot y[n-1] + b\cdot x[n]$, $=a\cdot y[x_1[n]] + b\cdot y[x_2[n]]$, therefore it is linear.

Time-invariance:
Let input be $z[n]$, therefore output is $y[n] = y[n-1] + z[n]$.
For Delayed input $z[n-1]$, output is $y[n-2] + z[n-1]$. This happens because when the the input is delayed, the output which starts at $y[0]$ remains the same until the input is delayed.
For Delayed output $y[n-1] = y[n-2] + z[n-1]$.
Therefore delayed input = delayed output, Therefore it is time-invariant.

Causality:
$y[n] = y[n-1] + x[n]$. Although it depends on past values of y[n], it does not depend on future values of x[n] or y[n], therefore it is causal.

BIBO Stability:
$y[n] = y[n-1] + x[n]$, we can rewrite it as $y[n] = \sum\limits_{k=0}^{n}x[k]$.
$y[n]$ is an accumulator. Even if $|x[n]|<B$, $|y[n]|$ is not bounded. Ex: $\ln(n+1)$ as an input, $y[n]$ will accumulate to $\infty$. Therefore, it is not BIBO stable.

Relaxed:
At $t_0$, $y[n]$ is not necessarily 0, since it is an accumulator. Even if $x[t_0]$ is 0, $y[n]$ when $n>t_0$ retains the value of $y[n-1]$, which is not necessarily 0. Therefore, it is not relaxed system. 

**b)** Linear, Time-invariant, Causal, NOT BIBO stable, not relaxed.

c)
$y[n] = y[n-1] + x[n]$, $\;y[-1]=1$


Linearity:
Applying input $a\cdot x_1[n] + b\cdot x_2[n]$, output is $a\cdot y[n-1] + a\cdot x[n] + b\cdot y[n-1] + b\cdot x[n]$, $=a\cdot y[x_1[n]] + b\cdot y[x_1[n]]$, therefore it is linear.

Time-invariance:
Let input be $z[n]$, therefore output is $y[n] = y[n-1] + z[n]$.
For Delayed input $z[n-1]$, output is $y[n-2] + z[n-1]$. This happens because when the the input is delayed, the output which starts at $y[0]$ remains the same until the input is delayed.
For Delayed output $y[n-1] = y[n-2] + z[n-1]$.
Therefore delayed input = delayed output, Therefore it is time-invariant.

Causality:
$y[n] = y[n-1] + x[n]$. Although it depends on past values of y[n], it does not depend on future values of x[n] or y[n], therefore it is causal.

BIBO Stability:
$y[n] = y[n-1] + x[n]$, we can rewrite it as $y[n] = 1 + \sum\limits_{k=0}^{n}x[k]$.
$y[n]$ is an accumulator. Even if $|x[n]|<B$, $|y[n]|$ is not bounded. Ex: $\ln(n+1)$ as an input, $y[n]$ will accumulate to $\infty$. Therefore, it is not BIBO stable.

Relaxed:
At $t_0$, $y[n]$ is not necessarily 0, since it is an accumulator. Even if $x[t_0]$ is 0, $y[n]$ when $n>t_0$ retains the value of $y[n-1]$, which is not necessarily 0. Therefore, it is not relaxed system.

**c)** Linear, Time-invariant, Causal, not BIBO stable, not relaxed.

d)
$y[n] = 2 + x[n]$

Linearity:
Applying input $a\cdot x_1[n] + b\cdot x_2[n]$, output is $2a + a\cdot x[n] + 2b + b\cdot x[n]$, $=a\cdot y[x_1[n]] + b\cdot y[x_2[n]]$, therefore it is linear.


Time-invariance:
Let input be $z[n]$, therefore output is $y[n] = 2 + z[n]$.
For Delayed input $z[n-1]$, output is $2 + z[n-1]$.
For Delayed output $y[n-1] = 2 + z[n-1]$.
Therefore delayed input = delayed output, Therefore it is time-invariant.

Causality:
$y[n] = 2 + x[n]$. Since it does not depend on past values of x[n], it is causal.

BIBO Stability:
If $|x[n]|<B$, then $|y[n]|$ is bounded, for all B. As long as not $B\to \infty$, $y[n]$ is bounded. Therefore, it is BIBO stable.

Relaxed:
At $t_0$, $y[n] = 2 + 0 = 2$, therefore it is not relaxed system.

**d)** Linear, Time-invariant, Causal, BIBO stable, not relaxed.



#### 5\. Determine
The conditions on the parameters of the following systems for stability:

a) $h[n] = \alpha^nu[-n]$

b) $h[n] = \alpha^n(u[n]-u[n-100])$

c) $h[n] = r^n\sin[n\omega_0]u[n]$

d) $h[n] = $\alpha^{|n|}$

e) $h[n] = K(-1)^nu[n]$


**Answers**

a) 
$h[n] = \begin{cases} \alpha^n, & n\leq 0 \\ 0, & n>0 \end{cases}$
For stability, $|h[n]|$ must be bounded, for all n.
We know that it is bounded for $n\geq 0$, but for it to be bounded for all n, it must be bounded for $n\leq 0$: $\alpha^n<B$, for $n\leq0$.
Thus condition for stability is that $|\alpha|\geq1$.

b)
$h[n] = \begin{cases} \alpha^n, & 0\leq n\leq 100 \\ 0, & else \end{cases}$
For stability, $|h[n]|$ must be bounded, for all n.
Since it is bounded for $0\geq n$ and $n\geq 100$, we need to make sure it is bounded for $0\leq n\leq 100$: $\alpha^n<B$, for $0\leq n\leq 100$. If $\alpha\geq1$, then $|h[n]|=\alpha^{100}$ else $|h[n]|=\alpha^0$, since both are bounded for any $\alpha$, it is stable.
Thus condition for stability is that $\alpha$ is bounded.

c)
$h[n] = \begin{cases} r^n\sin[n\omega_0], & n\geq 0 \\ 0, & else \end{cases}$
For stability, $|h[n]|$ must be bounded, for all n.
Let $h[n] = k[n]l[n]$, such that $k[n] = r^n$ and $l[n] = \sin[n\omega_0]$. Therefore, $|h[n]| = |k[n]|\cdot|l[n]|$. 
$|l[n]|$ = 1, since the absolute value of the max/min of a sinusoid is always the amplitude, which is 1.
Therefore $|h[n]| = |k[n]|$, which is bounded for r<1, since the exponent is only active for n>0, thus it needs to be bounded for n>0 which is true for |r|<1.
Thus condition for stability is $|r|<1$.

d) 
$h[n] = \begin{cases} \alpha^{n}, & n\geq 0 \\ \alpha^{-n}, & n<0 \end{cases}$ Thus $|h[n]| = |\alpha^{n}|$ for n>0, since $\alpha$ never takes a negative exponent. Therefore $\alpha<1$ makes $|h[n]|$ bounded for all n.
Thus condition for stability is $|\alpha|<1$.