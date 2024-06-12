import requests
import time

# Function to extract contents from the first URL
def get_order_id(api_key, service_id, country):
    url = f"https://juicysms.com/api/makeorder?key={api_key}&serviceId={service_id}&country={country}"
    response = requests.get(url)
    response.raise_for_status()
    try:
        data = response.json()
        # Assuming the order ID is in the format "ORDER_ID_xxxxxxx"
        order_id = data['order_id'].split('_')[-1]
        return order_id
    except ValueError:
        # If the response is not JSON, return the text content
        print("Error: Response is not in JSON format")
        return response.text

# Function to extract contents from the second URL
def get_sms(api_key, order_id):
    url = f"https://juicysms.com/api/getsms?key={api_key}&orderId={order_id}"
    response = requests.get(url)
    response.raise_for_status()
    try:
        data = response.json()
        return data
    except ValueError:
        # If the response is not JSON, return the text content
        print("Error: Response is not in JSON format")
        return response.text

def main():
    api_key = "84d68632bdcc580a68c988a73cda3bbf"
    service_id = 1
    country = "US"

    try:
        order_id = get_order_id(api_key, service_id, country)
        if isinstance(order_id, str) and order_id.startswith("ORDER_ID_"):
            print(f"Order ID: {order_id}")
            
            time.sleep(10)  # Wait for 10 seconds
            
            sms_data = get_sms(api_key, order_id)
            print("SMS Data:", sms_data)
        else:
            print("Failed to get a valid Order ID.")
            print("Response text:", order_id)
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()