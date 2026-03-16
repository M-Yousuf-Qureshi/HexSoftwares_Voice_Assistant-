#!/usr/bin/env python
# coding: utf-8

# ## **New Project Voice Assistant**
# ## 1. **Speech Recognition Setup**
# 
# 

# In[ ]:


get_ipython().system('pip install SpeechRecognition ffmpeg-python')
get_ipython().system('pip install gTTS')


# After installing the libraries, we can write a simple script to listen for audio input from your microphone and convert it into text using Google's Web Speech API (which `SpeechRecognition` uses by default for online recognition).

# In[ ]:


import datetime
import requests
from google.colab import userdata
from gtts import gTTS
from IPython.display import Audio, display
import google.generativeai as genai

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'response.mp3'
    tts.save(filename)
    display(Audio(filename, autoplay=True))
    print(f"Assistant: {text}")

def get_weather(city):
    try:
        api_key = userdata.get('OPENWEATHER_API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city.strip()}&appid={api_key}&units=metric'
        res = requests.get(url).json()
        if res.get('cod') != 200:
            return f"I couldn't find the weather for {city}."
        temp = res['main']['temp']
        desc = res['weather'][0]['description']
        return f"The weather in {city} is currently {desc} with {temp} degrees."
    except:
        return "I had trouble connecting to the weather service."


# ### 3. Weather API Integration
# 
# To get real-time weather, we'll use the OpenWeatherMap API.
# 1. Go to [OpenWeatherMap](https://openweathermap.org/api) and sign up for a free 'Current Weather Data' API key.

# In[ ]:


from google.colab import userdata
try:
    api_key = userdata.get('OPENWEATHER_API_KEY')
    print('Secret found successfully.')
except userdata.SecretNotFoundError:
    print('Error: Please add a secret named OPENWEATHER_API_KEY in the sidebar and enable notebook access.')


# In[ ]:


import requests
from google.colab import userdata

def get_weather(city: str) -> str:
    """
    Fetches current weather information for a given city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city to get weather for.

    Returns:
        str: A string describing the current weather conditions or an error message.
    """
    try:
        # Retrieve the API key from Colab user data secrets
        api_key = userdata.get('OPENWEATHER_API_KEY')
        if not api_key:
            return "Weather service setup error: OPENWEATHER_API_KEY not found."

        # Construct the API request URL with the city, API key, and metric units
        # Strip leading/trailing whitespace from the city name for cleaner API calls
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city.strip()}&appid={api_key}&units=metric'

        # Make the API call and parse the JSON response
        response_data = requests.get(url).json()

        # Check if the API call was successful (status code 200)
        if response_data.get('cod') != 200:
            # If not successful, return the error message from the API or a generic one
            return f"I couldn't find the weather for {city.strip()}. Reason: {response_data.get('message', 'Unknown error.')}"

        # Extract temperature and description from the successful response
        temperature = response_data['main']['temp']
        description = response_data['weather'][0]['description']

        # Format and return the weather report
        return f"The weather in {city.strip()} is currently {description} with a temperature of {temperature} degrees Celsius."

    except requests.exceptions.RequestException as req_err:
        # Handle network-related errors (e.g., no internet connection, DNS failure)
        return f"I had trouble connecting to the weather service due to a network error: {req_err}"
    except Exception as e:
        # Handle any other unexpected errors during the process
        return f"An unexpected error occurred while fetching weather for {city.strip()}: {e}"


# In[ ]:


def process_command_with_weather(text):
    text = text.lower()
    if 'weather in' in text:
        city = text.split('weather in')[-1].strip()
        report = get_weather(city)
        speak(report)
    elif 'search for' in text:
        search_query = text.split('search for')[-1].strip()
        speak(f"Searching for {search_query}.")
    elif 'time' in text:
        now = datetime.datetime.now().strftime('%H:%M')
        speak(f"The current time is {now}.")
    else:
        speak("I'm not sure how to help with that yet.")

# To use this, call process_command_with_weather(user_text) in your main loop.


# In[ ]:


import webbrowser

def process_command_extended(text):
    text = text.lower()
    if 'search for' in text:
        search_query = text.split('search for')[-1].strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Searching Google for {search_query}.")
    elif 'open youtube' in text:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif 'time' in text:
        now = datetime.datetime.now().strftime('%H:%M')
        speak(f"The current time is {now}.")
    else:
        speak("I heard you, but that command isn't programmed yet.")

# To test this, you would replace process_command in the previous loop with process_command_extended.


# ### 4. Text-to-Speech (TTS) Setup
# 
# To allow the assistant to speak, we'll use the `gTTS` library. It converts text into an MP3 file, which we can then play directly in the notebook.

# In[ ]:


pip install gTTS


# ## 5. Creating Voice Assistant

# In[ ]:


from gtts import gTTS
from IPython.display import Audio, display

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'response.mp3'
    tts.save(filename)
    display(Audio(filename))
    print(f"Assistant: {text}")

# Test the assistant's voice
speak("Hello! I am  Mohammad Yousaf custom voice assistant. How can I help you today?")


# ## 5. Integrate with Gemini

# In[ ]:


import google.generativeai as genai
from google.colab import userdata

# Configure Gemini API
try:
    GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    print("Gemini AI integrated successfully.")
except Exception as e:
    print("Note: Please add GOOGLE_API_KEY to Secrets to enable advanced Python tutoring.")


# In[ ]:


import google.generativeai as genai
from google.colab import userdata

# Configure Gemini API
try:
    GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    # Using gemini-pro which has high compatibility with this library version
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    print("Gemini AI configuration updated to gemini-pro.")
except Exception as e:
    print(f"Note: Error initializing Gemini: {e}")


# In[ ]:


from google.colab import userdata
import google.generativeai as genai
import requests

def run_diagnostics():
    print("--- Assistant Diagnostic Check ---")

    # 1. Check Gemini
    try:
        gemini_key = userdata.get('GOOGLE_API_KEY')
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        model.generate_content('test')
        print("✅ Gemini AI: Connected and Authorized.")
    except Exception as e:
        print(f"❌ Gemini AI: Error - {e}")

    # 2. Check Weather
    try:
        weather_key = userdata.get('OPENWEATHER_API_KEY')
        test_url = f'http://api.openweathermap.org/data/2.5/weather?q=London&appid={weather_key}'
        res = requests.get(test_url).json()
        if res.get('cod') == 200:
            print("✅ Weather API: Connected and Authorized.")
        else:
            print(f"❌ Weather API: {res.get('message', 'Unknown Error')}")
    except Exception as e:
        print(f"❌ Weather API: Error - {e}")

run_diagnostics()


# In[ ]:


def process_command_advanced(text):
    text = text.lower().strip()

    # Check if it's a weather query
    if 'weather' in text:
        city = text.replace('what is the', '').replace('weather today', '').replace('in', '').replace('weather', '').strip()
        if not city or 'isb' in city:
            city = 'Islamabad'
        report = get_weather(city)
        speak(report)

    # AI Brain (Gemini)
    # elif any(word in text for word in ['python', 'function', 'code', 'how to', 'what is', 'explain']):
    #     speak('Let me check my database for that...')
    else:
        try:
            prompt = f'You are a helpful Assistant. Answer the user\'s question concisely: {text}'
            # Ensure the function uses the current model instance
            response = model.generate_content(prompt)
            speak(response.text)
        except Exception as e:
            speak('I\'m having trouble accessing my programming database right now.')
            print(f'AI Error: {e}')

    # else:
    #     speak('I heard you. How can I help with Python or weather?')


# In[ ]:


import ipywidgets as widgets
from IPython.display import Javascript, Audio, display
from google.colab.output import eval_js
import speech_recognition as sr
import ffmpeg
import base64

output_area = widgets.Output()
status_label = widgets.Label(value='Ready')
command_input = widgets.Text(placeholder='Type command here...')
listen_btn = widgets.Button(description='Listen', button_style='primary', icon='microphone')
send_btn = widgets.Button(description='Send', button_style='success')

def on_listen(b):
    with output_area:
        status_label.value = 'Listening...'
        # Define and make the JavaScript record function available
        display(Javascript('''async function record() { const stream = await navigator.mediaDevices.getUserMedia({ audio: true }); const mediaRecorder = new MediaRecorder(stream); const chunks = []; mediaRecorder.ondataavailable = e => chunks.push(e.data); const promise = new Promise(resolve => { mediaRecorder.onstop = () => { const blob = new Blob(chunks, { type: 'audio/webm' }); const reader = new FileReader(); reader.readAsDataURL(blob); reader.onloadend = () => resolve(reader.result.split(',')[1]); }; }); mediaRecorder.start(); await new Promise(r => setTimeout(r, 4000)); mediaRecorder.stop(); return promise; }'''))
        try:
            # Call the JavaScript record function using eval_js
            s = eval_js('record()')
            with open('in.webm', 'wb') as f: f.write(base64.b64decode(s))
            ffmpeg.input('in.webm').output('in.wav', ac=1, ar='16k').run(overwrite_output=True, quiet=True)
            r = sr.Recognizer()
            with sr.AudioFile('in.wav') as source: user_text = r.recognize_google(r.record(source))
            status_label.value = f'You: {user_text}'; process_command_advanced(user_text) # Changed to process_command_advanced
        except Exception as e: # Catch specific exception for better debugging
            status_label.value = f'Recognition failed: {e}'

def on_send(b):
    with output_area: process_command_advanced(command_input.value); command_input.value = '' # Changed to process_command_advanced

listen_btn.on_click(on_listen); send_btn.on_click(on_send)
display(widgets.VBox([widgets.HTML('<h2>Voice Assistant</h2>'), widgets.HBox([command_input, send_btn, listen_btn]), status_label, output_area]))


# In[ ]:


# Update the GUI Send button to use the advanced logic
from IPython.display import clear_output

def on_send_clicked_advanced(b):
    with output_area:
        clear_output()
        text = command_input.value
        if text:
            status_label.value = f"Consulting Database: {text}"
            process_command_advanced(text)
            command_input.value = ""

send_btn.on_click(on_send_clicked_advanced, remove=True)
send_btn.on_click(on_send_clicked_advanced)
print("GUI updated to handle Python and Weather queries!")


# In[ ]:




