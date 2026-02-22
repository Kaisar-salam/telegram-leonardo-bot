from flask import Flask, render_template, request
from leonardo import generate_image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None

    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            image_url = generate_image(prompt)

    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
