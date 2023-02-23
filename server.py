from flask_app import app
from flask_app.controllers import Add_ons, Clients, Orders, Payments, Social_medias, Templates

if __name__ == "__main__":
    app.run(debug=True)