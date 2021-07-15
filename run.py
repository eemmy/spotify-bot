# -*- coding: utf-8 -*-
from Spotify import WebCrawler
from time import sleep
import threading

# Gets the listen times
listen_times = int(input("Quantas vezes deseja escutar cada música? (0 significa infinito): "))

# Get the listen type
listen_type = input("Qual tipo de entrada deseja usar? (1 = Música | 2 = Playlist): ")

# Get the limit of accounts
limit = int(input("Limite de contas simultâneas: "))

def run(e='', limit=30):
    threads = list()
    print("entered")

    # Loop controller
    i = 1

    # Loop accounts
    while True:
        # Instantiate the crawler
        app = WebCrawler(listen_times)

        # Get the accounts
        accounts = app.get_accounts(e)
        
        # Get the current account info
        email = accounts["A" + str(i)].value
        password = accounts["B" + str(i)].value

        # Verifies if the email is empty
        if email == None:
            # Exit the loop
            break

        # Gets the liste type
        if listen_type == "1":
            # Start the bot in a new thread
            t = threading.Thread(target=app.run_music, args=(email, password))
            threads.append(t)
            t.start()
        else:
            # Start the bot in a new thread
            t = threading.Thread(target=app.run_playlist, args=(email, password))
            t.start()
            threads.append(t)

        # Verifies if accounts range was reached
        if (i == limit):
            # ends loop
            break

        # Increments loop controller
        i += 1


    # Return threads
    return threads


i = 2

def loop(e='', limit=30):
    threads = run(e, limit)
    
    i = 2

    if e != '':
        i = int(e)+1

    while True:
        if all(not t.is_alive() for t in threads) == True:
            return loop(str(i), limit)
        else:
            sleep(2)


loop('', limit)
