from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Mapping choices
yourDict = {"s": -1, "w": 0, "g": 1}
reverseDict = {-1: "Snake", 0: "Water", 1: "Gun"}

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_choice = ""
    computer_choice = ""

    if request.method == "POST":
        yourStr = request.form.get("choice")
        if yourStr in yourDict:
            user = yourDict[yourStr]
            computer = random.randint(-1, 1)

            user_choice = reverseDict[user]
            computer_choice = reverseDict[computer]

            if computer == user:
                result = "It's a Draw!"
            elif (computer == -1 and user == 0):
                result = "You Lose! Snake drinks Water 🐍💧"
            elif (computer == -1 and user == 1):
                result = "You Win! Gun kills Snake 🔫🐍"
            elif (computer == 1 and user == -1):
                result = "You Lose! Gun kills Snake 🔫🐍"
            elif (computer == 1 and user == 0):
                result = "You Win! Water douses Gun 💧🔫"
            elif (computer == 0 and user == -1):
                result = "You Win! Snake drinks Water 🐍💧"
            elif (computer == 0 and user == 1):
                result = "You Lose! Water douses Gun 💧🔫"
    
    return render_template("index.html", result=result, user_choice=user_choice, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)
