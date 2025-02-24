import requests

API_KEY = "YOUR_GOOGLE_PLACES_API_KEY"
LOCATION = "37.7749,-122.4194"  # Latitude,Longitude (San Francisco example)
RADIUS = 5000  # In meters (5km)
TYPE = "restaurant"  # Change to your desired business type

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LOCATION}&radius={RADIUS}&type={TYPE}&key={API_KEY}"
response = requests.get(url).json()

for place in response.get("results", []):
    place_id = place["place_id"]
    details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_phone_number&key={API_KEY}"
    details_response = requests.get(details_url).json()
    
    name = details_response.get("result", {}).get("name")
    phone = details_response.get("result", {}).get("formatted_phone_number")

    if name and phone:
        print(f"Name: {name}, Phone: {phone}")
