Python Voice Assistant 🤖🎙️
Overview

This project is a Python-based Voice Assistant developed during my internship at HEX SOFTWARE.
The assistant allows users to interact with their computer using voice commands to perform different tasks such as searching the web, opening applications, retrieving weather information, and answering general questions.

The goal of this project is to demonstrate how Python, APIs, and AI models can be integrated to build an intelligent and interactive voice-controlled system.

Features 🚀

🎤 Voice Command Recognition – Converts speech into text using SpeechRecognition.

🔊 Text-to-Speech Responses – Responds to users using Google Text-to-Speech.

🌐 Web Search Automation – Performs quick searches on Google.

▶️ Open Websites – Opens platforms like YouTube and other websites.

⏰ Time Information – Tells the current system time.

🌦️ Weather Updates – Retrieves real-time weather information using a Weather API.

🤖 AI-Powered Answers – Integrated Gemini to answer general questions and provide quick information.

Technologies Used 🛠️

Python

SpeechRecognition

Google Text-to-Speech (gTTS)

Webbrowser Module

Weather API

Gemini

Google Colab / Python Environment

How It Works ⚙️

The assistant listens to the user's voice command.

Speech is converted into text using the SpeechRecognition library.

The program processes the command to determine the required task.

If the command is related to automation (open website, time, etc.), the assistant executes it.

If the user asks a general question, the query is sent to Gemini for an intelligent response.

The assistant then replies using text-to-speech audio output.

Example Commands 💬

You can try commands like:

“What is the time?”

“Open YouTube”

“Search Python programming”

“What is Artificial Intelligence?”

“Tell me the weather in London”

Project Structure 📂
Voice_Assistant_Project
│
├── Voice_Assistant.ipynb
├── modules
│   └── tts_engine.py
├── README.md
Learning Outcomes 📚

Through this project I learned:

Voice processing using speech recognition

Building voice-enabled applications

Integrating APIs for real-time data

Using AI models for intelligent responses

Automating tasks using Python

Future Improvements 🔮

Add GUI dashboard

Add face recognition login

Integrate more AI capabilities

Support offline speech recognition

Control system applications

Author 👨‍💻

Mohammad Yousuf Qureshi
AI & Machine Learning Enthusiast
Intern at HEX SOFTWARE
