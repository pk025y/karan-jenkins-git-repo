#!/bin/bash

# Prompt user for password to encrypt
read -s -p "Enter the password to encrypt: " password
echo

# Prompt user for a key to use for encryption
read -s -p "Enter the encryption key: " key
echo

# Encrypt the password using OpenSSL and AES-256
echo -n "$password" | openssl enc -aes-256-cbc -a -salt -pass pass:"$key" > encrypted_password.txt

echo "Password encrypted and saved to encrypted_password.txt"

