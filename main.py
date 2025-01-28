import speech_recognition as sr
import pyttsx3
import requests
import threading

API_URL = "https://api.edenai.run/v2/text/generation"
HEADERS = {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
}

engine = pyttsx3.init()
speaking = False

def get_ai_response(user_input):
    try:
        payload = {
            "providers": "openai",
            "text": user_input,
            "parameters": {
                "max_tokens": 200,
                "temperature": 0.7,
            }
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        response_json = response.json()
        standardized_response = response_json.get("openai/gpt-4o", {}).get("standardized_response", {})
        generated_text = standardized_response.get("generated_text", "Desculpe, não consegui gerar uma resposta.")
        return generated_text
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou ouvindo...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("Desculpe, não entendi.")
            return ""
        except sr.RequestError:
            print("Desculpe, houve um problema com o serviço de reconhecimento de fala.")
            return ""

def speak(text):
    global speaking
    speaking = True
    voices = engine.getProperty("voices")
    for voice in voices:
        if "pt" in voice.languages or "brazil" in voice.id:
            engine.setProperty("voice", voice.id)
            break
    engine.say(text)
    engine.runAndWait()
    speaking = False

def stop_speaking():
    global speaking
    if speaking:
        engine.stop()
        speaking = False

def main():
    global speaking
    while True:
        user_input = listen_to_user()
        if user_input.lower() == "parar":
            stop_speaking()
            continue
        if user_input.lower() in ["sair", "fechar"]:
            print("Até logo!")
            break
        if user_input:
            ai_response = get_ai_response(user_input)
            print(f"Robô: {ai_response}")
            speak(ai_response)

if __name__ == "__main__":
    main()
