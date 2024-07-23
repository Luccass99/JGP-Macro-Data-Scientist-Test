
import pandas as pd

def analyze_relationship():
    # Carrega os dados do arquivo CSV
    df = pd.read_csv('inflation_data.csv', index_col='date', parse_dates=True)

    # Calcula a correlação entre 'Todos os itens' e 'Gasolina'
    correlation = df['CPI Todos os itens, ajustado sazonalmente'].corr(df['CPI Gasolina (todos os tipos), ajustado sazonalmente'])
    print(f"A correlação entre 'Todos os itens' e 'Gasolina' é: {correlation}")

    # Salva o resultado em um arquivo de texto
    with open('correlation_result.txt', 'w') as file:
        file.write(f"A correlação entre 'Todos os itens' e 'Gasolina' é: {correlation}")

if __name__ == "__main__":
    analyze_relationship()
