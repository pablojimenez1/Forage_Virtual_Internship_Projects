from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password): 
    try:
        zf_handle.extractall(pwd=password)
        return True 
    except RuntimeError:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Write your logic here...
            for line in f:
                password = line.strip()
            # Attempt to extract the zip file using each password
                if attempt_extract(zf, password):
            # Handle correct password extract versus incorrect password attempt)
                    print("[+] Success! The password is: %s" % password)
                    exit (0)
                else:
                    print("[-] Failed attempt with password: %s" % password)
                    
        print("[+] Password not found in list")
        
if __name__ == "__main__":
    main()



