try:
    from flask import Blueprint, request
    from api.models import db, Enrollment
    from api.core import create_response, serialize_list, logger
    from sqlalchemy import inspect
    from flasgger import swag_from
except Exception as e:
    print("some modules are missing {}".format(e))

main = Blueprint("main", __name__)  # initialize blueprint


# function that is called when you visit /
@main.route("/")
def index():
    # you are now in the current application context with the main.route decorator
    # access the logger with the logger from api.core and uses the standard logging module
    # try using ipdb here :) you can inject yourself
    logger.info("Hello World!")
    return "<h1>Hello World!</h1>"


# function that is called when you visit /enrollments
@main.route("/test", methods=["GET"])
@swag_from('testEnrollments.yml')
def get_enrollments():
    enrollments = Enrollment.query.all()
    return create_response(data={"enrollments": serialize_list(enrollments)})


# POST request for /enrollment
@main.route("/enrollment", methods=["POST"])
@swag_from('Enrollment.yml')
def create_enrollment():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "nanodegree_key" not in data:
        msg = "No nanodegree_key provided for Enrollment."
        logger.info(msg)
        return create_response(status=422, message=msg)
    # if "udacity_user_key" not in data:
    #     msg = "No udacity_user_key provided for Enrollment."
    #     logger.info(msg)
    #     return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    nano_degree_key = data["nanodegree_key"]

    new_enrollment = Enrollment(nanodegree_key=nano_degree_key)

    # commit it to database
    db.session.add(new_enrollment)
    db.session.commit()
    return create_response(
        message=f"Successfully created Enrollment for dummy user  with course id: {nano_degree_key}"
    )
