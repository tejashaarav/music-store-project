class MusicStore:
    def __init__(self,listOfAlbums):
        self.showAlbums = listOfAlbums
    def displayAlbums(self):
        print("the available Albums are: ")
        for Album in self.showAlbums:
            print(Album)
    def buyalbum(self,albumName):
        if albumName in self.showAlbums:
            print("take the album its so good")
            self.showAlbums.remove(albumName)
        else:
            print("this album isn't available come after a week")
    def returnalbum(self,returnalbum):
        if returnalbum in self.showAlbums:
            print("we already have another copy")
        else:
            self.showAlbums.append(returnalbum)
            print("thank you have a nice day")





class Students:
    def requestalbum(self):
        self.album = input("which album do you want")
        return self.album
    def returnalbum(self):
        self.album = input("which album do you wanna return")
        return self.album

    





Jlb_Records = MusicStore(["cold mess", "Afterhours", "Carrie and Lowell", "Fineline", "Anuv Jain"])
student = Students()


while True:
    welcome_message = "welcome to JLB RECORDS\n choose a service:\n 1.show all available albums\n 2.rent a specific album\n 3. return an album\n 4. exit the library\n "
    print(welcome_message)
    
   
    a = int(input("enter a choice\n"))
    
    if a == 1:
        Jlb_Records.displayAlbums()
    elif a ==2:
        Jlb_Records.buyalbum(input("which album do you wanna buy"))
    elif a ==3:
        Jlb_Records.returnalbum(input("which album do you wanna return"))
    elif a ==4 :
        print("Thanks for visiting our store")
        break
    else:
        print("invalid operation")

