import requests
import json

# define payload
nutri = json.dumps({
    "model": "mistral:7b",
    "prompt": "",
    "stream": False
})

# function sand request
def generate_json_data():
    # define header so the server knows we are sanding JSON data
    headerlist = {
        "accept": "*/*",
        "content-Type": "application/json"
    }

    # sand a post request
    r = requests.post(
        url="http://localhost:11434/api/generate",
        headers= headerlist,
        data= nutri
    )

    # Return the text response from the AI
    return r.json()["response"]