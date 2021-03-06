import json

from flask import Blueprint

health_blueprint = Blueprint(name='health', import_name=__name__)


@health_blueprint.route('/health')
def health():
    return json.dumps({'status': 'healthy'})
