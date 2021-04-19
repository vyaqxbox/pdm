# pdm
This program allows you to search through the current PDM inventory to help you locate, price, and discuss vehicle(s) with a customer. 

In order to use the program, you will need all three files:
- pdm.py
- pdmCars.py
- pdmCustomers.py

Be sure to have all three of these files in the same folder. After doing so, the program is able to run off of only Python2, which is natively included in Windows.

Open command prompt on your computer, this is an example method of running the program, in which I recommend having the files in a folder titled 'pdm' on your desktop

In the command prompt enter the following commands (hitting enter after each one)
>> cd desktop 

>> cd pdm

>> python pdm.py

The first command opens your computer's desktop directory, the second opens the pdm folder containing the three files, and the third runs the main file that shows data

After the command 'python pdm.py' a new prompt should show:

Input 1 to search by name, 2 to search by price, or 3 to search by type and price:

Here, you can enter 1, 2, or 3 then hit enter. 

1: Allows you to search by vehicle keywords. After you type in the keyword, hit enter. For example, typing 'super' and hitting enter will display all of our super cars. 
You can also search by specific vehicle. For example, you can type 'charger' and hit enter, the program will display all of the vehicles we have that contain 'charger'

2: Allows you to search and display vehicles within a certain price range. When you choose this option you will be prompted to first, 

Enter lower bound for pricing:

Here, you can enter 0 or any value that you feel appropriate. For example, if you enter '50000' the program will not display any vehicles that cost less than $50,000

The second prompt will be, 

Enter lower bound for pricing:

Here, you enter the maximum amount the customer is willing to spend. For example, if you input '130000' the program will not display a vehicle that costs more
than $120,000

3: Allows you to search by vehicle keyword AND price.

For example, you can type 'suv' for the first prompt, and '40000' for the second prompt, and '120000' for the third prompt. Doing so will cause the program to 
display only suvs within the price range of $40,000 to $120,000
