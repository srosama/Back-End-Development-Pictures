from . import app
import os
import json
import random
from flask import abort
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    picList = []
    cont =0
    for i, dic in enumerate(data):
        picList.append(dic["pic_url"])
    return picList
    makeMeJson= jsonify(data=picList)

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
        for i, dic in enumerate(data):
            if dic['id'] == id:
                tackMe = jsonify(id=dic["id"])
                return tackMe, 200
            elif id == 404:
                return abort(404)




# "http://dummyimage.com/230x100.png/dddddd/000000"
@app.route("/picture", methods=["POST"])
def create_picture():
    # Add new random nubmer for the img
    width = random.randint(150,1905)
    hight = random.randint(150,1950)
    data.append('testChecl')
    return data



@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    pass


@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    pass
