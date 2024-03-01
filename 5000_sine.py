import numpy as np
from scipy.io.wavfile import write

def generate_sine_wave(frequency, duration, sample_rate=44100):
    # Calculate the number of samples
    num_samples = int(sample_rate * duration)
    # Generate equally spaced values over the time interval
    t = np.linspace(0, duration, num_samples, endpoint=False)
    # Generate the sine wave
    sine_wave = np.sin(2 * np.pi * frequency * t)
    # Scale the sine wave to 16-bit values
    sine_wave *= 32767
    # Convert the data to 16-bit integers
    sine_wave = np.int16(sine_wave)
    return sine_wave

def save_to_wav(filename, data, sample_rate=44100):
    # Write the data to a WAV file
    write(filename, sample_rate, data)

# Set the parameters
frequency = 5000  # Hz
duration = 5      # seconds

# Generate the sine wave
sine_wave = generate_sine_wave(frequency, duration)

# Save the sine wave to a WAV file
save_to_wav("sine_wave.wav", sine_wave)
