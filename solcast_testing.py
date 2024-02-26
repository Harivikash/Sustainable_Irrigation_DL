import requests

url = "https://solcast.p.rapidapi.com/radiation/forecasts"

querystring = {"api_key":"NjbZ5J8NkvqaNQDQmsGV5fKd7Xfe_sQb","latitude":"13.0547890","longitude":"80.2193408","format":"json"}

headers = {
	"X-RapidAPI-Key": "3dd3b5a980msh85edf0076358f52p11611djsn22de1be49218",
	"X-RapidAPI-Host": "solcast.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())