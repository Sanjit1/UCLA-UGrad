### Basic Signal Stuff
**Definition**: Even Signals: $x(t) = x(-t)$. Think $x^2$, Odd Signals: $x(t) = -x(-t)$. Think
**Decomposition**: For $x(t)$, $x_e(t) = \frac{1}{2}\cdot(x(t) + x(-t))$, $x_o(t) = \frac{1}{2}\cdot(x(t) - x(-t))$
For $x(t)$, $\quad$Amplitude Scaling: $ax(t)$, $\quad$ Time Scaling: $x(at)$ $\quad$Time Shift: $x(t-t_1)$
**Combining Operations**: SADMEP or Expand (), Perform shifts, Scale with respect to origin.
**Energy**: $E_x = \lim\limits_{t \to \infin}{\int_{-T}^{T}|x(t)|^2\,dt}\qquad$**Power**: $P_x = \lim\limits_{t \to \infin}{\frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt}$
### Periodic Signals
For $x(t) = x_1(t) + x_2(t)$, $T = LCM(T_1, T_2)$, Given integer multiple
$\frac{d}{dx}\sin(x) = \cos(x),\qquad\sin(\theta)=\cos(\theta-\frac{\pi}{2})\qquad$ $\omega_0=2\pi f = \frac{2\pi}{T_0}$
### Complex Signals
For $z(t) = x(t) + jy(t)$: We have Re(z) and Im(z) $\qquad$**Eulers**: $\quad e^{j\pi}+1=0$
For  $z=re^{j\phi}$:$\qquad$ r: Magnitude/Modulus$\qquad\phi$: Angle 
$re^{j\phi} = r\cos{\phi} +rj\sin{\phi}$
**Conversion:** $\quad x=r\cos\phi\qquad$$y=r\sin\phi\qquad$ $r=\sqrt{x^2+y^2}\qquad$ $\phi=tan^{-1}(\frac{y}{x})$
**Complex Conjugate**: For $z=x+jy$
$z^*=x-jy$ $\qquad|z|^2=zz^*$ $\qquad-j=\frac{1}{j}$
$\cos{\theta}=\frac{1}{2}(e^{j\theta}+e^{-j\theta})$ $\qquad\sin{\theta}=\frac{1}{2j}(e^{j\theta}-e^{-j\theta})$ *watch the j!
$j=e^{j\frac{\pi}2}\qquad -j=e^{-j\frac{\pi}2}\qquad 1=e^{j(0)}\qquad -1=e^{j\pi}$
### Elementary Signals
**Complex Sinusoid**: (complex part drawn with dotted lines)
$Ae^{j(\omega t+\theta)} = A\cos(\omega t + \theta) + jA\sin(\omega t+\theta), \qquad$ Dampening and Growing sinusoid: $e^{\sigma t}\cos(\omega t + \theta)$, If $\sigma>0$ growing else dampening. 

Common Signals:
**Heavyside**: $u(t) = \begin{cases} 1 \quad t \ge 0 \\ 0 \quad \text{else} \end{cases}$
**Rectangle**: $rect(t) = \begin{cases} 1 \quad |t| \le \frac{1}{2} \\ 0 \quad \text{else} \end{cases}\quad$ and $\qquad rect_{\Delta}(t) = \begin{cases} \frac{1}{\Delta} \quad |t| \le \frac{\Delta}{2} \\ 0 \quad \text{else} \end{cases}$
**Ramp**: $r(t) = \begin{cases} t \quad t \ge 0 \\ 0 \quad \text{else} \end{cases} = \int u(t)\,dt\qquad$ and $\qquad$ **Triangle**: $\Delta(t)=\begin{cases} 1-|t| \quad |t| \le 1 \\ 0 \quad \text{else} \end{cases}$
**Impulse**: $\delta(t)=\lim\limits_{t \to 0}{rect_\Delta(t)} = \frac{d}{dt}u(t)$
**Sinc**: $sinc(t)=\frac{\sin(\pi t)}{\pi t}$
**Impulse Properties**:
$x(t)\cdot\delta(t)=x(0)\cdot\delta(t)$
$x(t)\cdot\delta(t-T)=x(T)\cdot\delta(t)$: i.e. only the sample of x(T) at time T and 0 else
$\int_{-\infin}^{\infin}x(t)\cdot\delta(t-T)\;dt=x(T)$
**Impulse Response**: $h(t) = H[\delta(t)]$

### LTI, Causality, Stability and Memory
**Causal Signals**: $x(t)$, where $t\ge0$,$\quad$ **Noncausal Signals**: $x(t)$, where $t\lt0$,$\quad$**Anticausal Signals**: $x(t)$, where $t\le0$: Backwards
**BIBO**: Prove that for a bounded input: M<sub>x</sub> there is a bounded output M<sub>y</sub>. $\int_{-\infin}^{\infin}{x(t)dt}$
**Causal**: (Note this is for systems and not signals): Show that the signal does not require future values from the input.
**Time invariance**: Show that delayed input = delayed output.
**Linearity**: Show Homogeneity and Superposition. 
**Homogeneity**: $S(ax) = aS(x)\quad$ and $\quad$**Superposition**: $S(x+ x_0) = S(x) + S(x_0)$
**Combine and check**: $S(ax + bx_0) = aS(x) + bS(x_0)$
**Memory**: It has memory if it requires past or future values.
**Invertibility**: If input can be recovered from output.
**Extended Linearity**: Just means that linearity of a sum/integral holds if the function inside is linear.
### Convolution
For $y(t)=H[x(t)]$, where H is LTI system, $y(t)=H[\int_{-\infin}^{\infin}x(\tau)\delta(t-\tau)d\tau]$
= $\int_{-\infin}^\infin x(\tau)h(t-\tau)d\tau$
**For a causal LTI system**, $\int_{-\infin}^{t}x(\tau)h(t-\tau)d\tau$
**Convolving with impulse**: $x(t)\ast\delta(t-T) = x(t-T)$: This gives Identity/Delay
**Integration** using convolution: $x(t) \ast u(t) = \int_{-\infin}^{t}x(\tau)d\tau$
Rect:
$rect(\omega t)\ast rect(\omega_0t)=(\omega_0 + \omega)/2$ and $-(\omega_0 + \omega)/2$ 
![](https://lh6.googleusercontent.com/hNiXiuxCAgx1sWfnLTLw6QK8JKwOGfMO1YHsSaA06SiUZlgjMkO8nUgO7zz7qIhyws34VIcA6z4mhgms9zrXcNnQucAXQ_6a91lSJwy4YEM-iXzvxKd_e0weJtlNBXMJMMzRR0eI4nrIVLSMiVahIPIUnPlKbvEIXjZ3agT80xFo2tyNJwGm6hndqfniP28DcA)

### Fourier Series
For a well-behaved periodic signal: $f(t)$,
$f(t)=\sum\limits_{k=-\infin}^\infin{c_k}e^{jk\omega_0t}$, where c<sub>k</sub> can be given by
$c_k=\frac{1}{T}\int_\tau^{\tau+T_0}f(t)e^{-jk\omega_0t}dt$
$\int_{t_0}^{t_0+T_0}e^{jk\omega_0t}=\int_{t_0}^{t_0+T_0}cos({k\omega_0t)} + j\int_{t_0}^{t_0+T_0}sin({k\omega_0t)}$
**Complex Exponential**: $e^{jk\omega_0 t}=\cos(k\omega_0 t) + j\sin(k\omega_0 t)$
**Also**
$Re(c_k)=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f(t)\cos(k\omega_0t)dt$
$Im(c_k)=-\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f(t)\sin(k\omega_0t)dt$
**Properties**:
$Re(c_k) = Re(c_{-k})\qquad$ and $\qquad Im(c_k) = -Im(c_{-k})$
$c_k^\ast=c_{-k}\qquad$ and $\qquad |c_k|=|c_{-k}|\qquad$ and $\qquad\measuredangle c_k=-\measuredangle c_{k}^\ast$
For $f(t)$ even, $c_k=c_{-k}\qquad$ and $\qquad$For $f(t)$ odd, $-c_k=c_{-k}$
$\therefore$ $\qquad f(t)$ is even & real, $c_k$ is real $\qquad$ and $\qquad f(t)$ is odd & real, $c_k$ is imaginary

**Parsevals Theorum**:
For $x(t)$ with a fourier series,
$P=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}|x(t)|^2dt=\sum\limits_{k=-\infin}^{\infin}|c_k|^2=\sum\limits_{k=-\infin}^{\infin}c_kc_k^*$
Transform: P=$\int_{-\infty}^{\infty}|f(t)|^2=\frac1{2\pi}\int_{-\infty}^{\infty}|F(j\omega)|^2d\omega=\frac1{2\pi}\int_{-\infty}^{\infty}F^*(j\omega)F(j\omega)d\omega$
For $c_k=|c_k|e^{j\measuredangle c_k}$, We can have a Amplitude/Phase plot: ex: $\frac{3}{2}e^{2\pi jt}$.

**Eigenfunctions** of LTI:
For a system H, if $h(t)\ast x(t)=ax(t),\; x(t)$ is an eigenfunction.

For a signal $x(t) = e^{(\sigma+j\omega)t}$, $s=\sigma+j\omega$
$y(t)=\int_{-\infin}^\infin{h(\tau)e^{s(t-\tau)}}d\tau=\int_{-\infin}^\infin{h(\tau)e^{st}e^{-s\tau}}d\tau=e^{st}\int_{-\infin}^\infin{h(\tau)e^{-s\tau}}d\tau$
We have $H(s)=\int_{-\infin}^\infin{h(\tau)e^{-s\tau}}d\tau$ and $y(t) = H(s)e^{st}$ for all LTI
For a square wave which is 1 for -0.5 to 0.5,
$sinc(t) = \frac{\sin(\pi t)}{\pi t}$, also $sinc(0)=1$
$c_k=\frac{1}{2}sinc(k/2)$
### Fourier Transform
Truncated and actual $F_T(j\omega)=\int_{-\frac{T}{2}}^{\frac{T}{2}}f(t)e^{-j\omega t}dt \qquad F(j\omega)=\int_{-\infty}^{\infty}f(t)e^{-j\omega t}dt$ 
**IFT**: $f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(j\omega)e^{j\omega t}$
If you plug in t to a fourier transform $F(t) = 2\pi f(-j\omega) \qquad 2\pi f(-t)=\int_{-\infty}^{\infty}F(j\omega)e^{-j \omega t}d \omega$
Ex: $rect(t)=sinc(\omega/2\pi) \quad sinc(t/2\pi)=2\pi rect(-\omega)$
**Odd Even Real Complex**: 
$F_e(j\omega)=\int_{-\infty}^{\infty}f_e(t)\cos(\omega t)dt \qquad F_o(j\omega)=j\int_{-\infty}^{\infty}f_o(t)\sin(\omega t)dt$ 
Even and Odd duality holds:
If f(t) is real: $F(-j\omega)=\R(F(-j \omega))+j\Im(F(-j\omega))=F^*(j\omega)$ This is Hermitian
If f(t) is imag: $F(-j\omega)=\R(F(-j \omega))+j\Im(F(-j\omega))=-F^*(j\omega)$ This is Anti-Hermitian
$f^*(t)=F^*(-j \omega)$
$F[f(t-\tau)]=\int_{-\infty}^{\infty}f(t-\tau)e^{-j\omega t}dt=\int_{-\infty}^{\infty}f(u)e^{-j\omega(u+\tau)}du=e^{-j\omega\tau}\int_{-\infty}^{\infty}f(u)e^{-j\omega u}du=e^{-j\omega \tau}F(j\omega)$
**Modulations**:
$F[f(t)e^{j\omega_0 t}]=F(j(\omega -\omega_0))\qquad F[f(t)\cos(\omega_0t)]=\frac12F(j(\omega -\omega_0))+F(j(\omega+\omega_0))\qquad F[f(t)\sin(\omega_0t)]=\frac1{2j}F(j(\omega -\omega_0))-F(j(\omega+\omega_0))$
**Derivations**
**Convolution Theorum:** $\mathcal{F}[(f_1\ast f_2)(t)]= F_1(j\omega)F_2(j\omega) = \int_{-\infty}^{\infty}(\int_{-\infin}^{\infin}f_1(\tau)f_2(t-\tau)d\tau)e^{-j\omega t}dt$
$=\int_{-\infty}^{\infty}f_1(\tau)\cdot(\int_{-\infty}^{\infty}f_2(t-\tau)e^{-j\omega t}dt)d\tau=\int_{-\infin}^{\infin}f_1(\tau)[e^{-j\omega \tau}F_2(j\omega)]d\tau=F_2(j\omega)\cdot\int_{-\infty}^{\infty}f_1(\tau)e^{-j\omega t}d\tau=F_2(j\omega)F_1(j \omega)$
Also: $F[f_1(t)f_2(t)]=\frac1{2\pi}(F_1\ast F_2)(j\omega)$
**rect**: $F(j\omega)= \int_{-\infty}^{\infty}rect(t/T)e^{-j\omega t}dt =\int_{-T/2}^{T/2}e^{-j\omega t}dt=\frac{e^{-j \omega t}}{-j\omega}|^{T/2}_{-T/2}=\frac{-1}{j\omega}(e^{-j\omega T/2} - e^{-j \omega T/2})=2\sin(\omega T/2)/\omega=Tsinc(\omega T/2 \pi)$
**e^-at u(t)**: $F(j\omega)=\int^{\infty}_{-\infty}e^{-at}u(t)e^{-j \omega t}dt=\int^{\infty}_{0}e^{-at-j \omega t}dt=\frac{e^-(a+j \omega t)}{-a+j\omega}|^{\infty}_{0}=\frac{1}{a+j\omega}$
**cos**: $F[\cos(\omega_0 t)]=F[\frac12(e^{-j\omega_0 t}+e^{-j\omega_0 t})]=\frac12F(e^{j\omega_0 t})F(e^{-j\omega_0 t})= \pi(\delta(\omega-\omega_0).....)$ sin is easy: $e^{j\omega_0 t}-e^{-j\omega_0 t}$
**Integral**: Use convolution with step response as a representation for integral.
**![](https://lh4.googleusercontent.com/Z4fcnD3VOkpvZ--btq4SzLfq6orpRb5sbNg9NvQco34yLa4iVvq_8SduZ_Bdkekln7LD_NibEByDIjr7Lvk4D_MJvx8uHKBV-NeZiA1g8nz5W1mt-ACiD6h8A0aHDQkla8pSAb28YTTUYO5gs8qq-Nd9PQoVes0-eTYLeiv-rup28kMMB3x4EEkatdqnoQlF3A)**

### Filtering
Ideal filters?: NO: The  impulse  response  is  non-causal,  i.e.,  it  is  nonzero  for  t <  0.  Hence,  ideal  low  pass  filtering  the  signal  at  time  t  requires  convolution  with  future  signal,  which  might  not  be  known  to  us. Use transition band
**Ideal Band pass**: Ideal band pass is modulation convolved with rect, which becomes $2\cos(\omega_0 t)(\frac{\omega_c}{\pi})sinc(\frac{\omega_c}{\pi}t)$
**Causal Filtering**: You have to truncate and delay filters to make them causal: $h(t-t_d)$
**Distortionless LTI system:** $H(j \omega) = \frac{Y(j\omega)}{X(j\omega)}=Ke^{-j\omega t_d}$
In such: $|H(j\omega)|=K$ and $\angle H(j\omega)=-\omega t_d$
**Group Delay:** $t_d(\omega)=-\frac d{d\omega}=\angle H(j\omega)$
A low pass: $H(j\omega)=T rect(\frac{\omega}{4\pi B})$ This filter will span -2piB to 2piB.

### Sampling
FT of periodic functions:
General FS:$F(j\omega)=F[\sum\limits_{-\infty}^{\infty}c_ke^{jk\omega_0 t}]=\sum c_kF[e^{jk\omega_0t}]=\sum2\pi c_k\delta(\omega-k \omega_0)$
**Impulse Trains:** $\delta_T(t)=\sum\limits_{-\infty}^{\infty}\delta(t-kT)\quad c_k=\frac1T\int_{-T/2}^{T/2}\delta(t)e^{-j2\pi kt/T}dt=1/T$
$\delta(t)=\omega_0 \delta_{\omega_0}(\omega)$
Random thing: A  signal  that  is  periodic  in  time  is  discrete  in  spectrum.  A  signal  that  is  discrete  in  time  is  periodic  in  spectrum.
Sampling Theorum:
If sampled f:$\hat f(t)=f(t)\delta(t) \quad \hat F(j\omega)=\frac1T\sum F(j(\omega-k\omega_0))$
Bandwidth = +-B, such the signal spans $-2\pi B$ to $2\pi B$
While sampling, $2\pi B<\omega_0 /2$ otherwise aliasing. $T=1/2B$, then T is nyquist interval.
Whittaker Shannon Interpolation:
$\hat f(t)\ast h(t)=\sum f(kT)sinc(2Bt-k)$
Ex: $f(t)=cos(2\omega_0 t):\qquad B:2\pi B=\omega_0,B= \frac{\omega_0}{2\pi}\quad Nyq R:2B,$

**Laplace:** $\delta(t)=1 \quad u(t)=s^{-1} \quad tu(t)=s^{-2} \quad \frac12t^2u(t)=s^{-2}$...

### Tables and Derivations and Problems
**Time scaling** $F[f(at)]=\int f(at)e^{-j\omega t}dt=\frac1a\int f(\tau)e^{-j\omega \frac{\tau}a}d\tau =\frac1a\int f(\tau)e^{-j(\omega/a)\tau}d\tau=\frac1{|a|}F(j\frac{\omega}{a})$
**Conjugate** $f^{\ast}(t)=F^{\ast}(-j\omega)$
**Der**$F[f'(t)]=j\omega F(j\omega)$
**Multiplication** $F[f_1(t)f_2(t)]=\frac1{2\pi}(F_1\ast F_2)(j\omega)$
**Delay in freq domain**: $F[f(t)e^{j\omega_0 t}]=F(j(\omega-\omega_0))$
**Integral**: $\int_{-\infty}^{t}f(\tau)d\tau=F[f(t)\ast u(t)]=F[f(t)]F[u(t)]=F(j\omega)[\pi \delta(\omega) + \frac1{j\omega}]=
\pi F(0)\delta(\omega)+\frac{F(j\omega)}{j\omega}$
rect, sin, cos and eut done earlier
$F[e^{a|t|}]=\frac{2a}{a^2+\omega^2}$
![](https://i.imgur.com/gSNUe10.png)
![](https://i.imgur.com/IaLY2Qv.png)
![](https://i.imgur.com/Jorduvn.png)
![](https://i.imgur.com/Q4u0xPw.png)
![](https://i.imgur.com/k6NnzIn.png)
![](https://i.imgur.com/PxXr4dA.png)
![](https://i.imgur.com/Ue4ecEV.png)
![](https://i.imgur.com/EKd64iD.png)
![](https://i.imgur.com/YZGA7jK.png)
![](https://i.imgur.com/yUD4AFV.png)
![](https://i.imgur.com/mNPpvNH.png)
![](https://i.imgur.com/MAm8XNn.png)
![](https://i.imgur.com/yo5xEs1.png)
![](https://i.imgur.com/q4LBfSf.png)
Even: ade, Odd: f, Real: ce, Complex: ab, real and even: e, imag and odd: f, imag and even: d, $e^{j\omega_0 t}x(t)$ is real and even: b

![](https://cdn.discordapp.com/attachments/1049105924343726080/1049435605597180014/image.png)