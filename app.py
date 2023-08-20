
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""


from flask import Flask, render_template, request

app = Flask(__name__)

# Mapping of symptoms to AI responses
ai_responses = {
    "Fever": "You might have a fever. Get plenty of rest and drink fluids.",
    "Cough": "A persistent cough could indicate various conditions. Consult a doctor if it persists.",
    "Fatigue": "Feeling tired? Make sure you're getting enough sleep and maintaining a balanced diet.",
    "Headache": "Headaches can have multiple causes. Try relaxing and staying hydrated.",
    "Nausea": "Nausea can be caused by various factors. Consider eating light and staying hydrated.",
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    response = None
    if request.method == "POST":
        symptoms = [
            request.form["symptom1"],
            request.form["symptom2"],
            request.form["symptom3"],
            request.form["symptom4"],
            request.form["symptom5"]
        ]
        result = ", ".join(symptoms)
        result = result.replace(' ,','')

        # Basic AI response based on symptoms
        response = get_ai_response(symptoms)

    return render_template("index.html", result=result, response=response)

def get_ai_response(symptoms):
    ai_response = "AI response will be here."
    for symptom in symptoms:
        if symptom in ai_responses:
            ai_response = ai_responses[symptom]
            break
    return ai_response

if __name__ == "__main__":
    app.run()













































