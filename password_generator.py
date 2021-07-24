import string
import random
if __name__ == '__main__':
    s1 = string.ascii_letters
    s2 = string.ascii_lowercase
    s3 = string.ascii_uppercase
    s4 = string.digits
    s5 = string.punctuation
    while True:
        try:
            plen=int(input("Enter the password\n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    #random.shuffle(s)
    #print("".join(s[0:plen]))
    print("Your Password is:")
    print("".join(random.sample(s,plen)))

