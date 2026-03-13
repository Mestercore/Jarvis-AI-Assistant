import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

# إعداد محرك الصوت
engine = pyttsx3.init()

# تخصيص الصوت (اختياري: يمكنك تغيير السرعة أو النبرة)
engine.setProperty('rate', 170)  # سرعة الكلام

def speak(text):
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... (Waiting for your command)")
        # تقليل الضجيج ليكون السمع أدق
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except:
            return ""

# --- المرحلة الأولى: التعرف على المستخدم ---
speak("Hello. I am your AI Assistant. Please type your name so I can recognize you.")
user_name = input("Enter your name: ") # تدخل اسمك هنا (مثلاً Bnane)
speak(f"Welcome Master {user_name}. Systems are online and I am ready to follow your orders.")

# --- المرحلة الثانية: الأوامر الذكية ---
while True:
    query = listen()

    # 1. ميزة الوقت (يرد بصوته)
    if "time" in query:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Master {user_name}, the current time is {time_now}")

    # 2. ميزة الشرح (إذا لم تفهم موضوعاً)
    elif "explain" in query or "tell me about" in query:
        topic = query.replace("explain", "").replace("tell me about", "")
        speak(f"Sure {user_name}, let me search my database for {topic}...")
        try:
            # يجلب جملتين فقط لتكون الإجابة سريعة ومختصرة
            summary = wikipedia.summary(topic, sentences=2)
            speak(f"Here is what I found about {topic}:")
            speak(summary)
        except:
            speak(f"I am sorry {user_name}, I couldn't find a simple explanation for that.")

    # 3. فتح المواقع
    elif "google" in query:
        speak(f"Opening Google for you, Master {user_name}")
        webbrowser.open("https://www.google.com")
        
    elif "youtube" in query:
        speak(f"As you wish {user_name}, opening YouTube now.")
        webbrowser.open("https://www.youtube.com")

    # 4. إغلاق البرنامج
    elif "exit" in query or "stop" in query:
        speak(f"Systems shutting down. Goodbye Master {user_name}!")
        break