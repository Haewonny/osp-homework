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

@app.route("/register_review_post", methods=['POST'])
def reg_review_post():
    data=request.form
    return render_template("submit_review_result.html", data=data)


@app.route("/result")
def reg_result():
    return render_template("result.html")

@app.route("/register_reviewpost")
def reg_reviewpost():
    return render_template("register_reviewpost.html")


@app.route("/submit_restaurant")
def reg_restaurant_submit():
    name = request.args.get("name")
    addr = request.args.get("addr")
    tel = request.args.get("tel")
    category = request.args.get("category")
    park = request.args.get("park")
    time = request.args.get("time")
    site = request.args.get("site")

    print(name, addr, tel, category, park, time, site)
    return render_template("register_restaurant.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
