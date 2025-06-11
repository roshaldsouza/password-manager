import requests
import hashlib

def is_password_pwned(password: str) -> bool:
    # Hash the password using SHA-1 (as required by HIBP)
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    # Query HIBP's API (k-Anonymity model)
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if response.status_code != 200:
        return False  # Assume safe if API fails

    # Check if the suffix exists in the leaked passwords
    return any(line.split(":")[0] == suffix for line in response.text.splitlines())