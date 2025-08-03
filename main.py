import streamlit as st
import pandas as pd
import io
import plotly.express as px

@st.cache_data
def carregar_dados():
    df = pd.read_excel(
        r"C:\Users\rafae\PycharmProjects\planilha_streamlit\test.xlsx",
        engine='openpyxl'
    )
    df.columns = df.columns.str.strip()

    for col in df.columns:
        if col != "DESPESA":
            df[col] = pd.to_numeric(
                df[col].astype(str)
                .str.replace("R\$", "", regex=True)
                .str.replace(",", ".")
                .str.strip(),
                errors='coerce'
            )

    return df

df = carregar_dados()

st.title("📊 Planilha Financeira - Controle de custos")

st.sidebar.header("🔍 Filtros")
df_filtrado = df.copy()

for coluna in df.columns:
    try:
        if df[coluna].dtype == "object":
            opcoes = st.sidebar.multiselect(
                f"Filtrar {coluna}", df[coluna].unique(), default=df[coluna].unique()
            )
            df_filtrado = df_filtrado[df_filtrado[coluna].isin(opcoes)]
        elif pd.api.types.is_numeric_dtype(df[coluna]):
            if df[coluna].dropna():
                continue
            min_val, max_val = float(df[coluna].min()), float(df[coluna].max())
            slider = st.sidebar.slider(f"Filtrar {coluna}", min_val, max_val, (min_val, max_val))
            df_filtrado = df_filtrado[(df_filtrado[coluna] >= slider[0]) & (df_filtrado[coluna] <= slider[1])]
    except Exception as e:
        st.warning(f"Erro ao filtrar a coluna '{coluna}': {e}")

st.subheader("📋 Dados Editáveis")
edited_df = st.data_editor(df_filtrado.reset_index(drop=True), use_container_width=True)


colunas_validas = [col for col in df.columns if col not in ["TOTAL"]]
colunas_numericas = edited_df[colunas_validas].select_dtypes(include="number").columns.tolist()
colunas_categoricas = edited_df[colunas_validas].select_dtypes(include="object").columns.tolist()

df_melted = pd.melt(
    edited_df,
    id_vars=["DESPESA"],
    var_name="MÊS",
    value_name="VALOR"
)

df_melted = df_melted.dropna(subset=["VALOR"])

ordem_meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
               "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
df_melted["MÊS"] = pd.Categorical(df_melted["MÊS"], categories=ordem_meses, ordered=True)
df_melted = df_melted.sort_values("MÊS")

st.subheader("📈 Gráfico por Mês")
despesa_selecionada = st.selectbox("Selecione a Despesa", df_melted["DESPESA"].unique())
df_despesa = df_melted[df_melted["DESPESA"] == despesa_selecionada]

fig = px.line(df_despesa, x="MÊS", y="VALOR", title=f"Evolução de '{despesa_selecionada}' ao longo dos meses")
st.plotly_chart(fig, use_container_width=True)

if colunas_categoricas and colunas_numericas:
    col1, col2 = st.columns(2)
    with col1:
        coluna_x = st.selectbox("Eixo X", options=colunas_categoricas, index=0)
    with col2:
        coluna_y = st.selectbox("Eixo Y", options=colunas_numericas, index=0)

    tipo_grafico = st.radio("Tipo de Gráfico", ["Barras", "Pizza", "Linhas"])

    try:
        if tipo_grafico == "Barras":
            fig = px.bar(edited_df, x=coluna_x, y=coluna_y)
        elif tipo_grafico == "Pizza":
            fig = px.pie(edited_df, names=coluna_x, values=coluna_y)
        elif tipo_grafico == "Linhas":
            fig = px.line(edited_df, x=coluna_x, y=coluna_y)

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao gerar gráfico: {e}")
else:
    st.info("⚠️ Não há colunas numéricas e categóricas suficientes para gerar gráfico.")

st.subheader("⬇️ Baixar Dados Editados")
buffer = io.BytesIO()
edited_df.to_excel(buffer, index=False)
st.download_button(
    "📥 Baixar Excel",
    data=buffer.getvalue(),
    file_name="planilha_editada.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
