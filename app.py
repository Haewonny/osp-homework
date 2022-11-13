from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import sys

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


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

@app.route("/register_restaurant")
def reg_restaurant():
    rname = request.args.get("rname")
    cate = request.args.get("cate")
    park = request.args.get("park")
    addr = request.args.get("addr")
    tel = request.args.get("tel")
    price1 = request.args.get("price1")
    price2 = request.args.get("price2")
    time = request.args.get("time")
    site = request.args.get("site")
    bestmenuname = request.args.get("bestmenuname")
    bestmenuprice = request.args.get("bestmenuprice")
    print(rname, cate, park, addr, tel, price1, price2, time, site, bestmenuname, bestmenuprice)
    return render_template("register_restaurant.html")

@app.route("/result", methods=['POST'])
def result_post():
	data=request.form
	return render_template("result.html", data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
