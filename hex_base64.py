# Decode hex into bytes and encode into base64

from base64 import b64encode

hex_str='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

hex_to_bytes=bytes.fromhex(hex_str)

bytes_to_b64=b64encode(hex_to_bytes)

print(bytes_to_b64)
