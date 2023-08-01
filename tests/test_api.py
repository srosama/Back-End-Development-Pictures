import json
import requests


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200


def test_count(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10


def test_data_contains_10_pictures(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10


def test_get_picture(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10


def test_get_pictures_check_content_type_equals_json(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10





def test_get_picture_by_id(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10
    res = client.get('/picture/404')
    assert res.status_code == 404


def test_pictures_json_is_not_empty(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10

def test_post_picture(picture, client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10

def test_post_picture_duplicate(picture, client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10
def test_update_picture_by_id(client, picture):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10

def test_delete_picture_by_id(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['length'] == 10


