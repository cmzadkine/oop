from flask import Flask, request, redirect, url_for, render_template_string


app = Flask(__name__)


class Taak:
    def __init__(self, taak_id, titel):
        self.id = taak_id
        self.titel = titel
        self.klaar = False


class Takenlijst:
    def __init__(self):
        self.taken = []
        self.next_id = 1

    def add(self, titel):
        taak = Taak(self.next_id, titel)
        self.taken.append(taak)
        self.next_id += 1

    def done(self, taak_id):
        for taak in self.taken:
            if taak.id == taak_id:
                taak.klaar = True
                break

    def delete(self, taak_id):
        self.taken = [taak for taak in self.taken if taak.id != taak_id]


lijst = Takenlijst()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Takenplanner</title>
</head>
<body>

    <h1>Takenplanner</h1>

    <form method="post" action="/add">
        <input type="text" name="titel" placeholder="Nieuwe taak" required>
        <button type="submit">Toevoegen</button>
    </form>

    <hr>

    <ul>
    {% for taak in taken %}
        <li>
            {% if taak.klaar %}
                ✅ <s>{{ taak.titel }}</s>
            {% else %}
                {{ taak.titel }}
            {% endif %}

            <a href="/done/{{ taak.id }}">Klaar</a>
            <a href="/delete/{{ taak.id }}">Verwijder</a>
        </li>
    {% endfor %}
    </ul>

</body>
</html>
"""


@app.get("/")
def index():
    return render_template_string(HTML, taken=lijst.taken)


@app.post("/add")
def add():
    titel = request.form.get("titel")

    if titel:
        lijst.add(titel)

    return redirect(url_for("index"))


@app.get("/done/<int:taak_id>")
def done(taak_id):
    lijst.done(taak_id)
    return redirect(url_for("index"))


@app.get("/delete/<int:taak_id>")
def delete(taak_id):
    lijst.delete(taak_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)