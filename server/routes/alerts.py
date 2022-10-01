from flask import Blueprint, jsonify, request
from util.database import database

routes_alerts = Blueprint('routes_alerts', __name__, url_prefix='/api/alerts')


@routes_alerts.route('/addRecipient', methods=['POST'], strict_slashes=False)
def addRecipient():
    try:
        sessionToken = request.headers.get('Authorization').replace("Token ", "").replace("Bearer ", "")
    except Exception as e:
        return jsonify({'Error': 'No Bearer', 'Message': str(e)}), 401

    session = database["sessions"].find_one({"sessionToken": sessionToken})

    if session is None:
        return jsonify({"status": 401, "message": "session not found"})

    findUserQuery = database["users"].find_one({"userID": session.get("userID")})

    userID = findUserQuery.get("userID")

    try:
        req = request.get_json()
    except Exception as e:
        return jsonify({'Error': 'Invalid JSON', 'Message': str(e)}), 401

    email = req.get('email')
    firstName = req.get('firstName')
    lastName = req.get('lastName')
    phoneNumber = req.get('phoneNumber')

    database["alerts"].insert_one({"email": email, "firstName": firstName, "lastName": lastName,
                                   "phoneNumber": phoneNumber, "senderID": userID})

    return jsonify({'status': '200'}), 200


@routes_alerts.route('/', methods=['GET'], strict_slashes=False)
def getAlerts():
    try:
        sessionToken = request.headers.get('Authorization').replace("Token ", "").replace("Bearer ", "")
    except Exception as e:
        return jsonify({'Error': 'No Bearer', 'Message': str(e)}), 401

    session = database["sessions"].find_one({"sessionToken": sessionToken})

    if session is None:
        return jsonify({"status": 401, "message": "session not found"})

    findAlertsQuery = database["alerts"].find({"senderID": session.get("userID")}, {"_id": False})
    findAlertsQuery = list(findAlertsQuery)

    return jsonify(findAlertsQuery)

