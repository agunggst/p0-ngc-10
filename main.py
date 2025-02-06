from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

data = {
  "New York City": {
    "temperature": "10˚C",
    "condition": "Cloudy",
  },
  "Los Angeles": {
    "temperature": "20˚C",
    "condition": "Sunny",
  },
  "Chicago": {
    "temperature": "15˚C",
    "condition": "Cloudy",
  },
}

user_login = {
  '1': {
    'name': 'John',
    'password': '12345'
  }
}

API_KEY = '1234apikey456'

@app.get('/')
def root():
  return {
    'message': 'Welcome!',
    'menu': {
      '1': '/weather/<location> to get weather',
      '2': '/authenticate to get access to API Key'
    }
  }

@app.get('/weather/{location}')
def get_weather(location: str, api_key: str = Header(None)):
  if api_key is None or api_key != API_KEY:
    raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to read data!")
  else:
    return data[location]
  
@app.post('/authenticate')
def login(added_item: dict):
  is_authenticated = False
  for item in user_login:
    if user_login[item]['name'] == added_item['name'] and user_login[item]['password'] == added_item['password']:
      is_authenticated = True
      break
  if is_authenticated:
    return {
      'api_key': API_KEY
    }
  else:
    raise HTTPException(status_code=404, detail="User not found!")