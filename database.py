import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def insert_restaurant(self, rname, data, img_path):
        restaurant_info = {
        "cate": data['cate'],
        "park": data['park'],
        "addr": data['addr'],
        "tel": data['tel'],
        "price1": data['price1'],
        "price2": data['price2'],
        "time": data['time'],
        "site": data['site'],
        "img_path": img_path
        }
        if self.restaurant_duplicate_check(rname):
            self.db.child("restaurant").child(rname).set(restaurant_info)
            print(data, img_path)
            return True
        else:
            return False
        self.db.child("restaurant").child(rname).set(restaurant_info)
        print(data, img_path)
        return True

    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:
                return False
            return True