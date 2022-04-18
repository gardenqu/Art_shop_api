from src.flaskdr import create_app
from dotenv import load_dotenv,find_dotenv
a=find_dotenv("../.env")
load_dotenv(a)


app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
