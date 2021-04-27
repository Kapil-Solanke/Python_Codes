import requests

r = requests.get(
    "https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp#:~:text=NumPy%20is%20used%20to%20work,using%20the%20array()%20function.")

#  get request is to get the content from a URL  and bring it to your program
print(r.text)

#  post request has an API endpoint and we have to send some data. Endpoint is an URL
