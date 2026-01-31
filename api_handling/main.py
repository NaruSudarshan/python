import requests

def fetch_quote():
    r = requests.get('https://api.freeapi.app/api/v1/public/quotes/quote/random')

    data = r.json()

    if data["success"] and "data" in data:
        quote_data = data["data"]
        quote_text = quote_data["content"]
        print(f"Random Quote: {quote_text}")
    else:
        print("Failed to retrieve quote.")
        
def main():
    fetch_quote()
    
if __name__ == "__main__":
    main()