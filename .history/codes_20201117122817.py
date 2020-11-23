import wave
import numpy as np
import matplotlib.pyplot as plt

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


# Get the sound wave frame rate
framerate_gm = good_morning.getframerate()

# Find the sound wave timestamps
time_gm = np.linspace(start=0,
                      stop=len(soundwave_gm/framerate_gm), num=len(soundwave_gm))

# Print the first 10 timestamps
print(time_gm[:10])

#######plotting the wave

# Setup the title and axis titles
plt.title('Good Afternoon vs. Good Morning')
plt.ylabel('Amplitude')
plt.xlabel('Time (seconds)')

# Add the Good Afternoon data to the plot
plt.plot(time_ga, soundwave_ga, label='Good Afternoon')

# Add the Good Morning data to the plot
plt.plot(time_gm, soundwave_gm, label='Good Morning',
   # Set the alpha variable to 0.5
   alpha=0.5)

plt.legend()
plt.show()

######Speech Recognition API

#install 
#pip3 install SpeechRecognition

# Importing the speech_recognition library
import speech_recognition as sr

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# Set the energy threshold
recognizer.energy_threshold = 300

# Create a recognizer class
recognizer = sr.Recognizer()

# Transcribe the support call audio
text = recognizer.recognize_google(
  audio_data=clean_support_call_audio, 
  language='en-US')

print(text)

############Recognize from audio file to audio data

# Instantiate Recognizer
recognizer = sr.Recognizer()

# Convert audio to AudioFile
clean_support_call = sr.AudioFile('clean_support_call.wav')

# Convert AudioFile to AudioData
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe AudioData to text
text = recognizer.recognize_google(clean_support_call_audio,
                                   language="en-US")
print(text)


####### Reconize with cutting some section out
# Instantiate Recognizer
recognizer = sr.Recognizer()

# Convert audio to AudioFile
clean_support_call = sr.AudioFile('clean_support_call.wav')

# Convert AudioFile to AudioData
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe AudioData to text
text = recognizer.recognize_google(clean_support_call_audio,
                                   language="en-US")
print(text)


# Convert AudioFile to AudioData
with static_at_start as source:
    static_art_start_audio = recognizer.record(source,
                                               duration=None,
                                               offset=3)

# Transcribe AudioData to text
text = recognizer.recognize_google(static_art_start_audio,
                                   language="en-US")

print(text)


############Different kinds of Audio


# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the Japanese audio to recognize_google
text = recognizer.recognize_google(japanese_audio, language='en-US')

# Print the text
print(text)


# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the Japanese audio to recognize_google
text = recognizer.recognize_google(japanese_audio, language='ja')

# Print the text
print(text)


# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the leopard roar audio to recognize_google
text = recognizer.recognize_google(leopard_audio, 
                                   language="en-US", 
                                   show_all=True)

# Print the text
print(text)



# Create a recognizer class
recognizer = sr.Recognizer()

# Pass charlie_audio to recognize_google
text = recognizer.recognize_google(charlie_audio, 
                                   language="en-US")

# Print the text
print(text)


# Create a recognizer class
recognizer = sr.Recognizer()

# Recognize the multiple speaker AudioData
text = recognizer.recognize_google(multiple_speakers, 
                       			   language='en-US')

# Print the text
print(text)



recognizer = sr.Recognizer()

# Multiple speakers on different files
speakers = [sr.AudioFile("speaker_0.wav"), 
            sr.AudioFile("speaker_1.wav"), 
            sr.AudioFile("speaker_2.wav")]

# Transcribe each speaker individually
for i, speaker in enumerate(speakers):
    with speaker as source:
        speaker_audio = recognizer.record(source)
    print(f"Text from speaker {i}:")
    print(recognizer.recognize_google(speaker_audio,
         				  language="en-US"))



recognizer = sr.Recognizer()

# Record the audio from the clean support call
with clean_support_call as source:
  clean_support_call_audio = recognizer.record(source)

# Transcribe the speech from the clean support call
text = recognizer.recognize_google(clean_support_call_audio,
					   language="en-US")

print(text)



recognizer = sr.Recognizer()

# Record the audio from the noisy support call
with noisy_support_call as source:
  noisy_support_call_audio = recognizer.record(source)

# Transcribe the speech from the noisy support call
text = recognizer.recognize_google(noisy_support_call_audio,
                         language="en-US",
                         show_all=True)

print(text)


recognizer = sr.Recognizer()

# Record the audio from the noisy support call
with noisy_support_call as source:
	# Adjust the recognizer energy threshold for ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=1)
    noisy_support_call_audio = recognizer.record(noisy_support_call)
 
# Transcribe the speech from the noisy support call
text = recognizer.recognize_google(noisy_support_call_audio,
                                   language="en-US",
                                   show_all=True)

print(text)


recognizer = sr.Recognizer()

# Record the audio from the noisy support call
with noisy_support_call as source:
	# Adjust the recognizer energy threshold for ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    noisy_support_call_audio = recognizer.record(noisy_support_call)
 
# Transcribe the speech from the noisy support call
text = recognizer.recognize_google(noisy_support_call_audio,
                                   language="en-US",
                                   show_all=True)

print(text)



########### Working with PyDub
'''
  TO work with mp4 file type, you will need to install ffmpeg
'''
# Import AudioSegment from Pydub
from pydub import AudioSegment

# Create an AudioSegment instance
wav_file = AudioSegment.from_file(file='wav_file.wav', 
                                  format="wav")

# Check the type
print(type(wav_file))

######To use play, you have to install pyaudio or ffmpeg (for mp4)
# Import AudioSegment and play
from pydub import AudioSegment
from pydub.playback import play

# Create an AudioSegment instance
wav_file = AudioSegment.from_file(file="wav_file.wav", 
                                  format="wav")

# Play the audio file
play(wav_file)




# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the frame rate
print(wav_file.frame_rate)


# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the number of channels
print(wav_file.channels)


# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the max amplitude
print(wav_file.max)


# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the length
print(len(wav_file))

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Create a new wav file with adjusted frame rate
wav_file_16k = wav_file.set_frame_rate(16000)

# Check the frame rate of the new wav file
print(wav_file_16k.frame_rate)


# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Set number of channels to 1
wav_file_1_ch = wav_file.set_channels(1)

# Check the number of channels
print(wav_file_1_ch.channels)


# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Print sample_width
print(f"Old sample width: {wav_file.sample_width}")

# Set sample_width to 1
wav_file_sw_1 = wav_file.set_sample_width(1)

# Check new sample_width
print(f"New sample width: {wav_file_sw_1.sample_width}")


from pydub import AudioSegment

# Import audio file
volume_adjusted = AudioSegment.from_file('volume_adjusted.wav')

# Lower the volume by 60 dB
quiet_volume_adjusted = volume_adjusted - 60


from pydub import AudioSegment

# Import audio file
volume_adjusted = AudioSegment.from_file('volume_adjusted.wav')

# Increase the volume by 15 dB
louder_volume_adjusted = volume_adjusted + 15


# Import AudioSegment and normalize
from pydub import AudioSegment
from pydub.effects import normalize

# Import target audio file
loud_then_quiet = AudioSegment.from_file('loud_then_quiet.wav')

# Normalize target audio file
normalized_loud_then_quiet = normalize(loud_then_quiet)


from pydub import AudioSegment

# Import part 1 and part 2 audio files
part_1 = AudioSegment.from_file('part_1.wav')
part_2 = AudioSegment.from_file('part_2.wav')

# Remove the first four seconds of part 1
part_1_removed = part_1[4000:]

# Add the remainder of part 1 and part 2 together
part_3 = part_1_removed + part_2



from pydub import AudioSegment

# Import the .mp3 file
mp3_file = AudioSegment.from_file('mp3_file.mp3')

# Export the .mp3 file as wav
mp3_file.export(out_f='mp3_file.wav',
                format='wav')




# Loop through the files in the folder
for audio_file in folder:
    
	# Create the new .wav filename
    wav_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".wav"
        
    # Read audio_file and export it in wav format
    AudioSegment.from_file(audio_file).export(out_f=wav_filename, 
                                      format='wav')
        
    print(f"Creating {wav_filename}...")



  

