from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    search_res = []
    if 'id' in args:
        search_res = [user for user in USERS if user['id'] == args['id']]
    if 'name' in args:
        search_res += [user for user in USERS if args['name'].lower() in user['name'].lower() if user not in search_res]
    if 'age' in args: 
        search_res += [user for user in USERS if int(args['age']) + 1 >= user['age'] and int(args['age']) - 1 <= user['age'] if user not in search_res]
    if 'occupation' in args:
        search_res += [user for user in USERS if args['occupation'].lower() in user['occupation'].lower() if user not in search_res]

    return search_res
