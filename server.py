from flask_app import app
from flask_app.controllers import Add_ons, Clients, Commissions, Payments, Social_medias

if __name__ == "__main__":
    app.run(debug=True)