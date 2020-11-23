import wave

# Create audio file wave object
good_morning = wave.open('good_morning.wav', 'r')

# Read all frames from wave object 
soundwave_gm = good_morning.readframes(-1)

# View first 10
print(soundwave_gm[:10])