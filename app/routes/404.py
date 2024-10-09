from flask import redirect, Blueprint

error_page_bp = Blueprint('404', __name__)

### ERROR HANDLERS ###
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/'), 404