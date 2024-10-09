from flask import Blueprint, request

device_bp = Blueprint('device', __name__)

@device_bp.route('/devices', methods=['GET', 'POST'])
def devices():
    if request.method == 'GET':
        return "<p>GET, Devices!</p>"
    if request.method == 'POST':
        return "<p>POST, Devices!</p>"