import os
from dotenv import load_dotenv
from supabase import create_client, Client

def get_client() -> Client:
    load_dotenv()  # loads SUPABASE_URL and SUPABASE_KEY from .env
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY in .env")
    return create_client(url, key)

def main():
    supabase = get_client()

    # Replace "volleyball_matches" with your actual table name
    response = supabase.table("volleyball_matches").select("*").limit(5).execute()

    print("Rows:")
    for row in response.data:
        print(row)

if __name__ == "__main__":
    main()
