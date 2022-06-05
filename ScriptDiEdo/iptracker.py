from asyncio.log import logger
from operator import truediv
from re import T
from urllib import response
import requests
import time

def Track(ip):

    response = requests.get("http://ip-api.com/json/" + ip).json()


    print("\n\nIP richiesto: ", response['query'])

    time.sleep(3)

    if response['status'] == str('success'):


        print("\n\nCoordinate: \n\nLatitudine: ", response['lat'])
        print("Longitudine: ", response['lon'])

        print("\n\nStato/Nazione: ", response['country'])

        print("\nRegione: ", response['regionName'])
        print("\nTimezone: ", response['timezone'])

        print("\nFornitore: ", response['isp'])
        print("\nSocietà: ", response['as'])

    else:
        print("\nL'ip inserito non è valido, impossibile elaborare la richiesta")

def main():

    logged = False

    while True:
        try:
            username = int(input("Inserisci il codice: "))
            if username == int('010203'):
                print("\nLoggato correttamente")
                logged = True
                break

            else:
                print("\nIl codice inserito non è valido")
                continue

        except:
            print("inserire un codice numerico")

        
    if logged:
        while True:
            try:
                ip = str(input("\n\nInserisci un ip: "))
                break
            
            except:
                print("\nInserire una stringa")


        Track(ip)


main()
