from flask import Flask, render_template, request, redirect
import json
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    # JSON-Datei öffnen und Blogposts laden
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Template rendern und Posts übergeben
    return render_template('index.html', posts=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Daten aus dem Formular
        title = request.form['title']
        author = request.form['author']
        date = request.form['date']
        content = request.form['content']
        # Eindeutige ID generieren
        post_id = str(uuid.uuid4())
        # Neuen Beitrag erstellen
        new_post = {
            'id': post_id,
            'title': title,
            'author': author,
            'date': date,
            'content': content
        }
        # Bestehende Beiträge laden
        posts = load_blog_posts()
        # Neuen Beitrag hinzufügen
        posts.append(new_post)
        # Beiträge speichern
        save_blog_posts(posts)
        # Weiterleitung zur Startseite
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)