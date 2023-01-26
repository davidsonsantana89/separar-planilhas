import streamlit as st
import pandas as pd
import xlsxwriter
from io import BytesIO

st.title("WEB APP - ETE LUIZ ALVES LACERDA")
st.text('Este aplicativo reune as planilhas de componentes eletivos em planilhas por turma, em cada aba.\nEm fase de testes.')
st.markdown("---")
planilhas = st.file_uploader("Clique ou arraste suas planilhas aqui.", type='xlsx', accept_multiple_files=True)


lista_df = []
for planilha in planilhas:
    lista_df.append(pd.read_excel(planilha))

if lista_df is not None:
    df = pd.concat(lista_df).reset_index(drop=True)
    # st.dataframe(df)

output = BytesIO()

turmas = df['turma'].unique()

print(turmas)

lista_plan = []

for turma in turmas:
    lista_plan.append(df[df['turma'] == turma])

with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    for plan, i in zip(lista_plan, range(1,1+len(lista_plan))):
        plan.to_excel(writer, sheet_name=f'Planilha-{i}', index=False)
    writer.save()

st.download_button(
label="Baixe a planilha.",
data=output,
file_name="tumas_eletivas.xlsx",
mime="application/vnd.ms-excel")
