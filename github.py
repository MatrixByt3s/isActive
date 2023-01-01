import base64
import requests
import json

state = "online"
if state == "online":
    msg = "🟩 Active!"
else:
    msg = "🟥 Unactive!"

name, repo = "0x1-omnidev", "0x1-omnidev"

base_url = f"https://api.github.com/repos/{name}/{repo}"

token = ""

headers = {
    "accept": "application/vnd.github+json",
    "authorization": "Bearer " + token,
}

def get_sha(file_path):
    result = requests.get(f"{base_url}/contents/{file_path}",
        headers = headers
    )
    sha = json.loads(result.text)["sha"]
    return sha

with open('README.md', 'r', encoding="utf-8") as file:
    result = requests.put(f"{base_url}/contents/README.md",
        headers = headers,

        json = {
            "message": "Update activity status",
            "content": base64.b64encode(file.read().replace("[ACTIVITY]", msg).encode("utf-8")).decode("ascii"),
            "sha": get_sha("README.md"),
        }
    )
