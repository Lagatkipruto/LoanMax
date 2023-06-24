import os
import secrets

secret_key = secrets.token_hex(10)
os.environ['SECRET_KEY'] = secret_key
