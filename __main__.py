import sys
from time import sleep
from tkinter import Tk
from tkinter import filedialog
import csv
from magnet_link import magnet_from_LB_URL
from qbittorrent import Client

if __name__ == "__main__":

    root = Tk()
    root.withdraw()
    root.update()
    print("Please select the file of your list")
    sleep(2)
    csv_filepath = filedialog.askopenfilename(initialdir="/", title="Select list file", filetypes=[("csv files", "*.csv")])
    print("Please select directory for the  result")
    directory1 = filedialog.askdirectory(initialdir="/", title="Select target directory")
    with open(csv_filepath) as csv_file, open(directory1 + "/magnets.txt", 'w') as res:
        movies = csv.reader(csv_file, delimiter=",")
        while not (movie := next(movies)) or not movie[2].isnumeric(): pass #skip until the movies start
        magnet = magnet_from_LB_URL(movie[3])
        res.write(magnet + "\n")
        print(movie[1] + ": " + magnet)
        for movie in movies:
            magnet = magnet_from_LB_URL(movie[3])
            res.write(magnet + "\n")
            print(movie[1] + ": " + magnet)
    res = input("Do you want to download the torrents?[Y/N]")
    if res == "N": sys.exit()
    root = Tk()
    root.withdraw()
    root.update()
    directory2 = filedialog.askdirectory(initialdir="/", title="Select target directory")
    qb = Client("http://127.0.0.1:8080/")
    qb.login("admin", "administrator")
    with open(directory1 + "/magnets.txt", 'r') as magnets:
        for magnet in magnets:
            qb.download_from_link(magnet, savepath=directory2)
