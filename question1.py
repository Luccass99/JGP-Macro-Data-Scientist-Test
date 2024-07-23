
import requests
import pandas as pd
import json

# URL da API do BLS e o endpoint específico
BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
API_KEY = "64538ea894ff411c8abec18c26a646a7"

# IDs das séries a serem obtidas (corrigidos)
series_ids = {
    "CUSR0000SA0": "CPI Todos os itens, ajustado sazonalmente",
    "CUSR0000SA0L1E": "CPI Todos os itens, exceto alimentos e energia, ajustado sazonalmente",
    "CUSR0000SETB01": "CPI Gasolina (todos os tipos), ajustado sazonalmente"
}

# Parâmetros para o período de tempo
START_YEAR = "2019"
END_YEAR = "2024"

def fetch_bls_data(series_id, api_key):
    headers = {'Content-type': 'application/json'}
    data = json.dumps({
        "seriesid": [series_id],
        "startyear": START_YEAR,
        "endyear": END_YEAR,
        "registrationkey": api_key
    })
    response = requests.post(BLS_API_URL, headers=headers, data=data)
    print(response.status_code)
    print(response.text)  # Adicione esta linha para imprimir a resposta completa da API
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def process_data(data):
    series = data['Results']['series'][0]
    df = pd.DataFrame(series['data'])
    print(df.head())  # Adicione esta linha para imprimir o DataFrame e verificar a estrutura
    if 'year' in df.columns and 'period' in df.columns:
        df['date'] = pd.to_datetime(df['year'] + df['period'].str[1:] + '01')
        df.set_index('date', inplace=True)
        df = df.sort_index()
        df = df[['value']].astype(float)
        return df
    else:
        raise KeyError("'year' or 'period' column not found in the data")

def main():
    all_data = []
    for series_id, description in series_ids.items():
        data = fetch_bls_data(series_id, API_KEY)
        print(data)  # Adicione esta linha para imprimir os dados brutos
        df = process_data(data)
        df.columns = [description]
        all_data.append(df)
    
    final_df = pd.concat(all_data, axis=1)
    final_df.to_csv('inflation_data.csv')
    print("Arquivo inflation_data.csv criado com sucesso.")

if __name__ == "__main__":
    main()
