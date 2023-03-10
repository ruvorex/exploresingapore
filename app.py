from flask import Flask, render_template

from routes.central import central
from routes.east import east
from routes.enquiry import enquiry
from routes.north import north
from routes.south import south
from routes.west import west

app = Flask(__name__)
app.secret_key = 'RTYUjnbgf59ij34rhgieudfk'

app.register_blueprint(enquiry)
app.register_blueprint(south)
app.register_blueprint(west)
app.register_blueprint(north)
app.register_blueprint(east)
app.register_blueprint(central)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)


