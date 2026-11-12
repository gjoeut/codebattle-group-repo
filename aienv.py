#print("AI env attempting to run script.")

import json

try:
  import requests
except ImportError as e:
  print(f"ImportError detected: {e}")

models = ["gemini-3.5-flash-lite",
         "gemini-3.5-flash",
         "gemini-3.1-flash-lite",] #use model 3.1 lite for testing


auth_Key = "oh no you dont" #i know this aint supposed to be here, but its a free key anyway
model = models[2] 
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

def checkLLM():
  print(f"CURRENTLY USING MODEL: {model}")
  
  headers = {
    "X-goog-api-key": auth_Key,
    "Content-Type": 'application/json'
  }

  params = {
    "systemInstruction": {
      "parts": [
        #change and use for the aftercheck
        {"text": "reply in two words if you are functioning"}
      ]
    },
    #user input goes here 
    "contents": [
      {"role": "user", 'parts': [{"text": "test?"}]}
    ],
    "generationConfig": {"maxOutputTokens": 512,
                         "temperature": 0.5,
                         "thinkingConfig": {"thinkingLevel": "low"}}
  }
  
  try:
    response = requests.post(url, headers=headers, json=params, timeout=15)
    #print(response.text) #debug from google api
    verify = response.raise_for_status() #raises HTTPerror/raises none 

    APIresponse = response.json()
    #cand is array format
    candidates = APIresponse["candidates"]
    
    if not candidates:
      print("There is no response to the prompt: possible timeout error")
      return None
    
    reply = candidates[0]["content"]["parts"]

    reply = "".join(["".join(p["text"]) for p in reply])
  
    print(reply)
    return True
  except Exception as e:
    print(f"There was an error: {e}")
    return False

  
