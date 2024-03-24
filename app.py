from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey


app = Flask(__name__)

responses = []

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/questions/<int:id>')
def question_page(id):
    q = satisfaction_survey.questions[id].question
    choices = satisfaction_survey.questions[id].choices
    print(request.form)
    #raise
    #responses.append(request.form['choices'])
    return render_template("question.html", id=id, question=q, choices=choices)

@app.route('/answer', methods=["POST"])
def answer():
    ans = request.form['answer']
    responses.append(ans)
    if (len(responses) == len(satisfaction_survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(responses)}")
    
@app.route("/complete")
def complete():
    return render_template("complete.html")