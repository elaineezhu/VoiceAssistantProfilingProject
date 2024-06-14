import requests
import time
from bs4 import BeautifulSoup

# Function to extract contents from the first URL
def get_order_id(api_key, service_id, country):
    url = f"https://juicysms.com/api/makeorder?key={api_key}&serviceId={service_id}&country={country}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    order_id_text = soup.get_text()

    # order ID format is "ORDER_ID_XXXXXXX_NUMBER_XXXXXXXXXX"
    try:
        full_order_id = order_id_text.strip()
        number = full_order_id.split('NUMBER_')[-1]
        number = number[1:]
        order_id = full_order_id.split('ORDER_ID_')[1].split('_NUMBER')[0]
        return order_id, number
    except IndexError:
        print("Error: The expected format was not found in the response.")
        return None, None

# Function to extract contents from the second URL
def get_sms(api_key, order_id):
    url = f"https://juicysms.com/api/getsms?key={api_key}&orderId={order_id}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    sms_text = soup.get_text()

    return sms_text

# Function to skip the number
def skip_number(api_key, order_id):
    url = f"https://juicysms.com/api/skipnumber?key={api_key}&orderId={order_id}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    skip_response = soup.get_text()

    return skip_response

def main():
    api_key = "84d68632bdcc580a68c988a73cda3bbf"
    service_id = 1
    country = "UK"

    try:
        order_id, number = get_order_id(api_key, service_id, country)
        if order_id and number:
            print(f"Order ID: {order_id}")
            print(f"Number: {number}")

            while True:
                sms_data = get_sms(api_key, order_id)
                print("SMS Data:", sms_data)

                if "success_" in sms_data.lower():
                    digits = ''.join(filter(str.isdigit, sms_data))
                    otp = digits[-6:]
                    print(f"Code: {otp}")
                    break

                time.sleep(10)  # Wait for 10 seconds before checking again

            # Wait for 10 seconds before skipping the number
            time.sleep(10)

            # Skip the number after processing SMS
            skip_response = skip_number(api_key, order_id)
            print("Skip Number Response:", skip_response)

        else:
            print("Failed to get a valid Order ID or Number.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
