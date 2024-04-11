import requests

# Authentication credentials
username = 'pirateuserx@gmail.com'
password = 'tDLORU24rKBW)7A0AE%hwHoq'
base_url = 'https://anidl.org/wp-json/wp/v2/posts'

# Post ID to update
post_id = 195300

# Endpoint for updating the post
endpoint = f'{base_url}/{post_id}'

# Existing and new download links
existing_links = """
DDL Ep.07\t: https://anidl.ddlserverv1.me.in/dl/HECqsj2MYiR4rQQtvuwWLN4sLSvORnFoKyCZFARiIApivVXfAe
DDL Ep.08\t: https://anidl.ddlserverv1.me.in/dl/8dv36MYw9kiuILe7WDAMnR0HqcR7g4E24SMLZ9XclGLyWDMrac
DDL Ep.09\t: https://anidl.ddlserverv1.me.in/dl/dPhW3FxFPnG742Bx73ek96Znpt83jrs6gdKppuVZxD3j8zOYBv
DDL Ep.10\t: https://anidl.ddlserverv1.me.in/dl/JOU8tCndyJZgUu22QfAqvOtb5LUiKIAYM1xouMzBPhysvyVD7j
DDL Ep.11\t: https://anidl.ddlserverv1.me.in/dl/1sC6i2Q4yNRozEELHPgqxN24OoZhW6VKN9nN6swpMGcVsJfLNN
DDL Ep.12\t: https://anidl.ddlserverv1.me.in/dl/NZ02m1obbpv7pTrympmppR5nYXeptw1gsCeRzHAfwy0p3VkatT
"""

new_link = "DDL Ep.13\t: https://anidl.ddlserverv1.me.in/dl/newlink"

# Updated content for Episode 13
updated_content = f"""
<p>Ep.013\t: <a href="https://anidl.ddlserverv1.me.in/dl/testlink">Download Link</a></p>

{existing_links}
{new_link}
"""

# Data to be sent in the update request
update_data = {
    'content': updated_content
}

# Send POST request with authentication to update the post
response = requests.post(endpoint, json=update_data, auth=(username, password))

# Handle response
if response.status_code == 200:
    print('Post updated successfully.')
else:
    print('Failed to update post:', response.status_code, response.text)
  
