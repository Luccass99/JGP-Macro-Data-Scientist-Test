
from fastapi import FastAPI, HTTPException
import pandas as pd
from typing import List, Dict, Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Para acessar os dados, vá para /data"}

@app.get("/data", response_model=List[Dict[str, Union[str, float, int]]])
def get_data():
    try:
        # Carrega os dados do arquivo CSV
        df = pd.read_csv('inflation_data.csv')
        # Converte o DataFrame para uma lista de dicionários
        data = df.to_dict(orient='records')
        return data
    except Exception as e:
        # Log de erro para depuração
        print(f"Erro ao carregar os dados: {e}")
        raise HTTPException(status_code=500, detail="Erro ao carregar os dados")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
