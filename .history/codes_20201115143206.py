import wave
import num

# Create audio file wave object
good_morning = wave.open('good_morning.wav', 'r')

# Read all frames from wave object 
signal_gm = good_morning.readframes(-1)

# View first 10
print(signal_gm[:10])

########################Converting Soundwave byte to integers##########

# Convert good morning audio bytes to integers
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# View the first 10 sound wave values
print(soundwave_gm[:10])
