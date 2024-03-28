from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project1')
def project1():
    return render_template('project.html', project_id=1)

@app.route('/project2')
def project2():
    return render_template('project.html', project_id=2)

if __name__ == '__main__':
    app.run(debug=True)
