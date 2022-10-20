from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

# Generar llaves
eth_k = generate_eth_key()

# Privada
sk_hex = eth_k.to_hex()

# Pública
pk_hex = eth_k.public_key.to_hex()

data = b"Hola mundo cruel"

print("pub key:", pk_hex, "\n")
print("priv key:", sk_hex, "\n")
print(encrypt(pk_hex, data), "\n")
print(decrypt(sk_hex, encrypt(pk_hex, data)))
