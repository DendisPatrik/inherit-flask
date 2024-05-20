from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('about.html')

@app.route('/hobbies')
def hobbies():
    hobbies = ["Programming", "Dog", "Football"]
    return render_template('hobbies.html', hobbies = hobbies)


if __name__ == '__main__':
    app.run()
