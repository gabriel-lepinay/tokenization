import requests

def main():
    try:
        response = requests.get("http://127.0.0.1:8000/tokenize/Hello%20World")
        print(response.json())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()