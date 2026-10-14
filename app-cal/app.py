import streamlit as st

st.set_page_config(page_title="Calculadora de Preco", layout="centered")

st.title("Calculadora de Preco de Venda")
st.write("Calcule o preco ideal de venda considerando custos, despesas e lucro desejado.")

custo = st.number_input("Custo do produto (R$):", min_value=0.0, value=100.0, step=10.0)
despesas = st.number_input("Porcentagem de despesas/impostos (%):", min_value=0.0, max_value=99.0, value=0.0, step=1.0)
lucro = st.number_input("Porcentagem de lucro desejada (%):", min_value=0.0, max_value=99.0, value=30.0, step=1.0)

if st.button("Calcular Preco de Venda", use_container_width=True):
    divisor = 1 - ((despesas + lucro) / 100)
    
    if divisor <= 0:
        st.error("Erro: A soma das despesas e do lucro e muito alta! O preco ficaria infinito ou negativo.")
    else:
        preco_venda = custo / divisor
        st.success(f"Voce deve vender por: R$ {preco_venda:.2f}")