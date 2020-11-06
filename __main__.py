import sys
from time import sleep
from tkinter import Tk
from tkinter import filedialog
import csv
from magnet_link import magnet_from_LB_URL, NotFoundError
from qbittorrent import Client
from termcolor import colored


def handle_movie(movie):
    global magnet
    try:
        magnet = magnet_from_LB_URL(movie[3])
        res.write(magnet + "\n")
        print(colored("Found: ", "green") + movie[1])
    except NotFoundError:
        print(colored("Not Found: ", "red") + movie[1])
        failed.append(movie[1])


if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.update()
    print("Please select the file of your list")
    sleep(2)
    csv_filepath = filedialog.askopenfilename(initialdir="/", title="Select list file",
                                              filetypes=[("csv files", "*.csv")])
    print("Please select directory for the result")
    directory1 = filedialog.askdirectory(initialdir="/", title="Select target directory")
    failed = []
    with open(csv_filepath) as csv_file, open(directory1 + "/magnets.txt", 'w') as res:
        movies = csv.reader(csv_file, delimiter=",")
        while not (movie := next(movies)) or not movie[2].isnumeric(): pass  # skip until the movies start
        handle_movie(movie)
        for movie in movies:
            handle_movie(movie)

    print("Here's the movies I couldn't find:")
    print("\n\t" + "\n\t".join(failed))
    print("Select target directory")
    directory2 = filedialog.askdirectory(initialdir="/", title="Select target directory")
    qb = Client("http://127.0.0.1:8080/")
    qb.login("admin", "administrator")
    with open(directory1 + "/magnets.txt", 'r') as magnets:
        for magnet in magnets:
            qb.download_from_link(magnet, savepath=directory2)
