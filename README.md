# Google Places API Business Data Scraper

## Description
This script collects business names and phone numbers within a specified radius using the **Google Places API**. It ensures compliance with Google's Terms of Service while retrieving structured business data.

---

## Features
✅ Fetches business names and phone numbers  
✅ Searches within a specified radius  
✅ Uses Google’s official API (legal and reliable)  

---

## Prerequisites

### 1. Get a Google Places API Key
- Visit [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project.
- Enable the **Google Places API**.
- Generate an API key under **Credentials**.

### 2. Install Dependencies
Ensure you have Python 3 installed, then install `requests`:
```bash
pip install requests
```

---

## Usage

1. Open `script.py` and update the following variables:
```python
API_KEY = "YOUR_GOOGLE_PLACES_API_KEY"
LOCATION = "37.7749,-122.4194"  # Example: San Francisco (Latitude, Longitude)
RADIUS = 5000  # Search radius in meters (5km)
TYPE = "restaurant"  # Business type (e.g., "restaurant", "store", "cafe")
```

2. Run the script:
```bash
python script.py
```

3. The script will print business names and phone numbers if available.

---

## Example Output
```
Name: Joe's Pizza, Phone: +1 415-555-1234
Name: The Coffee Spot, Phone: +1 415-555-5678
```

---

## Important Notes
- **Billing must be enabled** on your Google Cloud account for full API access.
- The free tier has usage limits, so check Google’s pricing.
- Scraping Google Maps directly **violates Google’s Terms of Service**; this method is API-compliant.

---

### 🚀 Need Help?
Feel free to ask if you need assistance setting up the API key or modifying the script!  
