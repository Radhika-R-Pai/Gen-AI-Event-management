from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="YOUR_API_KEY_HERE")

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""
    if request.method == "POST":
        user_query = request.form["query"]
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert event management assistant"},
                {"role": "user", "content": user_query}
            ]
        )
        response_text = response.choices[0].message.content

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
