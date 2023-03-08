# Import required libraries
import speech_recognition
import pyttsx3

# Initialize speech recognizer
recognizer = speech_recognition.Recognizer()

# Continuously listen for speech input
while True:
    try:
        # Use microphone as input source
        with speech_recognition.Microphone() as mic:
            # Adjust for ambient noise to improve accuracy
            recognizer.adjust_for_ambient_noise(mic, duration=2.0)

            # Listen for audio input
            audio = recognizer.listen(mic)

            # Convert audio to text using Google Speech Recognition API
            text = recognizer.recognize_google(audio)

            # Convert text to lowercase for easier processing
            text = text.lower()

            # Print recognized text to console
            print(f"Recognized {text}")

    # Handle unknown speech input errors
    except speech_recognition.UnknownValueError:
        # Re-initialize speech recognizer and continue listening
        recognizer = speech_recognition.Recognizer()
        continue
