
chat = True
while chat:
    text = input('how you feeling today?')
    if text == 'exit':
        chat = False
    texto = text.replace('happy', '😊')
    texto = text.replace('sad', '☹')

    print(text)