import random
import streamlit as st
    
def jogo_sorteio():
    st.title("Jogo de Adivinhação")
    st.write("Tente adivinhar o número entre 1 e 15. Você tem 3 chances!")

    if "numero_sorteado" not in st.session_state:
        st.session_state.numero_sorteado = random.randint(1, 15)
        st.session_state.tentativas_restantes = 3
        st.session_state.resultado = ""

    if st.session_state.tentativas_restantes > 0:
        palpite = st.number_input("Digite seu palpite:", min_value=1, max_value=15, step=1)

        if st.button("Enviar Palpite"):
            if palpite == st.session_state.numero_sorteado:
                st.session_state.resultado = "Parabéns! Você acertou o número!"
                st.session_state.tentativas_restantes = 0
            elif palpite > st.session_state.numero_sorteado:
                st.session_state.tentativas_restantes -= 1
                st.session_state.resultado = f"Seu palpite foi maior que o número sorteado. Tentativas restantes: {st.session_state.tentativas_restantes}"
            else:
                st.session_state.tentativas_restantes -= 1
                st.session_state.resultado = f"Seu palpite foi menor que o número sorteado. Tentativas restantes: {st.session_state.tentativas_restantes}"

    else:
        st.session_state.resultado = f"Que pena! O número sorteado era {st.session_state.numero_sorteado}."

    st.write(st.session_state.resultado)

    if st.session_state.tentativas_restantes == 0:
        if st.button("Jogar Novamente"):
            st.session_state.numero_sorteado = random.randint(1, 15)
            st.session_state.tentativas_restantes = 3
            st.session_state.resultado = ""

if __name__ == "__main__":
    jogo_sorteio()