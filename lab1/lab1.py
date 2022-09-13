import requests as r

if __name__ == "__main__":
    # requests does redirects on its own
    print(r.get("http://www.google.com/"))
    print(r.get("https://raw.githubusercontent.com/prestonling/cmput404-labs/main/lab1/lab1.py"))
