# Example python app to get Vault secret

This is example Python app to get secret from Vault server

To runn this app you need set below environment variables:

VAULT_ADDR          - IP Address of Vault server e.g 'http://127.0.0.1:8200'

VAULT_TOKEN         - Token for Vault Authentication

VAULT_SECRET_PATH   - Secret path in vault e.g if secret has path 'secret/mysecret/pass' then provide '/mysecret/pass' 

file "devwebapp.yaml" contains manifest file for POD which will connect to external vault server

## PlayBook

1. Instal Vault, docker, kubectl, minikube

2. Run vault wit bellow command:

```md
vault server -dev -dev-root-token-id root -dev-listen-address 0.0.0.0:8200
```

3. export Vault Address for vault CLI:
```md
export VAULT_ADDR=http://0.0.0.0:8200
```

4. Login to vault as root:
```md
vault login root
```

5. Set example secret in vault:
```md
vault kv put secret/devwebapp/config username='giraffe' password='salsa'
```

6. Start minikube:
```md
minikube start
```

7. Login to minikube:
```md
minikube ssh
```

8. Check IP of minikube host it will be required further to set addess of external vout server usualy it is 192.168.65.2:
```md
dig +short host.docker.internal 
```

9. Exit from minikube ssh:
```md
exit
```

10. Deploy example POD from this repo:
```md
kubectl apply -f devwebapp.yaml
```

11. Now you can check pod logs displays secret configured in valut:
```md
kubectl logs devwebapp
```

![Screen](https://raw.githubusercontent.com/HubGab-Git/vault_python/main/Screenshot16.57.48.png)