from github import Github
from sys import argv

state = argv[-1]

if state == "online":
    msg = "🟩 Active!"
else:
    msg = "🟥 Unactive!"

g = Github("//TOKEN//")

file = "README.MD"

username = "MatrixByt3s"

repo = g.get_repo(f"{username}/{username}")
contents = repo.get_contents(file)

repo.update_file(contents.path, "update activity status", contents.decoded_content.decode().replace('[ACTIVITY]', msg), contents.sha)
