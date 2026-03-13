# 🤖 Nexus AI: Advanced Voice Command System

Welcome to the Nexus AI repository. This project is a sophisticated personal assistant built using Python, designed to bridge the gap between human voice commands and system-level automation.

## 👤 Developer Credits
Developed and maintained by: mrcore®
*Visionary Developer & Robotics Enthusiast.*

---

## 🚀 How to Run (طريقة التشغيل)
To get this assistant running on your local machine, follow these technical steps:

1. Clone the Repository:
   `bash
   git clone [https://github.com/Mastercore/Jarvis-AI-Assistant.git](https://github.com/Mastercore/Jarvis-AI-Assistant.git)

Install Dependencies:
Make sure you have Python 3.10+ installed. Run the following command to install all necessary libraries: pip install -r requirements.txt

Run the Application: python main.py

🧠 Core Algorithms & Logic (الخوارزميات المستخدمة)
​The system operates on a multi-layered architecture:
​Speech Recognition (Google Web Speech API): Used for converting acoustic signals into digital text strings.
​Text-to-Speech (Pyttsx3): An offline synthesis engine used to generate natural language responses.
​NLP Pattern Matching: Simple but effective logic to parse user intent and trigger system actions (Web browsing, Time retrieval, Wikipedia scraping)

​⚠️ The Debugging Journey (المشاكل التي واجهتنا)
​Building this project wasn't easy. We faced several "Master-level" challenges during development:
​The PyAudio Dependency Crisis: Installing PyAudio on Windows is notoriously difficult due to C++ compilation errors. We solved this by using pre-compiled binary wheels (.whl) specific to Python 3.13.
​Microphone Access & Permissions:
We encountered AssertionError where the system couldn't find an active audio stream. This was resolved by adjusting Windows Privacy Settings and optimizing the source context manager in Python.
​Ambient Noise Interference:
Initial tests failed in noisy environments. We implemented r.adjust_for_ambient_noise to calibrate the microphone energy threshold dynamically before each command.
​Typo Errors in Library Names:
A simple misspelling (like SpeehRecognition) can break the entire installation pipeline—a reminder that precision is key in programming!

​📜 License & Copyright
​All rights reserved to Mestercore®. This project is intended for educational purposes and to showcase the power of Python automation.
