from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_request():
    table_request = request.form
    return render_template('index.html', prediction_text='Sssss')


if __name__ == '__main__':
    app.run()
