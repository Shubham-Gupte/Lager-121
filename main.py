import time
# Gathers inputs and data from the User
def main():
    print("Hello World!")
    time.sleep(1)
    investment_amount = int(input("How much do you want to invest? $USD only please. ex: $500 \n").strip('$'))

if __name__ == "__main__":
    main()
