from flask import Blueprint, request

video_bp = Blueprint('video', __name__)

@video_bp.route('/videos', methods=['GET', 'POST'])
def videos():
    if request.method == 'GET':
        return "<p>GET, Videos!</p>"
    if request.method == 'POST':
        return "<p>POST, Videos!</p>"