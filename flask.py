from flask import Flask
app=Flask(__name__)
@app.route("/")

def first_flask():
    return "this is my first flask program"

@app.route("/flask_2")
def second_flask():
    return "python is done"

app.run(debug=True)