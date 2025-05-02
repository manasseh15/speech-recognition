import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("A moment of silence, please...")
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        print("Ready to listen. Listening 3 times only...")

        for i in range(3):  # Change to any number of iterations you prefer
            print(f"\n[{i+1}/3] Say something!")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                print("Got it! Now to recognize it...")

                value = r.recognize_google(audio)
                print("You said: {}".format(value))
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase.")
            except sr.UnknownValueError:
                print("Oops! Didn't catch that.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    print("\nExiting program. Goodbye!")
