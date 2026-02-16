A local python password manager which incorporates encryption.

## **How it works**
The application makes use of a ceasur cipher in order to encrypt the password details and reverses the ceasur to decrypt it. In terms of user encryption, the program makes use of a key generation system where it is generated at runtime and compared with the stored hash key of the master password. When the user goes to login, the hash of the given input is compared with the stored value to check they match.

![application screenshot](Interface_image.png)