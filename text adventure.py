print("""
TEXT ADVENTURE - Alpha 1.0
======type any key to start and type Q to quit======
""")
startgame=input(">  ")

if startgame=="Q" or startgame=="q":
    import time
    time.sleep(3600)

else:
    print("THE ADVENTURE HAS STARTED!")
    import time
    print("loading assets...")
    time.sleep(1)
    print("making a few tweaks...")
    time.sleep(1)
    print("you have loaded in!")
