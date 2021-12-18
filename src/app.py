from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['post', 'get'])
def get_request():
    if request.method == 'POST':
        country = request.form.get('country')  # Get data from form
        city = request.form.get('city')
    else:
        country = ''
        city = ''
    return render_template('search.html', output_text=f'{country} {city}')


if __name__ == '__main__':
    app.run(debug=True)
