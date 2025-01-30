import requests
import param_screen as ps

def main():
    #check if github release is more recent

    ps.start_param_screen()

def check_update():
    response = requests.get("https://api.github.com/repos/v2ray/v2ray-core/releases/latest")
    print(response.json()["name"])

if __name__ == "__main__":
    main()
