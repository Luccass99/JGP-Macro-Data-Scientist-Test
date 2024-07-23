
import pandas as pd
import plotly.express as px

def plot_inflation():
    # Carrega os dados do arquivo CSV
    df = pd.read_csv('inflation_data.csv', index_col='date', parse_dates=True)

    # Calcula a variação percentual ano a ano
    df['YoY Change'] = df['CPI Todos os itens, exceto alimentos e energia, ajustado sazonalmente'].pct_change(12) * 100

    # Remove valores NaN
    df = df.dropna()

    # Cria o gráfico
    fig = px.line(df, x=df.index, y='YoY Change', title='Year-over-Year Change in CPI (All items, less food and energy)')
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Percentage Change')

    # Salva o gráfico como um arquivo HTML
    fig.write_html('inflation_chart.html')
    print("Gráfico salvo como inflation_chart.html")

if __name__ == "__main__":
    plot_inflation()
