#from eth_keys import keys
import eth_keys, binascii

pk = eth_keys.keys.PrivateKey(b'\x01' * 32)
signature = pk.sign_msg(b'exercise-cryptography')
message = b'exercise-cryptography'

publicAddress = eth_keys.keys.PublicKey.recover_from_msg(message, signature)

print(publicAddress)