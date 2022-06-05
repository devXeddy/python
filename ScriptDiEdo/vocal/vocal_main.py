from asyncio.windows_events import NULL
import pyttsx3
import time

def vocal_program():

    engine = pyttsx3.init()

    amazing_name = False
    check = True

    while check == True:
            engine.say("inserisci il tuo nome")
            engine.runAndWait()
            Name = str(input("Inserisci il tuo nome: "))
            
            while True:

                print("hai inserito il nome corretto? [y/n]")
                engine.say("hai inserito il nome corretto?")
                engine.runAndWait()

                try:
                    NameVerification = str(input(">>>"))
                    if NameVerification == 'y' or NameVerification == 'Y':
                        check = False
                        break
                        
                    elif NameVerification == 'n' or NameVerification == 'N':
                        break

                    else:
                        print("il dato inserito non è valido, inserire una delle opzioni...")
                        engine.say("il dato inserito non è valido, inserire una delle opzioni...")
                        engine.runAndWait()
                        continue

                except:
                    print("\nIl dato inserito non è valido, inserire una delle opzioni.")
                    engine.say("il dato inserito non è valido, inserire una delle opzioni.")
                    engine.runAndWait()

    lowerName = Name.lower()

    if str(lowerName) == "edoardo" or str(lowerName) == "valentina":
        amazing_name = True

    time.sleep(1)
    if amazing_name == True:
        print("\nComplimenti! hai un nome stupendo!!")
        engine.say("Complimenti! hai un nome stupendo!!")
        engine.runAndWait()

    else:
        print("\nMi dispiace, il nome Edoardo è molto più bello.")
        engine.say("Mi dispiace, il nome Edoardo è molto più bello.")
        engine.runAndWait()

    input("press enter to esc...")

    return NULL;

vocal_program()