import requests
from bs4 import BeautifulSoup

# Step 1: Send GET request to fetch the form and extract CSRF token
url = 'http://localhost:8069/website/form/mail.mail'
response = requests.get(url)

# Extract CSRF token from the response
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf_token'}).get('value')

# Step 2: Construct the POST data with CSRF token and other fields
data = {
    'csrf_token': csrf_token,
    'field1': 'value1',
    'field2': 'value2',
    'email_to': 'example@example.com',
    'website_form_signature': 'some_signature_here'
    # Add other fields as needed for your Odoo form
}

# Step 3: Send the POST request with the constructed data
post_response = requests.post(url, data=data)

# Handle the response as needed
print(post_response.text)
