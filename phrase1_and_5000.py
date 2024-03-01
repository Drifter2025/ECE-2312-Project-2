import numpy as np
from scipy.io import wavfile

def normalize_audio(data):
    max_amplitude = np.max(np.abs(data))
    if max_amplitude > 0:
        scale_factor = 32767 / max_amplitude
        normalized_data = data * scale_factor
    else:
        normalized_data = data
    return normalized_data.astype(np.int16)

# Load the WAV files
sample_rate1, data1 = wavfile.read("Mono_Amplitude_1.wav")
sample_rate2, data2 = wavfile.read("sine_wave.wav")

# Ensure both arrays have the same length
min_length = min(len(data1), len(data2))
data1 = data1[:min_length]
data2 = data2[:min_length]

# Normalize both audio data
normalized_data1 = normalize_audio(data1)
normalized_data2 = normalize_audio(data2)

# Add the normalized audio data together
combined_data = normalized_data1*4 + normalized_data2

# Normalize the combined data to prevent clipping
#combined_data_normalized = normalize_audio(combined_data)

# Write the combined data to a new WAV file
wavfile.write("combined_output.wav", sample_rate1, combined_data)#_normalized)
