from flask import Blueprint, jsonify, request
from util.database import database
from twilio.rest import Client
from decouple import config

routes_twilio = Blueprint('routes_twilio', __name__, url_prefix='/api/twilio')


@routes_twilio.route('/sendAlerts', methods=['POST'], strict_slashes=False)
def sendAlerts():
    try:
        sessionToken = request.headers.get('Authorization').replace("Token ", "").replace("Bearer ", "")
    except Exception as e:
        return jsonify({'Error': 'No Bearer', 'Message': str(e)}), 401

    session = database["sessions"].find_one({"sessionToken": sessionToken})

    if session is None:
        return jsonify({"status": 401, "message": "session not found"})

    findAlertsQuery = database["alerts"].find({"senderID": session.get("userID")}, {"_id": False})
    findAlertsQuery = list(findAlertsQuery)

    try:
        req = request.get_json()
    except Exception as e:
        return jsonify({'Error': 'Invalid JSON', 'Message': str(e)}), 401

    alert = req.get('alert')

    if config("MODE") != "SANDBOX":
        account_sid = config('TWILIO_ACCOUNT_SID')
        auth_token = config('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        for r in findAlertsQuery:
            message = client.messages.create(
                body=alert,
                from_='+' + config('TWILIO_NUMBER'),
                to='+' + r.get("phoneNumber")
            )

    print("alerts sent")

    return jsonify({"status": "sent to all recepients"})
