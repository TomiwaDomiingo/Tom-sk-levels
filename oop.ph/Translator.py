class Translator:
    def record(self):
        print("Recording")

    def transcribeRecording(self):
        print("Converting audio to text")

    def translateText(self):
        print("Translating text")

    def translateLive(self):
        self.record()
        self.transcribeRecording()
        self.translateText()