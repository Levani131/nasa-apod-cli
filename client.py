import os
import requests
from dotenv import load_dotenv

# Load environment variables from the project configuration file
load_dotenv("NasaAPI.env")

class SecureApiClient:
    def __init__(self):
        self.api_key = os.getenv("NASA_API_KEY")
        
        if not self.api_key:
            raise ValueError("❌ API Key not found! Please check your .env file.")
        
        self.base_url = "https://api.nasa.gov/planetary"
        self.session = requests.Session()
        
        self.session.headers.update({
            "Accept": "application/json"
        })

    def fetch_data(self, query: str = ""):
        """Executes a secured GET request to the NASA APOD API. 
        (Query can be left blank for today's image, or pass a YYYY-MM-DD date)."""
        endpoint = f"{self.base_url}/apod"
        
        params = {
            "api_key": self.api_key
        }
        if query:
            params["date"] = query
        
        try:
            response = self.session.get(endpoint, params=params, timeout=10)
            
            response.raise_for_status()
            return response.json()
            
        except requests.RequestException as error:
            print(f"[Network Error]: Could not contact the API. Details: {error}")
            return None