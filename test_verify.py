import hashlib
import os

def verify():
    output_path = "/output/entry.txt"
    
    # Run main.py twice
    os.system("python3 main.py")
    with open(output_path, "rb") as f:
        h1 = hashlib.sha256(f.read()).hexdigest()
        
    os.system("python3 main.py")
    with open(output_path, "rb") as f:
        h2 = hashlib.sha256(f.read()).hexdigest()
        
    with open(output_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    match_hash = (h1 == h2)
    valid_len = (1 <= len(content) <= 199)
    utf8_ok = True
    try:
        content.encode("utf-8")
    except Exception:
        utf8_ok = False
        
    no_trailing_newline = not content.endswith("\n")
    
    match_all = match_hash and valid_len and utf8_ok and no_trailing_newline
    print(f"Match: {match_all}")

if __name__ == "__main__":
    verify()
