from inbuilt import *

# Lets have a class to represent a signal
# The signal can either be defined by a function or by a list of samples with a sampling frequency and a start time
class Signal:
    def __init__(self, samples=None, sampling_frequency=None, start_time=None, function=None, periodic=False):
        self.samples = samples
        self.sampling_frequency = sampling_frequency
        self.start_time = start_time
        self.function = function
        self.periodic = periodic

    def __call__(self, n):
        if self.function is not None:
            return self.function(n)
        else:
            return self.samples[n - self.start_time]
        
    def __len__(self):
        if self.function is not None:
            return 0
        else:
            return len(self.samples)
        
    def __getitem__(self, n):
        if self.function is not None:
            return self.function(n)
        else:
            return self.samples[n - self.start_time]
        
    def __setitem__(self, n, value):
        if self.function is not None:
            raise Exception("Cannot set a value to a function")
        else:
            self.samples[n - self.start_time] = value

    def __str__(self):
        # also add a check for periodic signals
        if self.function is not None:
            return self.function.__name__ + "[n]"
        else:
            return str(self.samples) + ", Periodic: " + str(self.periodic)
        
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        # if both are functions, we return a function
        if self.function is not None and other.function is not None:
            return Signal(function=lambda n: self.function(n) + other.function(n), sampling_frequency=self.sampling_frequency if self.sampling_frequency == other.sampling_frequency else None)
        # Otherwise, we need to check for lengths and sampling frequencies
        else:
            # If one of them is a function, we need to convert it to a list of samples
            if self.function is not None:
                self = self.to_samples()
            elif other.function is not None:
                other = other.to_samples()
            # Now we have two lists of samples
            # If they are of different lengths, we need to extend the shorter one
            if len(self) < len(other):
                self = self.extend(len(other) - len(self))
            elif len(other) < len(self):
                other = other.extend(len(self) - len(other))
            # Now we have two lists of samples of the same length
            # If they have different sampling frequencies, we need to resample the shorter one
            if self.sampling_frequency < other.sampling_frequency:
                self = self.resample(other.sampling_frequency)
            elif other.sampling_frequency < self.sampling_frequency:
                other = other.resample(self.sampling_frequency)
            # Now we have two lists of samples of the same length and the same sampling frequency
            # We can add them
            return Signal(samples=self.samples + other.samples, sampling_frequency=self.sampling_frequency)
        
    def __mul__(self, other):
        # similar to __add__
        if self.function is not None and other.function is not None:
            return Signal(function=lambda n: self.function(n) * other.function(n), sampling_frequency=self.sampling_frequency if self.sampling_frequency == other.sampling_frequency else None)
        else:
            if self.function is not None:
                self = self.to_samples()
            elif other.function is not None:
                other = other.to_samples()
            if len(self) < len(other):
                self = self.extend(len(other) - len(self))
            elif len(other) < len(self):
                other = other.extend(len(self) - len(other))
            if self.sampling_frequency < other.sampling_frequency:
                self = self.resample(other.sampling_frequency)
            elif other.sampling_frequency < self.sampling_frequency:
                other = other.resample(self.sampling_frequency)
            return Signal(samples=self.samples * other.samples, sampling_frequency=self.sampling_frequency)
        
    def __sub__(self, other):
        # similar to __add__
        if self.function is not None and other.function is not None:
            return Signal(function=lambda n: self.function(n) - other.function(n), sampling_frequency=self.sampling_frequency if self.sampling_frequency == other.sampling_frequency else None)
        else:
            if self.function is not None:
                self = self.to_samples()
            elif other.function is not None:
                other = other.to_samples()
            if len(self) < len(other):
                self = self.extend(len(other) - len(self))
            elif len(other) < len(self):
                other = other.extend(len(self) - len(other))
            if self.sampling_frequency < other.sampling_frequency:
                self = self.resample(other.sampling_frequency)
            elif other.sampling_frequency < self.sampling_frequency:
                other = other.resample(self.sampling_frequency)
            return Signal(samples=self.samples - other.samples, sampling_frequency=self.sampling_frequency)
        
    def __truediv__(self, other):
        # similar to __add__
        if self.function is not None and other.function is not None:
            return Signal(function=lambda n: self.function(n) / other.function(n), sampling_frequency=self.sampling_frequency if self.sampling_frequency == other.sampling_frequency else None)
        else:
            if self.function is not None:
                self = self.to_samples()
            elif other.function is not None:
                other = other.to_samples()
            if len(self) < len(other):
                self = self.extend(len(other) - len(self))
            elif len(other) < len(self):
                other = other.extend(len(self) - len(other))
            if self.sampling_frequency < other.sampling_frequency:
                self = self.resample(other.sampling_frequency)
            elif other.sampling_frequency < self.sampling_frequency:
                other = other.resample(self.sampling_frequency)
            return Signal(samples=self.samples / other.samples, sampling_frequency=self.sampling_frequency)

    def __neg__(self):
        if self.function is not None:
            return Signal(function=lambda n: -self.function(n))
        else:
            return Signal(samples=-self.samples)
        
    def __abs__(self):
        if self.function is not None:
            return Signal(function=lambda n: abs(self.function(n)))
        else:
            return Signal(samples=abs(self.samples))
        
    def __eq__(self, other):
        if self.function is not None:
            return self.function == other.function
        else:
            return self.samples == other.samples
        
    # Now we will start adding other functions
    def to_samples(self):
        if self.function is not None:
            return Signal(samples=[self.function(n) for n in range(len(self))], sampling_frequency=self.sampling_frequency, start_time=self.start_time)
        else:
            return self

    def extend(self, n):
        if self.function is not None:
            return Signal(function=self.function, sampling_frequency=self.sampling_frequency, start_time=self.start_time)
        else:
            # if it is periodic, we can just repeat the samples
            if self.is_periodic():
                return Signal(samples=self.samples * (n // len(self.samples) + 1), sampling_frequency=self.sampling_frequency, start_time=self.start_time)
            else:
                return Signal(samples=self.samples + [0] * n, sampling_frequency=self.sampling_frequency, start_time=self.start_time)

    def resample(self, sampling_frequency):
        if self.function is not None:
            return Signal(function=self.function, sampling_frequency=sampling_frequency, start_time=self.start_time)
        else:
            return Signal(samples=self.samples, sampling_frequency=sampling_frequency, start_time=self.start_time)

    # first a time shift
    def time_shift(self, n):
        if self.function is not None:
            return Signal(function=lambda m: self.function(m - n))
        else:
            return Signal(samples=self.samples, start_time=self.start_time + n)
        
    # now a time reversal
    def time_reversal(self):
        if self.function is not None:
            return Signal(function=lambda n: self.function(-n))
        else:
            return Signal(samples=self.samples[::-1], start_time=-self.start_time - len(self.samples) + 1)
        
    # now a time scaling
    def time_scaling(self, alpha):
        if self.function is not None:
            return Signal(function=lambda n: self.function(n / alpha))
        else:
            return Signal(samples=self.samples, sampling_frequency=self.sampling_frequency * alpha)
        
    # down sampling: When we down sample we will lose information
    def down_sampling(self, alpha):
        if self.function is not None:
            return Signal(function=lambda n: self.function(n * alpha))
        else:
            return Signal(samples=self.samples[::alpha], sampling_frequency=self.sampling_frequency / alpha)
        
    # up sampling: When we up sample we will add zeros
    def up_sampling(self, alpha):
        if self.function is not None:
            return Signal(function=lambda n: self.function(n / alpha))
        else:
            return Signal(samples=[self.samples[n // alpha] if n % alpha == 0 else 0 for n in range(len(self.samples) * alpha)], sampling_frequency=self.sampling_frequency * alpha)

# We will make a new class for sinusoids
class Sinusoid(Signal):
    def __init__(self, amplitude, frequency, phase, cos=True, sampling_frequency=None, start_time=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase if cos else phase - pi / 2
        self.cos = cos
        self.sampling_frequency = sampling_frequency
        self.start_time = start_time

    def __repr__(self):
        return f"{'cos' if self.cos else 'sin'}({self.amplitude} * exp(j * 2 * pi * {self.frequency} * n + {self.phase if self.cos else self.phase + pi / 2}))"
    
    def __call__(self, n):
        return self.amplitude * exp(1j * 2 * pi * self.frequency * n + self.phase)
    
    def __eq__(self, other):
        return repr(self) == repr(other)

    def to_samples(self):
        return Signal(function=self.__call__, sampling_frequency=self.sampling_frequency, start_time=self.start_time)
    
# Lets create other functions
def convolve(signal1, signal2):
    # We will assume that these two signals have the same length, sampling frequency, start time and are sampled rather than defined by a function
    # First lets find out how long the resulting signal will be
    length = len(signal1) + len(signal2) - 1
    # Now we will convolve the samples of the signals
    samples = [sum([signal1.samples[n - m] * signal2.samples[m] for m in range(len(signal1))]) for n in range(length)]
    # We will now return the convolution
    return Signal(samples=samples, sampling_frequency=signal1.sampling_frequency, start_time=signal1.start_time + signal2.start_time)




def convolve2(signal1, signal2):
    # We will first extend the signals so that they have the same length
    if len(signal1) < len(signal2):
        signal1 = signal1.extend(len(signal2) - len(signal1))
    elif len(signal2) < len(signal1):
        signal2 = signal2.extend(len(signal1) - len(signal2))

    # We will then convolve the samples of the signals
    samples = [sum([signal1.samples[n - m] * signal2.samples[m] for m in range(len(signal1))]) for n in range(len(signal1))]

    # We will now calculate the start time of the convolution
    start_time = signal1.start_time + signal2.start_time

    # We will now return the convolution
    return Signal(samples=samples, sampling_frequency=signal1.sampling_frequency, start_time=start_time)

