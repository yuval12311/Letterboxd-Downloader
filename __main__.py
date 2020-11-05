from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import csv
from magnet_link import magnet_from_LB_URL

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.update()
    print("Please select the file of your list")
    sleep(2)
    csv_filepath = askopenfilename(initialdir="/", title="Select list file", filetypes=[("csv files", "*.csv")])
    print("Please select directory for the  result")
    direcory = askdirectory(initialdir="/", title="Select target directory")
    with open(csv_filepath) as csv_file, open(direcory + "/magnets.txt", 'w') as res:
        movies = csv.reader(csv_file, delimiter=",")
        while not (movie := next(movies)) or not movie[2].isnumeric(): pass #skip until the movies start
        magnet = magnet_from_LB_URL(movie[3])
        res.write(magnet + "\n")
        print(magnet)
        for movie in movies:
            magnet = magnet_from_LB_URL(movie[3])
            res.write(magnet + "\n")
            print(magnet)

