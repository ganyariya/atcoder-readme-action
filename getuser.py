import requests


def get_user_and_id(gh_token):
    headers = {"Authorization": "Bearer " + gh_token}
    request = requests.post('https://api.github.com/graphql', json={'query': gh_token}, headers=headers)
    if request.status_code == 200:
        user_data = request.json()  # Execute the query
        username = user_data["data"]["viewer"]["login"]
        id = user_data["data"]["viewer"]["id"]
        return username, id
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, gh_token))
