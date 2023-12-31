# Keypair Encryption
## How to use it
pre requirements: Install Cryptography
You can also try to set a virtual Enviroment before installation by
```
venv
```
First Run gen_key file to create keys one for Private and one for Public  
```
python3 gen_key.py
```
We suppose to send Public key to anyone who want to send data to us  
In this case we will export it into our memory  
```
export PEMK=./priv.pem  
export PUB_PEMK=./pub.pem  
```
You can also check the key by run read_key.py  
Now you are free to run both Encrypt and Decrypt file  
For the sender you will use public key and Encrypt.py like this
```
python3 encrypt.py [filename]
exp:python3 encrypt.py data.txt
```
For reciever you will use private key and Decrypt.py like this
```
python3 decrypt.py [filename]
exp:python3 decrypt.py data.txt
```
