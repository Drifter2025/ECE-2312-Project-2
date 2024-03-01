import scipy.signal
import scipy.io.wavfile
import numpy as np

# Load the WAV file
file_path = "combined_output.wav"
sr, y = scipy.io.wavfile.read(file_path)

# Define the frequency cutoff (4000Hz)
cutoff_freq = 4000

# Normalize the audio data to the range [-1, 1]
y = y.astype(np.float32) / 32768.0

# Design a low-pass FIR filter
nyquist = 0.5 * sr
cutoff = cutoff_freq / nyquist
numtaps = 101  # Adjust the filter length as needed
b = scipy.signal.firwin(numtaps, cutoff)

# Apply the filter to the audio data
y_lowpass = scipy.signal.lfilter(b, 1.0, y)

# Convert the audio data back to the original data type
y_lowpass = np.clip(y_lowpass * 32767.0, -32768, 32767).astype(np.int16)

# Save the filtered audio as a new WAV file
output_file_path = "4000_filtered.wav"
scipy.io.wavfile.write(output_file_path, sr, y_lowpass)
