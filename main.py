import sys
from client import SecureApiClient

def display_menu():
    print("\n=== Secure API Fetcher (NASA APOD Edition) ===")
    print("1. Fetch Astronomy Picture (Today or by Date)")
    print("2. Exit")

def main():
    try:
        api_client = SecureApiClient()
    except ValueError as e:
        print(e)
        sys.exit(1)
        
    while True:
        display_menu()
        choice = input("\nSelect an option (1-2): ").strip()
        
        if choice == "1":
            query = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            
            print(f"\nFetching NASA APOD data...")
            data = api_client.fetch_data(query)
            
            if data:
                title = data.get("title", "N/A")
                date = data.get("date", "N/A")
                explanation = data.get("explanation", "No explanation provided.")
                hd_url = data.get("hdurl", data.get("url", "N/A"))
                media_type = data.get("media_type", "image")
                
                print("\n" + "=" * 60)
                print(f"🌌 NASA APOD Report: {title}")
                print("=" * 60)
                print(f"📅 Date       : {date}")
                print(f"📷 Media Type : {media_type.capitalize()}")
                print(f"🔗 Image URL  : {hd_url}")
                print("-" * 60)
                print(f"📖 Explanation:\n{explanation}")
                print("=" * 60)
            else:
                print("⚠️ Failed to retrieve data. Please check your date format (YYYY-MM-DD) or network connection.")
            
        elif choice == "2":
            print("👋 Exiting program. Clear skies!")
            sys.exit(0)
        else:
            print("⚠️ Invalid input. Enter 1 or 2.")

if __name__ == "__main__":
    main()