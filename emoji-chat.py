##Talk with yourself. It is possible to put some emojis that are: :D, =D, >:v, :8. The keyword to finish is 'Exit'.

keepTalking = True
while keepTalking:
    text = input('> ')
    if text == 'Exit':
        keepTalking = False
    text = text.replace(':D', '😀')
    text = text.replace('=D', '😄')
    text = text.replace('>:v', '👺')
    text = text.replace(':8', '😬')
    print(text)
