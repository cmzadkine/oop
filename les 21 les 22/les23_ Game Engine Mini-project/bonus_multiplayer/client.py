"""
bonus_multiplayer/client.py
-----------------------------
Simpele socket-client voor de RPG (bonus-opdracht).

Verbindt met de server, stuurt commando's en toont het antwoord.

Start (nadat de server al draait):
    python bonus_multiplayer/client.py

Commando's om te typen: LOOK, ATTACK <nr>, TAKE <item>, USE <item>,
GO <richting>, QUIT
"""

import socket

HOST = "127.0.0.1"
PORT = 5555


def start_client() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("✅ Verbonden met de RPG-server!\n")

        # Eerst het welkomstbericht van de server ontvangen en tonen
        welkom = client_socket.recv(1024).decode("utf-8")
        print(welkom)

        while True:
            cmd = input("> ")
            if not cmd.strip():
                continue

            client_socket.sendall(cmd.encode("utf-8"))

            if cmd.strip().upper() == "QUIT":
                antwoord = client_socket.recv(1024).decode("utf-8")
                print(antwoord)
                break

            antwoord = client_socket.recv(1024)
            if not antwoord:
                print("Server heeft de verbinding verbroken.")
                break

            print(antwoord.decode("utf-8"))


if __name__ == "__main__":
    start_client()
