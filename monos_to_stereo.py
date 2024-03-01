import numpy as np
import scipy.io.wavfile

# Load the two mono WAV files
file_path_1 = "combined_output.wav"
file_path_2 = "Mono_Amplitude_1.wav"

sr, y_1 = scipy.io.wavfile.read(file_path_1)
_, y_2 = scipy.io.wavfile.read(file_path_2)

# Ensure both audio files have the same sample rate
assert sr == 44100, "Sample rates of both files should be 44100Hz"

# Make sure both files have the same length
assert len(y_1) == len(y_2), "Audio files must have the same length"

# Convert mono signals to stereo
y_stereo = np.column_stack((y_1, y_2))

# Normalize the stereo signal
max_val = np.max(np.abs(y_stereo))
y_stereo_normalized = y_stereo / max_val

# Save the stereo audio as a new WAV file
output_file_path = "final_stereo_output.wav"
scipy.io.wavfile.write(output_file_path, sr, y_stereo_normalized)
