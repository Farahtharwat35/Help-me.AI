import webbrowser

def Enter():
    print("Entered Navigation")

def navigate(from_dest, to_dest):
    locations = {
        "home": "30.1008209,31.3490139",
        "work": "30.0926529,31.3840992"
    }

    from_dest = locations[from_dest]
    to_dest = locations[to_dest]
    loc = {from_dest, to_dest}
    middle = findMiddle(loc)
    url = f"https://www.google.com/maps/dir/{from_dest}/{to_dest}/@{middle},14z"
    webbrowser.open_new_tab(url)


def findMiddle(Location):
    x1 = list(Location)
    y1 = x1[0].split(",")
    x2 = list(Location)
    y2 = x2[1].split(",")
    middle = str((float(y1[0]) + float(y2[0])) / 2) + "," + str((float(y1[1]) + float(y2[1])) / 2)
    return middle