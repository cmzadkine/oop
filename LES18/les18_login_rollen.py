import json
import hashlib
from pathlib import Path


# =========================
# HASHING
# =========================

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def check_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash


# =========================
# USER CLASS
# =========================

class User:
    def __init__(self, username: str, password_hash: str, role: str):
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role
        }


# =========================
# USERS
# =========================

def load_users(filename="users.json"):
    path = Path(filename)

    if not path.exists():
        return []

    return json.loads(path.read_text(encoding="utf-8"))


def save_users(users, filename="users.json"):
    Path(filename).write_text(
        json.dumps(users, indent=2),
        encoding="utf-8"
    )


def ensure_default_users():
    if Path("users.json").exists():
        return

    users = [
        {
            "username": "admin",
            "password_hash": hash_password("admin123"),
            "role": "admin"
        },
        {
            "username": "user",
            "password_hash": hash_password("user123"),
            "role": "user"
        }
    ]

    save_users(users)


def find_user(users, username):
    for user in users:
        if user["username"] == username:
            return user

    return None


def login(users):
    print("\n=== LOGIN ===")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user = find_user(users, username)

    if user is None:
        print("Onbekende gebruiker.")
        return None

    if not check_password(password, user["password_hash"]):
        print("Wachtwoord klopt niet.")
        return None

    print(f"Ingelogd als {user['username']} ({user['role']})")
    return user


# =========================
# TAKEN
# =========================

def load_taken(filename="taken.json"):
    path = Path(filename)

    if not path.exists():
        return []

    return json.loads(path.read_text(encoding="utf-8"))


def save_taken(taken, filename="taken.json"):
    Path(filename).write_text(
        json.dumps(taken, indent=2),
        encoding="utf-8"
    )


def toon_taken(taken, current_user):
    if current_user["role"] == "admin":
        zichtbaar = taken
    else:
        zichtbaar = [
            taak
            for taak in taken
            if taak["owner"] == current_user["username"]
        ]

    if not zichtbaar:
        print("\n(Geen taken)")
        return []

    print("\n=== TAKEN ===")

    for i, taak in enumerate(zichtbaar, start=1):
        status = "✅" if taak["klaar"] else "⬜"

        extra = ""
        if current_user["role"] == "admin":
            extra = f" (owner: {taak['owner']})"

        print(f"{i}. {status} {taak['titel']}{extra}")

    return zichtbaar


# =========================
# MENU ACTIES
# =========================

def voeg_taak_toe(taken, current_user):
    titel = input("Titel van taak: ").strip()

    if not titel:
        print("Lege titel niet toegestaan.")
        return

    taken.append(
        {
            "titel": titel,
            "klaar": False,
            "owner": current_user["username"]
        }
    )

    save_taken(taken)
    print("Taak toegevoegd.")


def markeer_klaar(taken, current_user):
    zichtbaar = toon_taken(taken, current_user)

    if not zichtbaar:
        return

    try:
        keuze = int(input("Nummer taak: "))
    except ValueError:
        print("Ongeldige invoer.")
        return

    if keuze < 1 or keuze > len(zichtbaar):
        print("Ongeldig nummer.")
        return

    taak = zichtbaar[keuze - 1]
    taak["klaar"] = True

    save_taken(taken)
    print("Taak gemarkeerd als klaar.")


def verwijder_taak(taken, current_user):
    zichtbaar = toon_taken(taken, current_user)

    if not zichtbaar:
        return

    try:
        keuze = int(input("Nummer taak: "))
    except ValueError:
        print("Ongeldige invoer.")
        return

    if keuze < 1 or keuze > len(zichtbaar):
        print("Ongeldig nummer.")
        return

    taak = zichtbaar[keuze - 1]

    taken.remove(taak)

    save_taken(taken)
    print("Taak verwijderd.")


# =========================
# MAIN
# =========================

def main():
    ensure_default_users()

    users = load_users()
    taken = load_taken()

    current_user = login(users)

    if current_user is None:
        return

    while True:
        print("\n=== MENU ===")
        print("1. Toon taken")
        print("2. Voeg taak toe")
        print("3. Markeer taak als klaar")
        print("4. Verwijder taak")
        print("0. Stop")

        keuze = input("Keuze: ").strip()

        if keuze == "1":
            toon_taken(taken, current_user)

        elif keuze == "2":
            voeg_taak_toe(taken, current_user)

        elif keuze == "3":
            markeer_klaar(taken, current_user)

        elif keuze == "4":
            verwijder_taak(taken, current_user)

        elif keuze == "0":
            print("Programma afgesloten.")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    main()