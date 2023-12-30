#!/home/rhyme/penv/bin/python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


import sys, os

if (len(sys.argv)) != 2:
    print ('Usage: ./encrypt.py original_filename')
    exit(-1)

# open Original file in binary mode
with open(sys.argv[1], 'rb') as org_file:
    org_data = org_file.read()

# get the public key filename form enviroment varibles
pub_pem = os.environ.get('PUB_PEMK')

with open(pub_pem, 'rb') as pub_key_file:
    # De-serialize it back to an object  in public key
    public_key = serialization.load_pem_public_key(
        pub_key_file.read()
    )


encrypted = public_key.encrypt(
    org_data,
    padding.OAEP( #Optimal Asymmetric Encryption padding should be used in RSA Encryption
    #mask generation function (mgf) produce a mask that associated with the size of the input data
    #hashes.SHA256() produce a hash to check that sent massage is
    #unaltered but in itself is of fixed size(256 bits)

    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
    )
)

with open(sys.argv[1]+'.encrypted','wb') as file:
    file.write(encrypted) #DAta
