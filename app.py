from flask import Flask, request, render_template_string

app = Flask(__name__)
notes = []

HTML = """
<h2>📝 Notes App</h2>
<form method="POST">
    <input name="note" placeholder="Write a note" required>
    <button>Add</button>
</form>
<ul>
{% for n in notes %}
  <li>{{ n }}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        notes.append(request.form["note"])
    return render_template_string(HTML, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
