from flask import Flask, request, render_template
import replicate
import os
import time
from openai import OpenAI

model = OpenAI(api_key="sess-QJbVC96XEyR4YEKR5yj0Ga0kWGF6SOMR1YTmiVqH")
os.environ["REPLICATE_API_TOKEN"]="r8_YCkY5TTYO4H6Vu2IH9Navg8JezCJBqx3sDOM1"

app = Flask(__name__)

r = ""
first_time = 1

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    global r, first_time
    if first_time == 1:
        r = request.form.get("r")
        first_time = 0
    return render_template("main.html", r=r)

@app.route("/image_gpt", methods=["GET", "POST"])
def image_gpt():
    return render_template("image_gpt.html")

@app.route("/image_result", methods=["GET", "POST"])
def image_result():
     q = request.form.get("q")
     r = replicate.run(
     "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
     input={
         "prompt":q,
         }
     )
     time.sleep(10)
     return(render_template("image_result.html",r=r[0]))

@app.route("/text_gpt", methods=["GET", "POST"])
def text_gpt():
    return render_template("text_gpt.html")
     
@app.route("/text_result", methods=["GET", "POST"])
def text_result():
    q = request.form.get("q")
    r = model.chat.completions.create(
      model = "gpt-3.5-turbo",
      messages=[
        {
        "role" : "user",
        "content" : q
        }
      ]
    )
     time.sleep(5)
     return(render_template("text_result.html",r=r.choices[0].message.content))
     
@app.route("/about_ntu", methods=["GET", "POST"])
def about_ntu():
    return render_template("about_ntu.html")

@app.route("/image_ntu", methods=["GET", "POST"])
def about_ntu():
    return render_template("image_ntu.html")

@app.route("/text_ntu", methods=["GET", "POST"])
def about_ntu():
    return render_template("text_ntu.html")


@app.route("/end", methods=["GET", "POST"])
def end():
    global first_time
    first_time = 1
    return render_template("end.html")

if __name__ == "__main__":
    app.run()
