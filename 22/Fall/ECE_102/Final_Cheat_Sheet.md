# Basic Signal Stuff
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
### Elementary Signals
**Complex Sinusoid**: (complex part drawn with dotted lines)
$Ae^{j(\omega t+\theta)} = A\cos(\omega t + \theta) + jA\sin(\omega t+\theta), \qquad$ Dampening and Growing sinusoid: $e^{\sigma t}\cos(\omega t + \theta)$, If $\sigma>0$ growing else dampening. 

Common Signals:
**Heavyside**: $u(t) = \begin{cases} 1 \quad t \ge 0 \\ 0 \quad \text{else} \end{cases}$
**Rectangle**: $rect(t) = \begin{cases} 1 \quad |t| \le \frac{1}{2} \\ 0 \quad \text{else} \end{cases}\quad$ and $\qquad rect_{\Delta}(t) = \begin{cases} \frac{1}{\Delta} \quad |t| \le \frac{\Delta}{2} \\ 0 \quad \text{else} \end{cases}$
**Ramp**: $r(t) = \begin{cases} t \quad t \ge 0 \\ 0 \quad \text{else} \end{cases} = \int u(t)\,dt\qquad$ and $\qquad$ **Triangle**: $\Delta(t)=\begin{cases} 1-|t| \quad |t| \le 1 \\ 0 \quad \text{else} \end{cases}$
**Impulse**: $\delta(t)=\lim\limits_{t \to 0}{rect_\Delta(t)} = \frac{d}{dt}u(t)$

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

### Fourier Series
For a well-behaved periodic signal: $f(t)$,
$f(t)=\sum\limits_{k=-\infin}^\infin{c_k}e^{jk\omega_0t}$, where c<sub>k</sub> can be given by
$c_k=\frac{1}{T}\int_\tau^{\tau+T_0}f(t)e^{-jk\omega_0t}dt$
$\int_{t_0}^{t_0+T_0}e^{jk\omega_0t}=\int_{t_0}^{t_0+T_0}cos({k\omega_0t)} + j\int_{t_0}^{t_0+T_0}sin({k\omega_0t)}$
**Also**
$Re(c_k)=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f(t)\cos(k\omega_0t)dt$
$Im(c_k)=-\frac{1}{T_0}\int_{t_0}^{t_0+T_0}f(t)\sin(k\omega_0t)dt$
**Properties**:
$Re(c_k) = Re(c_{-k})\qquad$ and $\qquad Im(c_k) = -Im(c_{-k})$
$c_k^\ast=c_{-k}\qquad$ and $\qquad |c_k|=|c_{-k}|\qquad$ and $\qquad\measuredangle c_k=-\measuredangle c_{k}^\ast$
For $f(t)$ even, $c_k=c_{-k}\qquad$ and $\qquad$For $f(t)$ odd, $-c_k=c_{-k}$
$\therefore$ $\qquad f(t)$ is even & real, $c_k$ is real $\qquad$ and $\qquad f(t)$ is odd & real, $c_k$ is imaginary

**Parsevals Theorum**:
For $x(t)$ with a fourier transform,
$P=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}|x(t)|^2dt=\sum\limits_{k=-\infin}^{\infin}|c_k|^2=\sum\limits_{k=-\infin}^{\infin}c_kc_k^*$

For $c_k=|c_k|e^{j\measuredangle c_k}$, We can have a Amplitude/Phase plot: ex: $\frac{3}{2}e^{2\pi jt}$.

**Eigenfunctions** of LTI:
For a system H, if $h(t)\ast x(t)=ax(t),\; x(t)$ is an eigenfunction.

For a signal $x(t) = e^{(\sigma+j\omega)t}$, $s=\sigma+j\omega$
$y(t)=\int_{-\infin}^\infin{h(\tau)e^{s(t-\tau)}}d\tau=\int_{-\infin}^\infin{h(\tau)e^{st}e^{-s\tau}}d\tau=e^{st}\int_{-\infin}^\infin{h(\tau)e^{-s\tau}}d\tau$
We have $H(s)=\int_{-\infin}^\infin{h(\tau)e^{-s\tau}}d\tau$ and $y(t) = H(s)e^{st}$

For a square wave which is 1 for -0.5 to 0.5,
$sinc(t) = \frac{\sin(\pi t)}{\pi t}$, also $sinc(0)=1$
$c_k=\frac{1}{2}sinc(k/2)$
