# 📊 Financial Dashboard — Streamlit

Interactive web app built with **Python, Streamlit, Pandas, and Plotly** to explore a monthly
expense spreadsheet: filter the data, edit it in the browser, visualize trends, and export
the result back to Excel.

## Features

- **Data cleaning on load** — converts currency strings (e.g. `R$ 1.234,56`) into numeric values
- **Dynamic filters** — multiselect for text columns and range sliders for numeric columns
- **Editable table** — adjust values directly in the browser (`st.data_editor`)
- **Monthly trend chart** — line chart per expense, with months correctly ordered (Jan → Dec)
- **Custom charts** — choose X/Y columns and switch between bar, pie, and line charts
- **Excel export** — download the edited data as a new `.xlsx` file

## Tech stack

Python · Streamlit · Pandas · Plotly · OpenPyXL

## Getting started

```bash
git clone https://github.com/RafaelGambin/Planilha-Financeira---Streamlit.git
cd Planilha-Financeira---Streamlit

python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

pip install -r requirements.txt
streamlit run main.py
```

The app loads the sample file `test.xlsx`. To use your own data, keep the same structure:
an `DESPESA` (expense) column plus one column per month (`JANEIRO` … `DEZEMBRO`).

## Possible improvements

- File upload so users can analyze their own spreadsheets
- Unit tests for the data-cleaning step
- Deploy to Streamlit Community Cloud
