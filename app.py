from flask import Flask, request, render_template
import replicate
import os

app = Flask(__name__)
os.environ["REPLICATE_API_TOKEN"] = "r8_YCkY5TTYO4H6Vu2IH9Navg8JezCJBqx3sDOM1"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["POST"])
def main():
    r = request.form.get("r")
    return render_template("main.html", r=r)

@app.route("/image_gpt", methods=["GET", "POST"])
def image_gpt():
    return render_template("image_gpt.html")

@app.route("/image_result", methods=["POST"])
def image_result():
    q = request.form.get("q")
    try:
        r = replicate.run(
            "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
            input={"prompt": q}
        )
        # 这里可以根据 replicate.run() 的返回值处理结果
        return render_template("image_result.html", r=r[0])
    except Exception as e:
        # 异常处理，可以返回一个错误页面或者信息
        return render_template("error.html", error=str(e))

@app.route("/end", methods=["GET", "POST"])
def end():
    return render_template("end.html")

if __name__ == "__main__":
    app.run(debug=True)
