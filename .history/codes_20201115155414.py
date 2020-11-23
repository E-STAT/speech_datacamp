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



