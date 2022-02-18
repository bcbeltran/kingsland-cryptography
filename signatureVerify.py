from inspect import signature
import eth_keys, binascii

msg = b'exercise-cryptography'
msgSigner = eth_keys.keys.PrivateKey(b'\x01' * 32)
signature = eth_keys.keys.Signature(binascii.unhexlify('082ee3bbc3dafc902f16f2cc7f20f37787886022002586517888e460795cfede20ffc4288225f4e665794ee639c379031cb625ea9b82a1310183e2e4f448aecc00'))

signerPubKey = signature.recover_public_key_from_msg(msg)
print('Signer public key (recovered): ', signerPubKey)

signerAddress = signerPubKey.to_checksum_address()
signer = msgSigner.public_key.to_checksum_address()

print('Signer address: ', signerAddress)
print('Signature valid?: ', signerAddress == signer)