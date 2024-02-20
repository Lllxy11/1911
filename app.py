from flask import Flask, request, render_template

app = Flask(__name__)

r = ""
first_time = True

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    global r, first_time
    if first_time:
        if request.method == "POST":
            r = request.form.get("r")
            first_time = False
        return render_template("main.html", r=r)
    else:
        # Handle subsequent requests here if needed
        pass

@app.route("/image_gpt", methods=["GET", "POST"])
def image_gpt():
    return render_template("image_gpt.html")

if __name__ == "__main__":
    app.run()
