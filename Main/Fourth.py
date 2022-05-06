from First import Hello
class Whatsapp(Hello):


    def chat(self):
        print("chat")

    def newmessage(self):
        print("calling message from whatsapp")
        #Hello.message(self)

w=Whatsapp()
w.newmessage()
