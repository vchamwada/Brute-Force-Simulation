from zipfile import ZipFile, BadZipFile
import sys

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except RuntimeError:
        return False
    except BadZipFile:
        print("The zip file is corrupted.")
        sys.exit(1)

def main():
    print("[+] Beginning bruteforce ")
    try:
        with ZipFile('enc.zip') as zf:
            with open('rockyou.txt', 'rb') as f:
                for line in f:
                    password = line.strip()
                    if attempt_extract(zf, password):
                        print(f"[+] Password found: {password.decode()}")
                        return
                    else:
                        print(f"[-] Attempted password: {password.decode()}")
        print("[+] Password not found in list")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
