# 💰 Simulador de Investimentos & Juros Compostos

Aplicação Full-Stack para simulação financeira e projeção de Reserva de Emergência, utilizando dados reais do Banco Central do Brasil.

## 🚀 Funcionalidades

- **Cálculo de Juros Compostos:** Projeção matemática precisa mês a mês.
- **Conexão API BCB:** Busca automática da taxa Selic atualizada (Série 432).
- **Fallback de Segurança:** Sistema resiliente que funciona mesmo se o BCB estiver offline.
- **Interface Visual:** Dashboard interativo com gráficos de área (Matplotlib + Base64).
- **Relatório Executivo:** Geração automática de análise de viabilidade financeira.

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python 3.13, FastAPI, Uvicorn, Requests.
- **Front-end:** HTML5, CSS3 (Grid Layout, Variáveis), JavaScript (Fetch API).
- **Ciência de Dados:** Matplotlib, Pydantic.
- **Qualidade de Código:** Black Formatter, Flake8 (PEP 8 Compliant).

## 📦 Como Rodar

1. Clone o repositório.
2. Instale as dependências:
   ```bash

   pip install -r requirements.txt

   ---
## 📸 Screenshots

### Gráfico de Evolução
![Gráfico do Sistema](https://github.com/Well-ads/simulador-financeiro-py/blob/main/grafico.png?raw=true)

### Relatório Gerado
![Relatório Financeiro](relatorio.png)

