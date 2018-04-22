from flask import Blueprint

index_blueprint = Blueprint(name='index', import_name=__name__)


@index_blueprint.route('/')
def health():
    return "<h1>Placeholder</h1>"