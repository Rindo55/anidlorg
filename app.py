import requests

# Define the URL of your WordPress site and the post ID you want to edit
wordpress_url = 'https://anidl.org/wp-json/wp/v2/posts/'
post_id = 195300  # Replace 1 with the ID of the post you want to edit

# Set your WordPress username and password
username = 'pirateuserx@gmail.com'
password = 'tDLORU24rKBW)7A0AE%hwHoq'

# Set the new content for the post
new_content = {
    'title': 'Test',  # Replace with your new title
    'content': 'Nothing',  # Replace with your new content
}

# Authenticate and get an authentication token
auth_response = requests.post(
    wordpress_url + 'jwt-auth/v1/token',
    data={'username': username, 'password': password}
)
auth_response.raise_for_status()
token = auth_response.json()['token']

# Set the headers with the authentication token
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}

# Send the request to update the post
update_response = requests.post(
    wordpress_url + str(post_id),
    headers=headers,
    json=new_content
)
update_response.raise_for_status()

print('Post updated successfully!')
