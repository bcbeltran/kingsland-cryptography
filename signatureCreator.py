from eth_keys import keys
pk = keys.PrivateKey(b'\x01' * 32)

print('Private key (64 hex digits):', pk)
signature = pk.sign_msg(b'exercise-cryptography')
print('Signature: [v = {0}, r = {1}, s = {2}]'.format(
  hex(signature.v), hex(signature.r), hex(signature.s)))
print('Signature (130 hex digits):', signature)