## **About**
This is a mock banking application which makes use of an online API as well as a GUI interface. Within this program, I have made use of a Supabase database API to store and retrieve data as well as develop a simple GUI. I have also used my past experiences with .env files, try and except blocks and encryption techniques to improve my project. I have also began to explore classes and creating methods and attributes.

## **How it works**
- A Supabase backend for data storage such as username, password and account balance
- Improved encryption algorithm for secure data storage as well as hashing for secure password storing
- Tkinter GUI interface for user interactions
- Use of classes to hold user information
- Use of .env files to hold sensitive information such as supabase url and key

## **How to make it work**
You will need to create a Supabase account and setup a .env file in the following mannor:  

SUPABASE_URL=""  
SUPABASE_KEY=""  
encryption_key=""  

key=""  
iv=""  

## **Screenshot**
Login interface
![application screenshot](\images\login_interface.png)
Sign up interface
![application screenshot](\images\signup_interface.png)
Username taken
![application screenshot](\images\username_taken.png)
Main interface
![application screenshot](\images\main_interface.png)
Sending money
![application screenshot](\images\successful_send.png)
Invalud funds
![application screenshot](\images\invalid_funds.png)
Supabase screenshots
![application screenshot](\images\supabase_users.png)
![application screenshot](\images\supabase_balance.png)

## **Limitations and future development**
In this iteration, I did not need to make use of the decrypt function. I have included it in case I decide to use the encrypt and decrypt functions in future developments. I would also have to look into sanitising my user inputs, especially in amount inputs as currently users can enter negative amounts and non-integer values which can break the program.