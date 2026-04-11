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

    df.rename(columns = { 
        'vrijeme': 'date',
        'vrijednost': 'value'
    }, inplace=True)

    df['date'] = pd.to_datetime(df['date'])

    return df


df = get_air_quality_data("Osijek", 2017)

top_dates = df.nlargest(3, 'value')[['date', 'value']]

print("Tri datuma u godini kada je koncentracija PM10 bila najveca:")
for _, row in top_dates.iterrows():
    print(f"{row['date'].date()} -> {row['value']:.2f} µg/m3")