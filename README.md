# Summergeeks
A very basic management applications that handles a visitor's check-in and check-out time and notify about it.

## How to set it up in your device?

1. Clone or download the source code in your device.
2. Create a virtual enviornment in your device and activate it. If you're not familiar with virtual env. then check out this [link](https://www.geeksforgeeks.org/python-virtual-environment/) that how to create a virtual env and activate it.
3. After activating the enviornment install the requirements using command `pip install -r requirements.txt`. requirements.txt file is in home directory of source code.
4. After successfully installing the requirements go into *geeks/settings.py*.
5. At the end of file place your gmail id in EMAIL_HOST_USER(remove- *os.environ.get('EMAIL_USER2')*)variable and App password in EMAIL_HOST_PASSWORD(remove- *os.environ.get('EMAIL_PASS2')*)
6. If you don't know how to set an APP password then check-out this [link](https://devanswers.co/create-application-specific-password-gmail/). 
7. Step no-5 & 6 are for sending mails to the visitor and host.
8. After activating the python environment mentioned in step-2 run the command `python manage.py makemigrations` followed by `python manage.py migrate`
9. To run the project on your local device now run the command `python manage.py runserver`
10. Paster the url in your browser and BOOM!!! your app is ready to go.

Here are some screenshots of the app-

- Home Page

![](https://i.imgur.com/Aj5PjBl.png)

- Visitor Info

![](https://i.imgur.com/ncKeCWc.png)

- When visitor checks in

![](https://i.imgur.com/g0Xy45O.png)

- Asking for email-id when meeting ends

![](https://i.imgur.com/ivq9375.png)

- When visitor checks-out

![](https://i.imgur.com/23lkwaD.png)

- The host will recieve this mail

![mail](https://i.imgur.com/8DKMiTJ.png)

- On check-out this is mail that visitor will recieve

![recieve](https://i.imgur.com/WDOWRUh.png)

## Technology Stack-
- Django
- db.sqlite
- SMTP

The mail used in here is just for test purpose. Thank you.
