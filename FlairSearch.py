from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # This line brings all environment variables from .env into os.environ
    print(os.environ['VONAGE_API'])

if __name__ == "__main__":
    main()
