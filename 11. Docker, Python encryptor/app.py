import base64

def encrypt(text):
    return base64.b64encode(text.encode()).decode()

message = "An example string being encrypted"

print(f"Original: {message}")
print(f"Encrypted: {encrypt(message)}")