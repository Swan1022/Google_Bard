from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import requests
load_dotenv()

params = {
    "engine": "google_maps",
    "q": "Granite Restaurant",
    "type": "place",
    "api_key": os.getenv("SERP_API_KEY")
}
search = GoogleSearch(params)
results = search.get_dict()
print(results)
# first_place = results.get('place_results')
# if not first_place:
#     first_place = results.get('local_results')[0]
# if 'gps_coordinates' in first_place:
#     lat = first_place['gps_coordinates']['latitude']
#     lng = first_place['gps_coordinates']['longitude']
#     data_id = first_place['data_id']
#     params = {
#         "engine": "google_maps",
#         "type": "place",
#         "data": f"!4m5!3m4!1s{data_id}!8m2!3d{lat}!4d{lng}",
#         "api_key": os.getenv("SERP_API_KEY")
#     }
#     search = GoogleSearch(params)
#     results = search.get_dict()
#     print(results['search_metadata']['google_maps_url'])
#     # return results['search_metadata']['google_maps_url']
# else:
#     print("No GPS coordinates found for this place.")
