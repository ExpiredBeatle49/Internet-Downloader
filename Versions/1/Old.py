import urllib.request

a = input("Enter the url: ")
print('Beginning file download...')
urllib.request.urlretrieve(a, 'C:\Users\moran\OneDrive\Desktop\Python\Internet-Downloader\Downloads\test.jpg')
print('Done')
exit()
