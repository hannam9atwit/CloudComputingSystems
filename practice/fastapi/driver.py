import requests


def driver():
    print("hello")

    continueToLoop = True
    while continueToLoop:
        print("0: Exit")
        print("1: Hello World")
        command = input("Enter your choice: ")
        if command == "0":
            continueToLoop = False
        if command == "1":
            url = "http://127.0.0.1:8000"
            response = requests.get(url)
            print("the response is:", response.json())

driver()