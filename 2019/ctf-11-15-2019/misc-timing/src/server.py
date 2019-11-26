from secret import flag
import time

if __name__ == '__main__':
    while True:
        print("Send me a thankful string: ")
        user_input = input()

        # Validate
        start = time.time()
        for i in range(len(user_input)):
            if user_input[i] == flag[i]:
                time.sleep(.05)
        end = time.time()
        print("Thankfulness rating:", end - start)
        print()
