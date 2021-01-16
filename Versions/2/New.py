import wget

a = input("Enter a Url: ")
b = input("Enter a File name: ")
print("Tip no periods")
c = input("Enter a File extension: ")

print("Beginning file download...")
wget.download(a, '/Users/moran/OneDrive/Desktop/Python/Internet-Downloader/Downloads/' + str(b) + "." + str(c))
print("Done")
