import requests

url = "https://gpxz-elevation.p.rapidapi.com/v1/elevation/point"

querystring = {"lat":"34.1390884","lon":"-118.7942219","bathymetry":"true"}

headers = {
	"X-RapidAPI-Host": "gpxz-elevation.p.rapidapi.com",
	"X-RapidAPI-Key": "ae9a9016ddmsh82dfd6b68984452p1af8a7jsnc14b5593aa6c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)