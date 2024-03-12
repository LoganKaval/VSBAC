import webbrowser

times = int(input("How Many Accounts Do You Want to Open?:"))
code = input("What is the Blooket Code?:")

# Launching Browser, Entering Code, and Making Usr

for number in range(times):
    webbrowser.open_new("https://play.blooket.com/play")
