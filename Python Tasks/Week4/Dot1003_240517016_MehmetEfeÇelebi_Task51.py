yazi = "The quick brown fox jumps over the lazy dog"
devam = True
while devam:
    aranan = input("What are you looking for?")
    
    if aranan == "-1":
        print("Bye.")
        devam = False
    else:
        gösterge = yazi.find(aranan)

        if gösterge == -1:
            print("not found")
        else:
            print(f"found it at{gösterge}")    

    
