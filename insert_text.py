import requests
from pybadges import badge

result_to_color = {
    'AC': 'brightgreen',
    'WA': 'yellow',
    'TLE': 'yellow',
    'CE': 'yellow',
    'IE': 'lightgrey',
    'OLE': 'yellow',
    'MLE': 'yellow'
}


def make_insert_text(ATCODER_ACCOUNT):
    url = f"https://kenkoooo.com/atcoder/atcoder-api/results?user={ATCODER_ACCOUNT}"
    json_data = requests.get(url).json()
    json_data.sort(key=lambda x: x['epoch_second'])
    json_data.reverse()

    ret_text = "#### Recently Solved Problems\n"

    for i in range(min(len(json_data), 10)):
        data = json_data[i]
        contest = data['contest_id']
        problem = data['problem_id']
        result = data['result']
        point = data['point']
        language = data['language']
        iid = data['id']
        url = f"https://atcoder.jp/contests/{contest}/submissions/{iid}"
        p = problem.replace("_", "").upper()

        text = f"[![Badge](https://img.shields.io/static/v1?label={p}%20{str(point)[:-2]}&message={result}&color={result_to_color[result]})]({url})\n"
        ret_text += text

    return ret_text
