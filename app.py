from hvac import Client
from os import environ

vault_addr  = environ.get("VAULT_ADDR")
vault_token = environ.get("VAULT_TOKEN")
secret_path = environ.get("VAULT_SECRET_PATH")

assert vault_addr is not None, "There is no Environment Variable 'VAULT_ADDR'! Please Set this variable"
assert vault_token is not None, "There is no Environment Variable 'VAULT_TOKEN'! Please Set this variable"
assert secret_path is not None, "There is no Environment Variable 'VAULT_SECRET_PATH'! Please Set this variable"

client = Client(
    url=vault_addr,
    token=vault_token
)

secret = client.secrets.kv.read_secret_version(path=secret_path)

print(secret['data']['data'])