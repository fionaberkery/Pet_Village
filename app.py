from flask import Flask, render_template

from controllers.owners_controller import owners_blueprint
from controllers.pets_controller import pets_blueprint
from controllers.treatments_controller import treatments_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.nurse_controller import nurses_blueprint
from controllers.price_controller import prices_blueprint
from controllers.booking_controller import bookings_blueprint


app = Flask(__name__)

app.register_blueprint(owners_blueprint)
app.register_blueprint(pets_blueprint)
app.register_blueprint(treatments_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(nurses_blueprint)
app.register_blueprint(prices_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def main():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
