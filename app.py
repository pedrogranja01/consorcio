import streamlit as st

st.title("Calculadora Simples")

num1 = st.number_input("Digite o primeiro número:", value=0.0)
num2 = st.number_input("Digite o segundo número:", value=0.0)
operacao = st.selectbox("Escolha a operação:", ["Soma", "Subtração", "Multiplicação", "Divisão"])

if st.button("Calcular"):
    if operacao == "Soma":
        resultado = num1 + num2
    elif operacao == "Subtração":
        resultado = num1 - num2
    elif operacao == "Multiplicação":
        resultado = num1 * num2
    elif operacao == "Divisão":
        if num2 == 0:
            resultado = "Erro: divisão por zero!"
        else:
            resultado = num1 / num2

    st.success(f"Resultado: {resultado}")