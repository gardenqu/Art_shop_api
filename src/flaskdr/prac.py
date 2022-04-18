import os
from dotenv import load_dotenv,find_dotenv

a=find_dotenv("/../home/nay/Documents/project/api/.env")


load_dotenv(a)

print(f'{os.getenv("DB_HOST")}')