from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
feedbacks = list()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        feedbacks.append({'name': name, 'email': email, 'message': message})
        return redirect(url_for('feedback'))
    return render_template('main.html', feedbacks=feedbacks)


if __name__ == '__main__':
    app.run(debug=True)