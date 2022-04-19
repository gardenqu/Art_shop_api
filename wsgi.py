import os
from src.flaskdr import create_app
from dotenv import load_dotenv
load_dotenv()





app = create_app()

if __name__ == "__main__":
    app.run(host= f'{os.getenv("ec2")}', port=5002)
