import streamlit as st

st.set_page_config(page_title="SignISLMed", layout="wide")

import time
import googletrans
import speech_recognition
import gtts
import playsound

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os
import cv2
import io

from detectv8 import onButtonPressv8
from detect import onButtonPress



col4, col5, col6 = st.columns(3, gap="large")

with col5:
    st.header("SignISLMed")
    st.header("  ")
    
st.subheader("Sign to Spoken Language")
st.header("  ")
    


# # display the content of unique_classes.txt
# def display_unique_classes(stop_detection_placeholder):
#     # with open("/Users/adityadubey/Desktop/yolov5/runs/detect/exp35/unique_classes.txt", "r") as file:
#     with open("D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp31/unique_classes.txt", "r") as file:
#         unique_classes_content = file.read()
        
#     with stop_detection_placeholder.container():
#         st.text("Unique Classes:")
#         st.text(unique_classes_content)




# Function to translate text
def translate_text(text, input_lang, output_lang):
    translator = googletrans.Translator()
    translation = translator.translate(text, dest=output_lang)
    text_new = translation.text

    # Remove any special characters from the translated text
    sanitized_text = ''.join(e for e in text_new if e.isalnum() or e == ' ')
    return sanitized_text



# # Download NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')

# Function to process text and display videos
def process_text_and_display_videos(text):
    # Step 2: Load custom stopwords from file
    with open("D://ENGG//SEM 8//B.TECH PROJECT//yolov5v8streamlit//custom_stopwords.txt", "r") as file:
        custom_stopwords = file.read().splitlines()

    # Step 3: Remove stopwords
    stop_words = set(stopwords.words('english') + custom_stopwords)
    word_tokens = word_tokenize(text)
    filtered_sentence = [word for word in word_tokens if word.lower() not in stop_words]

    # Step 4: Perform stemming
    ps = PorterStemmer()
    stemmed_words = [ps.stem(word) for word in filtered_sentence]

    # Step 5: Break down stemmed sentence into individual words
    individual_words = ' '.join(stemmed_words).split()



    # Step 6: Fetch and play videos corresponding to words
    video_directory = "D://ENGG//SEM 8//B.TECH PROJECT//yolov5v8streamlit//videos"
    video_files = os.listdir(video_directory)
    for word in text.split():
        for video_file in video_files:
            if word in video_file:
                video_path = os.path.join(video_directory, video_file)
                st.video(video_path)
                break



    




def extract_and_write_unique_lines_to_same_file(file_path):
    unique_lines = set()

    # Open the text file in read mode
    with open(file_path, 'r') as file:
        # Read each line from the file
        for line in file:
            # Add the whole line to the unique_lines set
            unique_lines.add(line.strip())

    # Re-open the file in write mode to overwrite its contents
    with open(file_path, "w") as f:
        # Write each unique line to the same file
        for line in unique_lines:
            f.write(f"{line}\n")





 



def read_text_file_and_display_as_stream_v5(stop_detection_placeholder_v5, file_path):
    # Specify the file path
    # file_path = "D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp35/unique_classes.txt"
    
    # Open the text file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file and convert to a single string
        words = file.read().split()

    trans_text = ""


    def stream_words():
        nonlocal trans_text
        for word in words:
            trans_text += word + " "
            yield word + " "
            time.sleep(0.23)
    
    # Open a container in the specified placeholder
    with stop_detection_placeholder_v5.container():
        # Write the words to the stream
        st.write_stream(stream_words())


    # st.write(trans_text)
    # Call spoken_output function to convert and play trans_text
    spoken_output(trans_text)













def spoken_output(text):
    input_lang = "en"
    output_lang = "hi"

    translator = googletrans.Translator()
    translation = translator.translate(text, dest=output_lang)
    text_new = translation.text

    # Remove any special characters from the translated text
    sanitized_text = ''.join(e for e in text_new if e.isalnum() or e == ' ')

    # Generate the audio data
    tts = gtts.gTTS(text_new, lang=output_lang)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    # Display the audio player in the Streamlit app
    st.audio(audio_buffer, format='audio/mp3')






# function not required now
def read_text_file_and_display_as_stream_v8(stop_detection_placeholder_v8, file_path):
    # Specify the file path
    # file_path = "D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp35/unique_classes.txt"
    
    # Open the text file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file and convert to a single string
        words = file.read().split()

    def stream_words():
        for word in words:
            yield word + " "
            time.sleep(0.23)
    
    # Open a container in the specified placeholder
    with stop_detection_placeholder_v8.container():
        # Write the words to the stream
        st.write_stream(stream_words())







# 

col1, col2, col3 = st.columns(3, gap="large")

# col1, col2= st.columns(2, gap="large")

with col1:
   st.header("YOLOV5")
   detectv5 = st.button("Start the detection(V5)")
   stopDetectv5 = st.button("Stop the detection", key="stop_v5")
   placeholderv5 = st.empty()

   # Placeholder for the Stop Detection button
   stop_detection_placeholder_v5 = st.empty()

   if detectv5:
    onButtonPress(placeholderv5)
   if stopDetectv5:
    file_path = "D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp53/unique_classes.txt"
    # display_unique_classes(stop_detection_placeholder)
    read_text_file_and_display_as_stream_v5(stop_detection_placeholder_v5, file_path)
     

with col3:
   st.header("YOLOV8")
   detectv8 = st.button("Start the detection(V8)")
   stopDetectv8 = st.button("Stop the detection", key="stop_v8")
   placeholderv8 = st.empty()

   # Placeholder for the Stop Detection button
   stop_detection_placeholder_v8 = st.empty()

   if detectv8:
    onButtonPressv8(placeholderv8)
   if stopDetectv8:
    file_path_v8 = "D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/unique_labels_v8_1.txt"
    # display_unique_classes(stop_detection_placeholder)
    extract_and_write_unique_lines_to_same_file(file_path_v8)
    read_text_file_and_display_as_stream_v5(stop_detection_placeholder_v8, file_path_v8)





st.header("   ")
st.subheader("Spoken Language to Sign")



# Button to trigger audio capture
if st.button("Capture Audio"):
    # use for text to sign or audio to sign
    input_lang = "hi"
    output_lang = "en"

    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        st.write("Speak now...")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        st.write(f"Captured text: {text}")
    

# Translate captured text to English
    translated_text = translate_text(text, input_lang, output_lang)
    st.write(f"Translated text: {translated_text}")

    # Process translated text and display videos
    process_text_and_display_videos(translated_text)

