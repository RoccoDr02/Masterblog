from flask import Flask, render_template, request, redirect, url_for
import json
import uuid

app = Flask(__name__)

# Funktion zum Laden der Blogposts aus der JSON-Datei
def load_blog_posts():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Funktion zum Speichern der Blogposts
def save_blog_posts(posts):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)


@app.route('/')
def index():
    # Blogposts aus JSON-Datei laden
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            posts = json.load(f)
    except FileNotFoundError:
        posts = []  # falls Datei noch nicht existiert

    # Template rendern und Posts übergeben
    return render_template('index.html', posts=posts)


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


@app.route('/delete/<post_id>', methods=['POST'])
def delete_post(post_id):
    posts = load_blog_posts()
    # Beitrag mit der passenden ID entfernen
    posts = [post for post in posts if post['id'] != post_id]
    save_blog_posts(posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)