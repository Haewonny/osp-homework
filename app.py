from flask import Flask, render_template, request
from database import DBhandler
import sys

app = Flask(__name__)

DB = DBhandler()

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
    data = request.form
    print(data)
    return render_template("result_review.html", data=data)


@app.route("/register_reviewpost")
def reg_reviewpost():
    return render_template("result_review.html")


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
    img1 = request.args.get("img1")
    img2 = request.args.get("img2")
    print(rname, cate, park, addr, tel, price1, price2, time, site, bestmenuname, bestmenuprice)
    return render_template("register_restaurant.html")


@app.route("/result", methods=['POST'])
def result_post():
    image_file1 = request.files["file1"]
    image_file1.save("static/img/{}".format(image_file1.filename))
    image_file2 = request.files["file2"]
    image_file2.save("static/img/{}".format(image_file2.filename))
    data = request.form
    print(image_file1, image_file2, data)
    return render_template("result.html", data=data)

@app.route("/register_menu", methods=['POST'])
def reg_menu():
    data=request.form
    print(data)
    return render_template("register_menu.html", data=data)

@app.route("/result", methods=['POST'])
def reg_restaurant_submit_post():
    global idx
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    if DB.insert_restaurant(data['name'], data, image_file.filename):
        return render_template("result.html", data=data, image_path="static/img/" + image_file.filename)
    else:
        return "이미 등록된 가게입니다."


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
