import numpy as np
from scipy.io.wavfile import write

def generate_sine_wave(duration, sample_rate=44100):
    # Calculate the number of samples
    num_samples = int(sample_rate * duration)
    # Generate equally spaced values over the time interval
    t = np.linspace(0, duration, num_samples, endpoint=False)

    combined_sine_wave = np.array([])

    # Define frequency for each time interval
    for time in t:
        if 0 <= time < .75:      
            frequency = 1176
        elif .75 <= time < 1.25:
            frequency = 1320
        elif 1.25 <= time < 2.25:
            frequency = 1048
        elif 2 <= time < 2.5:
            frequency = 524
        elif 2.5 <= time <= 4:
            frequency = 784

        # Generate the sine wave with constant frequency
        sine_wave = np.sin(2 * np.pi * frequency * time)
        combined_sine_wave = np.append(combined_sine_wave, sine_wave)

    # Scale the sine wave to 16-bit values
    combined_sine_wave *= 32767
    # Convert the data to 16-bit integers
    combined_sine_wave = np.int16(combined_sine_wave)

    return combined_sine_wave

def save_to_wav(filename, data, sample_rate=44100):
    # Write the data to a WAV file
    write(filename, sample_rate, data)

# Set the parameters
duration = 4  # seconds

# Generate the combined sine wave with varying frequency
combined_sine_wave = generate_sine_wave(duration)

# Save the combined sine wave to a WAV file
save_to_wav("CETK_remake.wav", combined_sine_wave)
