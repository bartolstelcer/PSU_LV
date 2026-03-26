"""

# 1.

import pandas as pd
import numpy as np

mtcars = pd.read_csv("mtcars.csv")

#1 Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
print("Automobili s najvecom potrosnjom: ")
print(mtcars[['car','mpg']].sort_values(by='mpg').tail(5))

#2 Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
print("Automobili s najmanjom potrosnjom (8 cilindra)")
print(mtcars[['car','mpg','cyl']][mtcars.cyl == 8].sort_values(by='mpg').head(3))

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
"""

"""
# 2.

import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv("mtcars.csv")

fig, axs = plt.subplots(2, 2, figsize=(15, 10))

#1
axs[0, 0].bar(['4 cilindra', '6 cilindara', '8 cilindara'], mtcars.groupby('cyl')['mpg'].mean(), color=['blue', 'green', 'red'])
axs[0, 0].set_title('Prosjecna potrosnja goriva po broju cilindara')
axs[0, 0].set_xlabel('Broj cilindara')
axs[0, 0].set_ylabel('Prosjecna potrosnja goriva')

#2
mtcars.boxplot(column='wt', by='cyl', ax=axs[0, 1])
axs[0, 1].set_title('Distribucija tezine po broju cilindara')
axs[0, 1].set_xlabel('Broj cilindara')
axs[0, 1].set_ylabel('Tezina')

#3
mtcars.groupby('am')['mpg'].mean().plot(kind='bar', color=['blue', 'red'], ax=axs[1, 0])
axs[1, 0].set_title('Prosjecna potrosnja goriva za automobile s rucnim i automatskim mjenjacem')
axs[1, 0].set_xlabel('Tip mjenjaca')
axs[1, 0].set_ylabel('Prosjecna potrosnja goriva')
axs[1, 0].set_xticks([0, 1], ['Rucni', 'Automatski'])

#4
axs[1, 1].scatter(mtcars[mtcars['am'] == 1]['hp'], mtcars[mtcars['am'] == 1]['qsec'], color='blue', label='Automatski')
axs[1, 1].scatter(mtcars[mtcars['am'] == 0]['hp'], mtcars[mtcars['am'] == 0]['qsec'], color='red', label='Ručni')
axs[1, 1].set_title('Odnos ubrzanja i snage za automobile s rucnim i automatskim mjenjacem')
axs[1, 1].set_xlabel('Snaga')
axs[1, 1].set_ylabel('Ubrzanje')

plt.tight_layout()
plt.show()
"""

import requests
import pandas as pd

def get_air_quality_data(city, year):

    url = "https://iszz.azo.hr/iskzl/rs/podatak/export/json?polutant=5&postaja=160&tipPodatka=4&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Greska: {response.status_code}")

    try:
        data = response.json()
    except:
        print("Odgovor nije JSON:")
        print(response.text[:300])
        raise

    df = pd.DataFrame(data)

    df.rename(columns={
        'vrijeme': 'date',
        'vrijednost': 'value'
    }, inplace=True)

    df['date'] = pd.to_datetime(df['date'])

    return df


df = get_air_quality_data("Osijek", 2017)

top_dates = df.nlargest(3, 'value')[['date', 'value']]

print("Tri datuma u godini kada je koncentracija PM10 bila najveća:")
for _, row in top_dates.iterrows():
    print(f"{row['date'].date()} -> {row['value']:.2f} µg/m3")





