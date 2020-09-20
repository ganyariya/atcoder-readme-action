import re
import os
import base64
import json

import requests

from github import Github, InputGitAuthor
from dotenv import load_dotenv
from getuser import get_user_and_id

load_dotenv()

START_COMMENT = '<!--START_SECTION:action-->'
END_COMMENT = '<!--END_SECTION:action-->'
START_COMMENT = '<!--START_SECTION:waka-->'
END_COMMENT = '<!--END_SECTION:waka-->'
LIST_REG = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
gh_token = os.getenv('INPUT_GH_TOKEN')

print(gh_token)


def get_readme_content_as_text(data: str):
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, 'utf-8')


def generate_new_readme(new_text: str, readme: str):
    stats_in_readme = f"{START_COMMENT}\n{new_text}\n{END_COMMENT}"
    return re.sub(LIST_REG, stats_in_readme, readme)


if __name__ == '__main__':
    try:
        if gh_token is None:
            raise Exception('Token not available')
        github = Github(gh_token)
        username = "Ganariya"
        repo = github.get_repo(f"{username}/{username}")
        readme_contents = repo.get_readme()
        readme_blob = readme_contents.content
        old_readme_text = get_readme_content_as_text(readme_blob)

        # this is we want the text!!!
        insert_text = "hello"

        new_readme_text = generate_new_readme(insert_text, old_readme_text)
        committer = InputGitAuthor('readme-bot', 'readme-bot@example.com')

        # repo.update_file(path=readme_contents.path, message="Updated README by bot", content=new_readme_text, sha=readme_contents.sha, branch='master', committer=committer)
        print("Readme Updated!")

    except Exception as e:
        print("Exception Occurred " + str(e))
