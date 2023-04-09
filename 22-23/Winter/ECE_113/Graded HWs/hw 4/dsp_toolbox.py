import numpy as np
import matplotlib.pyplot as plt 

def dft(signal : np.array) -> np.array:
    """Returns the Discrete Fourier Transform of a signal

    Args:
        signal (np.array): Input signal

    Returns:
        np.array: Input Signal in the Frequency Domain
    """

    #1. Generate the DFT matrix by completing the <create_dft_matrix> function.
    length_signal = len(signal)
    dft_matrix = create_dft_matrix(length=length_signal)

    #2. Apply the DFT matrix to the signal by completing the <apply_dft_matrix> function.
    #   Store the frequency domain representation of the signal in variable <F_Signal>
    F_signal = apply_dft_matrix(dft_matrix=dft_matrix, signal=signal)

    return F_signal

def create_dft_matrix(length : int) -> np.array:
    """Returns a DFT matrix to enable calculation of the DFT.

    Args:
        length (int): length of the input signal or N of the NxN DFT Matrix.

    Returns:
        np.array: NxN DFT Matrix
    """
    dft_mat = np.zeros(shape=(length,length), dtype=np.cdouble) # We don't need this line

    #***************************** Please add your code implementation under this line *****************************
    # Hint: The complex number e^(-4j) can be represented in numpy by <np.exp(-4j)>
    dft_mat = np.array([[np.exp(-2j*np.pi*i*j/length) for j in range(length)] for i in range(length)])


    #***************************** Please add your code implementation above this line *****************************

    return dft_mat

def apply_dft_matrix(dft_matrix : np.array, signal : np.array):
    """_summary_

    Args:
        dft_matrix (np.array): The DFT Matrix
        signal (np.array): The time-domain signal

    Returns:
        F_signal (np.array): The frequency-domain signal
    """
    signal_length = signal.shape[0]
    F_signal = np.zeros(shape=signal_length)

    #***************************** Please add your code implementation under this line *****************************
    # Hint: search the numpy library documentation for the <np.matmul> operation.
    F_signal = np.matmul(dft_matrix, signal)

    #***************************** Please add your code implementation above this line *****************************

    return F_signal

def plot_dft_magnitude_angle(frequency_axis : np.array, f_signal : np.array, fs : int=1, format : str=None):
    """_summary_

    Args:
        frequency_axis (np.array).
        f_signal (np.array): input signal in the frequency domain
        fs (int, optional): Sampling Frequency. Defaults to 1.
        format (string, optional): Plotting Format. Defaults to None.
    """
    
    N = len(f_signal)
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212, sharex=ax1)

    #***************************** Please add your code implementation under this line *****************************
    if(format == None):
        ax1.set_ylabel("Magnitude")
        ax1.stem(frequency_axis, np.abs(f_signal))
        ax2.set_ylabel("Phase (radians)")
        ax2.stem(frequency_axis, np.angle(f_signal))
        ax2.set_xlabel("Frequency Bins")
        ax2.set_ylim((-np.pi, np.pi))

    if(format == "ZeroPhase"):
        #Hint: the numpy library documentation for the <np.where> operation might be useful.
        ax1.set_ylabel("Magnitude")
        ax1.stem(frequency_axis, np.abs(f_signal))
        ax2.set_ylabel("Phase (radians)")
        phase = np.array([0 if np.abs(signal) <= 1e-1 else np.angle(signal) for signal in f_signal])
        ax2.stem(frequency_axis, phase)
        ax2.set_xlabel("Frequency Bins")
        ax2.set_ylim((-np.pi, np.pi))
        
    if(format == "Normalized"):
        frequency_axis=frequency_axis-frequency_axis.min()
        frequency_axis=frequency_axis/frequency_axis.max()
        ax1.set_ylabel("Magnitude")
        ax1.stem(frequency_axis, np.abs(f_signal))
        ax2.set_ylabel("Phase (radians)")
        ax2.stem(frequency_axis, np.angle(f_signal))
        ax2.set_xlabel("Frequency Bins")
        ax2.set_ylim((-np.pi, np.pi))

    if(format == "Centered_Normalized"):
        frequency_axis=frequency_axis-frequency_axis.min()
        frequency_axis=frequency_axis/frequency_axis.max()
        indices=np.arange(-N//2,N//2)
        frequency_axis[indices[indices<0]]-=1+frequency_axis[-1]-frequency_axis[-2]
        ax1.set_ylabel("Magnitude")
        ax1.stem(frequency_axis[indices], np.abs(f_signal)[indices])
        ax2.set_ylabel("Phase (radians)")
        ax2.stem(frequency_axis[indices], np.angle(f_signal)[indices])
        ax2.set_xlabel("Frequency Bins")
        ax2.set_ylim((-np.pi, np.pi))

    if(format == "Centered_Original_Scale"):
        frequency_axis=frequency_axis-frequency_axis.min()
        frequency_axis=frequency_axis/frequency_axis.max()
        indices=np.arange(-N//2,N//2)
        frequency_axis[indices[indices<0]]-=1+frequency_axis[-1]-frequency_axis[-2]
        frequency_axis=frequency_axis*fs
        ax1.set_ylabel("Magnitude")
        ax1.stem(frequency_axis[indices], np.abs(f_signal)[indices])
        ax2.set_ylabel("Phase (radians)")
        phase=np.angle(f_signal)
        ax2.stem(frequency_axis[indices], phase[indices])
        ax2.set_xlabel("Frequency Bins")
        ax2.set_ylim((-np.pi, np.pi))

    #***************************** Please add your code implementation above this line *****************************

def idft(signal : np.array) -> np.array:
    """Returns the Inverse Discrete Fourier Transform of a frequency domain signal. 

    Args:
        signal (np.array): Input frequency signal

    Returns:
        np.array: Transforms input signal to time-domain.
    """
    length_signal = len(signal)
    time_domain_signal = np.zeros(length_signal)

    #***************************** Please add your code implementation under this line *****************************
    # Try to only use the <create_dft_matrix> and <apply_dft_matrix> operations that you have already implemented and some numpy operations.
    # Hint: look up the <np.conjugate>

    time_domain_signal = apply_dft_matrix(create_dft_matrix(length_signal).T, signal)/length_signal
    time_domain_signal = np.roll(time_domain_signal[::-1], 1) # Rectify the signal

    #***************************** Please add your code implementation above this line *****************************

    return time_domain_signal

def convolve_signals(x_signal : np.array, y_signal : np.array) -> np.array:
    """Convolve the X and Y signal using the DFT.

    Args:
        x_signal (np.array)
        y_signal (np.array)

    Returns:
        np.array: z_signal = x_signal * y_signal
    """
    z_signal = np.zeros(len(x_signal))
    
    #***************************** Please add your code implementation under this line *****************************
    #Make sure you do the time-domain convolution in the frequency domain. 
    z_signal=idft(dft(x_signal)*dft(y_signal))
    #***************************** Please add your code implementation above this line *****************************

    return z_signal

def zero_pad_signal(x_signal : np.array, new_length : int) -> np.array:
    """Append zeros to the end of the input signal until it reaches the desired [new_length].

    Args:
        x_signal (np.array): input signal.
        new_length (int): new length of signal such that we add new_length minus original_length number of zeros to the end of the signal

    Returns:
        np.array: zero-padded signal
    """
    zero_padded_signal = np.zeros(new_length)

    #***************************** Please add your code implementation under this line *****************************
    zero_padded_signal[:len(x_signal)] = x_signal
    #***************************** Please add your code implementation above this line *****************************

    return zero_padded_signal