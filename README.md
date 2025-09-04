# 💰 Analisador de Criptomoedas com Interface Gráfica

Este projeto foi desenvolvido com o objetivo de oferecer uma ferramenta simples, intuitiva e funcional para análise de preços de criptomoedas em tempo real. Utilizando **Python** e bibliotecas como **Tkinter**, **Pandas**, **Matplotlib** e a **API pública do CoinGecko**, o aplicativo permite ao usuário:

- Selecionar uma criptomoeda popular (Bitcoin, Ethereum, Cardano, Solana ou Dogecoin)
- Visualizar o gráfico de variação de preços dos últimos 7 dias
- Exportar os dados em formato `.csv` para uso externo ou arquivamento

---

## 🧠 Tecnologias e conceitos aplicados

- **Integração com API REST**: Consumo de dados em tempo real da CoinGecko  
- **Manipulação de dados com Pandas**: Conversão de timestamps, agrupamento por data e cálculo de médias  
- **Visualização com Matplotlib**: Geração de gráficos limpos e informativos  
- **Interface gráfica com Tkinter**: Criação de uma GUI amigável e responsiva  
- **Tratamento de exceções**: Garantia de robustez e feedback ao usuário em caso de erros  

---

## 📦 Como usar

1. Execute o script Python  
2. Escolha uma criptomoeda no menu suspenso  
3. Clique em **"Visualizar gráfico"** para ver a evolução dos preços  
4. Clique em **"Gerar relatório CSV"** para salvar os dados localmente  

---

## 📈 Exemplo de saída

**Relatório CSV com colunas:**

- `date`: Data da cotação  
- `price`: Preço médio diário em USD  

**Gráfico gerado:**

- Linha temporal com marcações diárias  
- Título dinâmico com o nome da criptomoeda  
- Eixos rotulados e grade para facilitar a leitura  

---

## 🚀 Lições aprendidas neste projeto

Este projeto foi criado como parte do meu portfólio para demonstrar habilidades em desenvolvimento Python voltado para aplicações práticas com dados financeiros. Ele combina consumo de APIs, análise de dados e design de interfaces — tudo em um único aplicativo funcional.

Se você gostou, sinta-se à vontade para **clonar, testar e contribuir!**
