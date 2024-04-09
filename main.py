from flask import Flask, request

app = Flask(__name__)

validCombos = {
    "1": {"name": "Sonos", "email": "sonos@gmail.com", "password": "sonos"},
    "2": {"name": "Google", "email": "google@gmail.com", "password": "google"},
    "3": {"name": "Facebook", "email": "facebook@gmail.com", "password": "facebook"}
}

def check_combination(name, email, password):
    for combo in validCombos.values():
        if combo["name"] == name and combo["email"] == email and combo["password"] == password:
            return True
    return False
    

@app.route("/login", methods=["POST"])
def login():
    form = request.form
    name = form["username"]
    email = form["email"]
    password = form["password"]

    if check_combination(name, email, password):
        return f"Welcome {name}!"
    else:
        return f"Sorry, {name}, you are not welcome here."

@app.route('/')
def index():
    page = """<html>
    <form method="post" action="/login">
        <p>Name: <input type="text" name="username" required></p>
        <p>Email: <input type="email" name="email" required></p>
        <p>Password: <input type="password" name="password" required></p>
        <p><button type="submit">Submit</button></p>
    </form>
    </html>
    """
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
