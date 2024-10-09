from flask import Blueprint, request

alarm_bp = Blueprint('alarm', __name__)

@alarm_bp.route('/alarms', methods=['GET', 'POST'])
def alarms():
    if request.method == 'GET':
        return "<p>GET, Alarms!</p>"
    if request.method == 'POST':
        return "<p>POST, Alarms!</p>"