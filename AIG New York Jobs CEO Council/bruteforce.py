from zipfile import ZipFile, BadZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password): 
    try:
        zf_handle.extractall(pwd=password.encode('utf-8'))
        return True 
    except RuntimeError:
        return False
    except BadZipFile:
        print("Bad zip file. It might be corrupted.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
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
                    print(f"[+] Success! The password is: {password.decode('utf-8')}")
                    return
                else:
                    print(f"[-] Failed attempt with password: {password.decode('utf-8')}")
    #print("[+] Password not found in list")
        print("[+] Password not found in list")
        
if __name__ == "__main__":
    main()



