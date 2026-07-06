"""
bonus_multiplayer/server.py
-----------------------------
Simpele socket-server voor de RPG (bonus-opdracht).

De server houdt de "echte" game state bij (player + huidig level) en
verwerkt commando's die de client stuurt (LOOK, ATTACK <nr>, TAKE <item>,
USE <item>, GO <richting>).

Start:
    python bonus_multiplayer/server.py

Let op: dit voorbeeld ondersteunt 1 client tegelijk (single-client server),
zoals aangeraden in de opdracht ("begin met 1 client"). Zie de docstring
onderaan voor hints om dit uit te breiden naar 2 spelers.
"""

import socket
import sys
import os

# Zorgt dat "models" en "game" importeerbaar zijn als je dit script
# vanuit de hoofdmap of vanuit bonus_multiplayer/ start.
HUIDIGE_MAP = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HUIDIGE_MAP)
sys.path.insert(0, PROJECT_ROOT)

from models.player import Player          # noqa: E402
from models.enemy import Enemy             # noqa: E402
from models.item import Item               # noqa: E402
from models.level import Level             # noqa: E402


HOST = "127.0.0.1"
PORT = 5555


def maak_wereld():
    """Zelfde opzet als in main.py, hier los beschikbaar voor de server."""
    player = Player(name="Speler1", hp=100, attack_power=10)

    forest = Level(
        name="Forest",
        description="Je staat in een donker bos.",
        enemies=[Enemy(name="Wolf", hp=20, attack_power=4)],
        items=[Item(name="Potion", item_type="heal", value=20)],
        exits={"east": "Cave"},
    )
    cave = Level(
        name="Cave",
        description="Een vochtige grot.",
        enemies=[Enemy(name="Goblin", hp=25, attack_power=6)],
        items=[Item(name="Sword", item_type="attack_boost", value=5)],
        exits={"west": "Forest"},
    )

    levels = {"Forest": forest, "Cave": cave}
    return player, levels


def verwerk_commando(cmd: str, player: Player, levels: dict, state: dict) -> str:
    """Verwerkt één commando en geeft de tekstboodschap terug die naar
    de client gestuurd moet worden."""
    cmd = cmd.strip()
    if not cmd:
        return ""

    delen = cmd.split(maxsplit=1)
    actie = delen[0].upper()
    argument = delen[1] if len(delen) > 1 else ""

    huidig_level = levels[state["huidig_level"]]

    if actie == "LOOK":
        return huidig_level.beschrijving_volledig()

    if actie == "ATTACK":
        levend = huidig_level.levende_enemies()
        if not levend:
            return "Er zijn hier geen vijanden."
        try:
            enemy = levend[int(argument)]
        except (ValueError, IndexError):
            return "Ongeldig vijand-nummer."
        boodschap = player.attack(enemy)
        if not enemy.is_alive():
            boodschap += f"\n💀 {enemy.name} is verslagen!"
        elif player.is_alive():
            boodschap += "\n" + enemy.attack(player)
        return boodschap

    if actie == "TAKE":
        item = huidig_level.remove_item(argument)
        if item is None:
            return f"Geen item genaamd '{argument}' gevonden."
        player.add_item(item)
        return f"Je hebt {item.name} opgepakt."

    if actie == "USE":
        return player.use_item(argument)

    if actie == "GO":
        if not huidig_level.is_cleared():
            return "Je moet eerst alle vijanden hier verslaan."
        volgende = huidig_level.exits.get(argument.lower())
        if volgende is None:
            return f"Geen uitgang '{argument}' hier."
        state["huidig_level"] = volgende
        return f"Je loopt naar {volgende}."

    return "Onbekend commando. Gebruik LOOK, ATTACK <nr>, TAKE <item>, USE <item>, GO <richting>."


def start_server() -> None:
    player, levels = maak_wereld()
    state = {"huidig_level": "Forest"}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"🎮 RPG-server luistert op {HOST}:{PORT} ...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"✅ Client verbonden vanaf {addr}")
            conn.sendall(
                "Welkom bij de multiplayer RPG-server! Typ LOOK om te beginnen.\n".encode("utf-8")
            )

            while True:
                data = conn.recv(1024)
                if not data:
                    print("Client heeft de verbinding verbroken.")
                    break

                cmd = data.decode("utf-8")
                print(f"Ontvangen: {cmd!r}")

                if cmd.strip().upper() == "QUIT":
                    conn.sendall("Tot ziens!\n".encode("utf-8"))
                    break

                antwoord = verwerk_commando(cmd, player, levels, state)

                if not player.is_alive():
                    antwoord += "\n💀 GAME OVER - je bent verslagen."
                    conn.sendall(antwoord.encode("utf-8"))
                    break

                conn.sendall(antwoord.encode("utf-8"))


if __name__ == "__main__":
    start_server()


# ----------------------------------------------------------------------
# Hints om uit te breiden naar 2 spelers (Stap 11 uit de opdracht):
#
# 1. Gebruik server_socket.accept() twee keer, bewaar beide 'conn' objecten
#    in een lijst clients = [conn1, conn2].
# 2. Houd een "current_turn" index bij (0 of 1) in de state.
# 3. Verwerk alleen commando's van de client wiens beurt het is; stuur de
#    andere speler een bericht als "Wacht op de beurt van Speler X".
# 4. Na een geldige actie: stuur het resultaat naar BEIDE clients (broadcast)
#    zodat iedereen de update ziet, en wissel current_turn om.
# 5. Gebruik 'threading' als je beide clients tegelijk (non-blocking) wilt
#    laten versturen/ontvangen.
# ----------------------------------------------------------------------
