from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # JSON-Datei öffnen und Blogposts laden
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Template rendern und Posts übergeben
    return render_template('index.html', posts=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)