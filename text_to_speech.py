from gtts import gTTS
import os

def generate_hindi_audio(text):
    # Set language to Hindi
    language = 'hi'

    # Create a gTTS object with the input text and Hindi language
    tts = gTTS(text=text, lang=language)

    # Save the generated audio as an mp3 file
    tts.save("output.mp3")

    # Play the audio file using the default media player
    os.system("start output.mp3")

# Example usage
generate_hindi_audio("हेलो, मैं वेदांत हूं और मैं गे हूं।")
