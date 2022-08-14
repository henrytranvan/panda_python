print('Hello')
print('This is the passcode')
print('might be 1234')
passcodeGuess = input('What is the passcode? ')
print('Access Granted!')
Passcode = '1234'
stats = "Welcome to chatbot!"
fakestats = ' You Can you trust might be 1234 hahahaha Trust problem #lol'
def passcode():
  if passcodeGuess == Passcode:
    print('System stats = '+ stats )
  else:
    print('access denied')
    print('stats:' + fakestats)
    quit('BADD')
  
  
    
  

passcode()
ChatBot_Name = "chat_bot1"
print('commands are: Who are you?,Hi,Quit,what version is it?,I am sad,why,Your not real, But why?, But really why?')
UserInput = input("You: ")

while (UserInput != "quit") :
  if UserInput == 'Who are you?':
    print('ChatBot1: I am ' + ChatBot_Name)
    UserInput = input("You: ")
  if UserInput == 'Hi' :
    print('ChatBot1: Hi')
    UserInput = input('You: ') 
  if UserInput == "what version is it?":
    print("ChatBot: version 4.5 beta dev spot has closed.")
    UserInput = input('You: ')
  if UserInput == 'I am sad':
    print('Chatbot: That is sad')
  UserInput = input('You: ')
  if UserInput == 'why':
      print('ChatBot: idk')
      UserInput = input('You: ')
  if UserInput == 'But why?':
    print('Chatbot: Ok i was just made because The bot dev was bored like this one')
    UserInput = input('You: ')
  if UserInput == 'Your not real':
    print('ChatBot: Hey, I am a robot I am real what did I do? to get this')
    UserInput = input('bad:')
  if UserInput == 'But really why?':
    print('Chatbot: I get it Stop asking or else...')
    UserInput = input('Crazy guy: ') 

  print('i can not understand what you said ')
  print('can you repeat that?')
  UserInput = input("You: ")

  
