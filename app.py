from flask import Flask, render_template, request
import sys

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/register_restaurant")
def reg_restaurant():
    return render_template("register_restaurant.html")


@app.route("/register_review")
def reg_review():
    nickname = request.args.get("nickname")
    menu = request.args.get("menu")
    star = request.args.get("star")
    content = request.args.get("content")

    print(nickname, menu, star, content)
    return render_template("register_review.html")

@app.route("/register_reviewpost", methods=['POST'])
def reg_review_post():
    data=request.form
    return render_template("register_reviewpost.html", data=data)


@app.route("/register_reviewpost")
def reg_reviewpost():
    return render_template("register_reviewpost.html")


@app.route("/result")
def reg_restaurant_submit_result():
	data=request.form
	return render_template("result.html", data=data)

@app.route("/result", methods=['POST'])
def reg_restaurant_submit_result_img():
    image_file = request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    return render_template("result.html", image_file=image_file)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
