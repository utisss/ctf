from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64decode


raw_cipher_data = b64decode("jUUcwVvv1vV7bF5KfKllc+BrtWuzm6BsIhYAtpC6aXkMG4FfdTa8i7a+DKjxx5/Mm25l8yq2Lxx4wxzIYuk1Yu76PAnzxg/tfVDwRsOPjpAaEDClczUuShEkL5Q7hTZ+oOyJRLRzL8ShgZ0jn70hSczVV4pqAhiE+epAeEupxfASs//ABMKXRscKv9Y2GTr5JDxhVtezCGqo4AQlqgZEjot9UNVMzjzqAx2uww3MlwO4CydeGdQjnW0zefcdBqXXUpMGlo1URPoW+jNTdkECaPoknBMipQ2uf5gMkNVL0bdel2As2RfO0hCF0p3xzgfrXF6ZkbnCl/6TtYFu/3Ht8c7GXf/twpjdaHSFOvTMShjSSdbe/hi/wZjYGZHLje/NH+r/uIhPCyVi8VPlKds3pA34ILGOKmmvKbCweYccX2ll2XobaWJNYl112ffzaufM1wIXkjVQirgDA2ELsAtE/GYXWXcZtOw/KiCMNBCPWOSV3FBgtdlb5Us7Sr/TqcXmm7JY02/RVPcXr7aEky9MoW3zH8+z/KhUhoQXvF5+yHewzz7hU3f/OMR7Vz8D78HKNBmfhyy++7ejtqKwJgBjgG4Yd7aFahxpN2ghgtu0R4Z0QssPyjFGb95NDw7mWi+ixR7pj86isIEdGa33ftjlJJMG2CIcwgGCY6hjVoWLxQM=")


for i in range(19, -1, -1):
    temp = RSA.importKey(open('priv'+str(i)+'.pem', "rb").read())
    verifier = PKCS1_v1_5.new(temp)
    raw_cipher_data = temp.decrypt(raw_cipher_data)
    print i

print raw_cipher_data
