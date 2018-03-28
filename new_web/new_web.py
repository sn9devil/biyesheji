from flask import Flask,render_template

import data_operatio
app = Flask(__name__)


@app.route('/')
def index():
    data = data_operatio.date_find_all()
    return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run()
