import requests

# URL where the form data is submitted
submit_url = 'https://example.com/submit_vote'  # <-- Replace with actual form action URL

# Data payload for the form (this must match what the form expects)
payload = {
    'candidate': 'Chayce Han, Boulder Creek, Sr.',  # Replace with actual form field name
    # Add other required form fields here
}

# Optional headers (like user-agent)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    # Add other headers if necessary
}

session = requests.Session()

# Send POST request to submit vote
response = session.post(submit_url, data=payload, headers=headers)

if response.status_code == 200:
    print("Vote submitted successfully.")
else:
    print(f"Failed to submit vote. Status code: {response.status_code}")