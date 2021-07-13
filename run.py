# -*- coding: utf-8 -*-
from Spotify import WebCrawler
import threading

# Gets the listen times
listen_times = int(input("Quantas vezes deseja escutar cada música? (0 significa infinito): "))

# Get the listen type
listen_type = input("Qual tipo de entrada deseja usar? (1 = Música | 2 = Playlist): ")



def run():
    threads = list()

    # Loop controller
    i = 1

    # Loop accounts
    while True:
        # Instantiate the crawler
        app = WebCrawler(listen_times)

        # Get the accounts
        accounts = app.get_accounts()
        
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
            t.start()
        else:
            # Start the bot in a new thread
            t = threading.Thread(target=app.run_playlist, args=(email, password))
            t.start()
            # Run the bot with playlists
            # app.run_playlist(email, password)

        i += 1

run()

