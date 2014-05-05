from flask import Flask
app = Flask(__name__)
app.config.from_object(__name__)

import flask_config
app.config.update(flask_config.config)

from flask import request, jsonify, g


@app.route("/currency/api/1/debit", methods=["POST"])
def debit():
    '''
    Subtract money from the user's account according to their usage of
    some device or service.  Accepts JSON of the following form:

    {"card_id": "060135FD07", "device_name": "some-device-specific-name",
     "timestamp": "2014-05-04T23:29:30Z", "minutes_passed": 1}
    '''
    # TODO: Inspect authentication type, then authenticate accordingly

    # Retrieve from MySQL the Card for given card_id

    # Retrieve Account corresponding to Card

    # Retrieve cost per minute for given Device by device_name

    # balance -= minutes_passed * cost_per_minute
    return jsonify(error="TODO"), 500


if __name__ == "__main__":
    app.run()
