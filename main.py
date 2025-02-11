import requests
import param_screen as ps

local_version = "0.0"

def main():
    check_update()
    ps.start_param_screen()


def check_update():
    response = requests.get(
        "https://api.github.com/repos/AlexFioriniSinergia/Software-fori/releases"
    )

    if response.status_code == 200:
        releases = response.json()
        if releases:
            latest_release = releases[0]
            prelease = latest_release["prerelease"]
            git_version = latest_release["tag_name"]
            if prelease:
                if git_version != local_version:
                    print(f"Aggiornamento disponibile: {latest_release['name']}")
        else:
            print("Nessun file disponibile.")
    else:
        print(f"Errore nella ricerca di aggiornamenti: {response.status_code}")

if __name__ == "__main__":
    main()
