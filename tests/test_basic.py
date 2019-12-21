from api.models import db, Enrollment


# client passed from client - look into pytest for more info about fixtures
# test client api: http://flask.pocoo.org/docs/1.0/api/#test-client
def test_index(client):
    rs = client.get("/")
    assert rs.status_code == 200


def test_enrollment(client):
    rs = client.get("/enrollment")

    assert rs.status_code == 200
    ret_dict = rs.json  # gives you a dictionary
    assert ret_dict["success"] == True
    assert ret_dict["result"]["degrees"] == []

    # create Person and test whether it returns an enrollment
    nano_degree_enrollment = Enrollment(nanodegree_key="123")
    db.session.add(nano_degree_enrollment)
    db.session.commit()

    rs = client.get("/test")
    ret_dict = rs.json
    assert len(ret_dict["result"]["enrollments"]) == 1
    assert ret_dict["result"]["enrollments"][0]["nanodegree_key"] == "123"
