import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv("mtcars.csv")

fig, axs = plt.subplots(2, 2, figsize = (15, 10))

#1
axs[0, 0].bar(['4 cilindra', '6 cilindara', '8 cilindara'], mtcars.groupby('cyl')['mpg'].mean(), color = ['blue', 'green', 'red'])
axs[0, 0].set_title('Prosjecna potrosnja goriva po broju cilindara')
axs[0, 0].set_xlabel('Broj cilindara')
axs[0, 0].set_ylabel('Prosjecna potrosnja goriva')

#2
mtcars.boxplot(column = 'wt', by = 'cyl', ax = axs[0, 1])
axs[0, 1].set_title('Distribucija tezine po broju cilindara')
axs[0, 1].set_xlabel('Broj cilindara')
axs[0, 1].set_ylabel('Tezina')

#3
mtcars.groupby('am')['mpg'].mean().plot(kind = 'bar', color = ['blue', 'red'], ax = axs[1, 0])
axs[1, 0].set_title('Prosjecna potrosnja goriva za automobile s rucnim i automatskim mjenjacem')
axs[1, 0].set_xlabel('Tip mjenjaca')
axs[1, 0].set_ylabel('Prosjecna potrosnja goriva')
axs[1, 0].set_xticks([0, 1], ['Rucni', 'Automatski'])

#4
axs[1, 1].scatter(mtcars[mtcars['am'] == 1]['hp'], mtcars[mtcars['am'] == 1]['qsec'], color = 'blue', label = 'Automatski')
axs[1, 1].scatter(mtcars[mtcars['am'] == 0]['hp'], mtcars[mtcars['am'] == 0]['qsec'], color = 'red', label = 'Ručni')
axs[1, 1].set_title('Odnos ubrzanja i snage za automobile s rucnim i automatskim mjenjacem')
axs[1, 1].set_xlabel('Snaga')
axs[1, 1].set_ylabel('Ubrzanje')

plt.tight_layout()
plt.show()