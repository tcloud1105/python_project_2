import requests
import simplejson as json

# getting data using request
params = {"q", "pizza"}
r = requests.get("http://www.bing.com/search",params=params)
print(r.text)
f = open("./page.html",'w+')
f.write(r.text)


# posting data using request
my_data = {"name":"Cedric", "email":"kayimsavi@gmail.com"}
r = requests.post("http://www.w3schools.com/php/welcome.php", data=my_data)
f = open("myfile.html",'w+')
f.write(r.text)

# posting json objects
url="https://www.googleapis.com/urlshortener/v1/url"
payload={"longUrl":"http://example.com"}
headers={"Content_type":"application/json"}
r = requests.post(url,json=payload,headers=headers)

print(json.dumps(r.text))

print(r.headers)


