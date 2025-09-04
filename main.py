# 📦 Importação das bibliotecas necessárias
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import requests
import matplotlib.pyplot as plt

# 🔍 Função para buscar dados da API CoinGecko
def buscar_dados(cripto_id):
    """
    Consulta os dados de preço dos últimos 7 dias para uma criptomoeda específica
    usando a API do CoinGecko. Agrupa os dados por data e calcula a média diária
    para evitar duplicatas.

    Parâmetros:
        cripto_id (str): ID da criptomoeda conforme definido pela API.

    Retorno:
        pd.DataFrame: Tabela com colunas 'date' e 'price' (média diária).
    """
    url = f"https://api.coingecko.com/api/v3/coins/{cripto_id}/market_chart"
    params = {
        "vs_currency": "usd",     # Moeda de referência: dólar americano
        "days": "7",              # Últimos 7 dias
        "interval": "daily"       # Intervalo diário
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    dados = response.json()
    precos = dados['prices']  # Lista de [timestamp, preço]

    # Cria DataFrame e converte timestamp para data
    df = pd.DataFrame(precos, columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms').dt.date

    # Agrupa por data e calcula média dos preços
    df_agrupado = df.groupby('date', as_index=False)['price'].mean()

    return df_agrupado

# 📁 Função para gerar e salvar o relatório em CSV
def gerar_csv():
    """
    Gera um arquivo CSV com os dados da criptomoeda selecionada.
    """
    cripto = combo.get()
    if not cripto:
        messagebox.showwarning("Atenção", "Selecione uma criptomoeda.")
        return

    try:
        df = buscar_dados(cripto)
        nome_arquivo = f"{cripto}_relatorio.csv"
        df.to_csv(nome_arquivo, sep=';', index=False)
        messagebox.showinfo("Sucesso", f"Relatório salvo como '{nome_arquivo}'!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar CSV:\n{e}")

# 📊 Função para visualizar gráfico de preços
def visualizar_grafico():
    """
    Exibe um gráfico de linha com os preços da criptomoeda nos últimos 7 dias.
    """
    cripto = combo.get()
    if not cripto:
        messagebox.showwarning("Atenção", "Selecione uma criptomoeda.")
        return

    try:
        df = buscar_dados(cripto)
        plt.figure(figsize=(8, 4))
        plt.plot(df['date'], df['price'], marker='o', linestyle='-')
        plt.title(f"Preço de {cripto.capitalize()} (últimos 7 dias)")
        plt.xlabel("Data")
        plt.ylabel("Preço (USD)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar gráfico:\n{e}")

# 🖼️ Configuração da interface gráfica principal
janela = tk.Tk()
janela.title("Analisador de Criptomoedas")
janela.geometry("420x160")
janela.resizable(False, False)

# 🔠 Título e instrução
tk.Label(janela, text="Escolha uma criptomoeda:", font=("Arial", 12)).pack(pady=10)

# 🪙 Lista de criptomoedas disponíveis
criptomoedas = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Cardano": "cardano",
    "Solana": "solana",
    "Dogecoin": "dogecoin"
}

# 🔽 Combobox para seleção da criptomoeda
combo = ttk.Combobox(janela, values=list(criptomoedas.values()), state="readonly", width=30)
combo.pack(pady=5)

# 🔘 Botões de ação
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

btn_csv = tk.Button(
    frame_botoes,
    text="Gerar relatório CSV",
    command=gerar_csv,
    bg="green",
    fg="white",
    width=20
)
btn_csv.grid(row=0, column=0, padx=10)

btn_grafico = tk.Button(
    frame_botoes,
    text="Visualizar gráfico",
    command=visualizar_grafico,
    bg="blue",
    fg="white",
    width=20
)
btn_grafico.grid(row=0, column=1, padx=10)

# ▶️ Inicia o loop da interface
janela.mainloop()