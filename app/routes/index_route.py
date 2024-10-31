from flask import Blueprint, request

index_bp = Blueprint('/', __name__)

@index_bp.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return "<p>GET, ROOT!</p>"