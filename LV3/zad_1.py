import pandas as pd
import numpy as np

mtcars = pd.read_csv("mtcars.csv")

#1 Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
print("Automobili s najvecom potrosnjom: ")
print(mtcars[['car','mpg']].sort_values(by = 'mpg').tail(5))

#2 Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
print("Automobili s najmanjom potrosnjom (8 cilindra)")
print(mtcars[['car','mpg','cyl']][mtcars.cyl == 8].sort_values(by = 'mpg').head(3))

#3 Kolika je srednja potrošnja automobila sa 6 cilindara?
print("Srednja potrosnja automobila (6 cilindra): ")
print(mtcars['mpg'][mtcars.cyl == 6].mean())

#4 Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
print("Srednja potrosnja automobila (4 cilindra, masa izmedju 2000 i 2200 lbs): ")
print(mtcars['mpg'][(mtcars.cyl == 4) & (mtcars.wt<=2.2) & (mtcars.wt>=2.0)].mean())

#5 Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
rucni = mtcars[mtcars.am == 1].shape[0]
automatski = mtcars[mtcars.am == 0].shape[0]
print("Broj automobila s rucnim mjenjacem: " + str(rucni))
print("Broj automobila s automatskim mjenjacem: " + str(automatski))

#6 Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
print("Broj automobila s automatskim mjenjacem i snagom preko 1000 konjskih snaga: " + str(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)].shape[0]))

#7 Kolika je masa svakog automobila u kilogramima?
mtcars['kg'] = mtcars.wt * 1000
print(mtcars[['car','kg']])