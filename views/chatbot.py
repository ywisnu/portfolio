import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hai, jika butuh bantuan jangan lupa kontak saya di linkedin channel https://www.linkedin.com/in/yohanes-wisnu-krisnantio-723b2646",
            "Tahukah kamu bahwa OTDR digunakan untuk mengevaluasi serat optik dalam domain waktu"
            "OTDR mengirimkan pulsa pendek berupa cahaya (antara 5 ns s/d 20 µs)",
            "Dynamic range merupakan ukuran dari range maksimum suatu pengukuran power level yang bisa diukur oleh OTDR",
            "Tahukah kamu panjang patchcord yang direkomendasikan adalah 2x panjang ",
            "LACP adalah protocol link aggregation yang bersifat open source dan dikembangkan oleh IEEE.",
            "Bridging loop akan terjadi ketika salah satu switch tidak mendisable link secara logical",
            "Konfigurasi VLAN bermanfaat untuk mengontrol size broadcast domain dan menjaga trafik local",
            "InterVLAN membutuhkan interface fisik router atau sub-interface router sebagai gateway masing-masing VLAN dan L3 switch",
            "VLAN ID digunakan oleh switch untuk mengetahui semua frame melalui trunk link",
            "VLAN Membagi single broadcast domain menjadi beberapa broadcast domain",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Robot Ngobrol")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
