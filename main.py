import re
import os
import base64
import json

import requests

from insert_text import make_insert_text
from github import Github, InputGitAuthor
from dotenv import load_dotenv

load_dotenv()

START_COMMENT = '<!--START_SECTION:custom_action-->'
END_COMMENT = '<!--END_SECTION:custom_action-->'
UPDATE_REG = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"

GH_TOKEN = os.getenv('INPUT_GH_TOKEN')
USERNAME = os.getenv('INPUT_USERNAME')
ATCODER_ACCOUNT = os.getenv('INPUT_ATCODER_ACCOUNT')


def get_readme_content_as_text(data: str):
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, 'utf-8')


def generate_new_readme(new_text: str, readme: str):
    stats_in_readme = f"{START_COMMENT}\n{new_text}\n{END_COMMENT}"
    return re.sub(UPDATE_REG, stats_in_readme, readme)


if __name__ == '__main__':
    try:
        if GH_TOKEN is None:
            raise Exception('Token not available')
        github = Github(GH_TOKEN)
        repo = github.get_repo(f"{USERNAME}/{USERNAME}")
        readme_contents = repo.get_readme()
        readme_blob = readme_contents.content
        old_readme_text = get_readme_content_as_text(readme_blob)

        # this is the text which we want to insert!
        insert_text = make_insert_text(ATCODER_ACCOUNT)

        new_readme_text = generate_new_readme(insert_text, old_readme_text)
        committer = InputGitAuthor('readme-bot', 'readme-bot@example.com')
        print(new_readme_text)

        repo.update_file(path=readme_contents.path, message="Updated README by bot", content=new_readme_text, sha=readme_contents.sha, branch='main', committer=committer)
        print("Readme Updated!")

    except Exception as e:
        print("Exception Occurred " + str(e))
