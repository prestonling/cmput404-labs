import requests as r

if __name__ == "__main__":
    # requests does redirects on its own
    print(r.get("http://www.google.com/"))
