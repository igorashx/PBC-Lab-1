import requests
from bs4 import BeautifulSoup

DOC_URL = "https://docs.google.com/document/d/1tC_VkoBOzXVpkqHe47dqKGUE-zFmBkAZ/edit?usp=sharing&ouid=102727259188757353982&rtpof=true&sd=true"

try:
    response = requests.get(DOC_URL, timeout=10)

    print(f"Status code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    print(f"Dimensiune răspuns: {len(response.text)} bytes")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "Necunoscut"

        print("\n=== Informații generale ===")
        print(f"Titlu pagină: {title}")
        print(f"URL final: {response.url}")

    elif response.status_code in (401, 403):
        print("Acces restricționat.")
    else:
        print("Documentul nu a putut fi accesat.")

except Exception as e:
    print(f"Eroare: {e}")