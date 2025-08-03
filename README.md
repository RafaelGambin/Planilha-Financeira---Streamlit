# 📊 Dashboard Interativo com Streamlit

Este projeto é uma aplicação web desenvolvida com [Streamlit](https://streamlit.io/) para leitura de planilhas Excel, onde é possível **filtrar dados dinamicamente** e visualizar gráficos interativos baseados nos valores mensais de despesas ou outras métricas.

---

## 🚀 Funcionalidades

- 📂 Carregamento de arquivos `.xlsx`
- 🔎 Filtros dinâmicos para colunas de texto e números
- 📉 Geração automática de gráficos interativos com Plotly
- 📊 Eixo X representando os meses do ano e Y os valores (ex: despesas)
- ❌ Tratamento de valores nulos (ignora para gerar gráficos)
- 📌 Ordenação correta dos meses (Janeiro a Dezembro)

---

## 🛠️ Pré-requisitos

Certifique-se de ter o Python instalado e crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate     # Windows
```

---

## Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## Executar o programa
```bash
streamlit run main.py
```