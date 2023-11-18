from jwt import decode, encode
def create_token(data: dict) -> str:
    token: str = encode(data.dict(), key='my_secret_key',  algorithm='HS256')
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token.strip(), key="my_secret_key", algorithms="HS256")
    return data