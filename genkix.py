# This python program generates ssh-keys
# Extract public key for use on servers such as github
# Copy your public key and past it where ever its required
# The diverse, the safer

import subprocess
import os

generate_key = subprocess.run(["ssh-keygen", "-o"])

print("\nHere is your key:\n")
print("==================================================================================\n")
hereIsThekey = os.system("cat ~/.ssh/id_rsa.pub")
print("==================================================================================\n")