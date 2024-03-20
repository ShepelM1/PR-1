from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', message='Привіт, це мій перший веб-застосунок на Flask!')


@app.route('/about/<name>')
def about(name):
    return render_template('about.html', message=f'Це сторінка про {name}.')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/form_data', methods=['POST'])
def form_data():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    return render_template('form_data.html', name=name, email=email, message=message)


if __name__ == '__main__':
    app.run(debug=True)
