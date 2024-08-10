from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def quiz():
    return render_template('quiz.html')

@app.route('/submit', methods=['POST'])
def submit():
    answers = {
        'q1': request.form.get('q1'),
        'q2': request.form.get('q2'),
        'q3': request.form.get('q3'),
        'q4': request.form.get('q4')
    }
    return render_template('submit.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
