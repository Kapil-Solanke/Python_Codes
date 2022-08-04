import requests

r = requests.get(
    "https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp#:~:text=NumPy%20is%20used%20to%20work,using%20the%20array()%20function.")

# get request is an url and the browser saves it in its history
#  get request is to get the content from a URL  and bring it to your program
print(r.text)
print(r.status_code)  # search status_code in google
#  post request has an API endpoint and we have to send some data. Endpoint is an URL

url = "www.something.com"
data = {
    "p1": 4,
    "p2": 5
}

r2 = requests.post(url=url, data=data)
