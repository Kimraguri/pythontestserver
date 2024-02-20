from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('write.html')

if __name__ == '__main__':
    app.run(debug=True)
