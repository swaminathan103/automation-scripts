"""
NOTE - PLEASE MAINTAIN THE INDENDATION

Add the relevant details in the placeholders given below
run using python work.py or python3 work.py
"""

import os, sys, webbrowser

def main(argv):
    appPaths = [
        #EG (for mac): "/Applications/Slack.app"
        "<path to app 1>",
        "<path to app 2>",
        "<path to app 3>"
    ]

    webURLs = [
        #EG: "https://www.google.com/"
        "<path to url 1>",
        "<path to url 2>",
        "<path to url 3>"
    ]

    if (argv.lower() == "s"):
        for path in appPaths:
            os.system("open " + path)
        for url in webURLs:
            webbrowser.open(url)
    elif (argv.lower() == "c"):
        for path in appPaths:
            appName = os.path.basename(os.path.normpath(os.path.splitext(path)[0]))
            appName = appName.replace("\\", "")
            print(appName)
            os.system("osascript -e \'quit app \"{}\"\'".format(appName))

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("args needed")
        exit()
    main(sys.argv[1])