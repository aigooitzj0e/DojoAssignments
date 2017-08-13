import md5
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))
password = "password"

hashed_password = md5.new(password).hexdigest()
print hashed_password + salt
