"please write a python script to extract the contents of the website https://juicysms.com/api/makeorder?key=84d68632bdcc580a68c988a73cda3bbf&serviceId=1&country=US, then wait 10 seconds, then extract the content from https://juicysms.com/api/getsms?key=84d68632bdcc580a68c988a73cda3bbf&orderId= where "orderId=" should then be populated with the 7 digit code that comes after "ORDER_ID_" in the first link's contents"

import requests
import time

# Define the initial URL
initial_url = "https://juicysms.com/api/makeorder?key=84d68632bdcc580a68c988a73cda3bbf&serviceId=1&country=US"

# Make a request to the initial URL
response = requests.get(initial_url)
initial_content = response.text

# Extract the order ID from the initial content
order_id_start = "ORDER_ID_"
order_id_end = initial_content.find("&")
order_id = initial_content[initial_content.find(order_id_start) + len(order_id_start):order_id_end]

# Wait for 10 seconds
time.sleep(10)

# Define the second URL with the extracted order ID
second_url = f"https://juicysms.com/api/getsms?key=84d68632bdcc580a68c988a73cda3bbf&orderId={order_id}"

# Make a request to the second URL
response = requests.get(second_url)
second_content = response.text

# Print the extracted content from the second URL
print(second_content)
