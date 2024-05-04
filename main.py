# Programaçao crud
from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
#import controllers.ac as ac
#import models.AberturadeContas as AberturadeContas

st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox(label='Selecione a página', options=['Abertura de contas', 'Resumo Flog(Em breve)', 'Resumo Funcionário (Em breve)', 'POBJ Produção (Em breve)'])

if paginaSelecionada == 'Abertura de contas':
    st.title("Abertura de Contas")
    with st.form(key="include_base"):
        input_name = st.selectbox(label="Selecione o seu nome", options=["","Daniel Banja","Gabriella Oliveira","Diego Farinha","Bradesco Expresso(MedicFarm)"])
        input_conta = st.number_input(label="Insira o número da Conta (Sem dígito)", format='%d', step=1)
        input_produto = st.selectbox(label="Selecione o produto", options=["","Invest", "Cheque Especial", "Lime", "Cartão de Crédito"])
        input_qtde = st.number_input(label="Insira a quantidade", format='%d', step=1)
        input_valor = st.number_input(label="Insira o Valor", step=100, )    
        input_button_submit = st.form_submit_button(label="Enviar")
    
    if input_button_submit:
        AberturadeContas.name = input_name
        AberturadeContas.conta = input_conta
        AberturadeContas.produto = input_produto
        AberturadeContas.qtde = input_qtde
        AberturadeContas.valor = input_valor
        st.success("Salvo com Sucesso!")


