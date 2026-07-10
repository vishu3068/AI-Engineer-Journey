class dog:
    def speak(self):
        print('bark')
class person:
    def speak(self):
        print('hello')
def make_speak(obj):
    obj.speak()
make_speak(dog())
make_speak(person())