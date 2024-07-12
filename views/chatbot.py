import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hai, jika butuh bantuan jangan lupa kontak saya di linkedin channel https://www.linkedin.com/in/yohanes-wisnu-krisnantio-723b2646",
            "Tahukah kamu bahwa OTDR digunakan untuk mengevaluasi serat optik dalam domain waktu",
            "OTDR mengirimkan pulsa pendek berupa cahaya (antara 5 ns s/d 20 µs)",
            "Dynamic range merupakan ukuran dari range maksimum suatu pengukuran power level yang bisa diukur oleh OTDR",
            "ACL Menentukan tipe traffic yang akan di control",
            "Salah Satu Kerugian OSPF Mengkonsumsi lebih banyak resource CPU",
            "LACP adalah protocol link aggregation yang bersifat open source dan dikembangkan oleh IEEE.",
            "Bridging loop akan terjadi ketika salah satu switch tidak mendisable link secara logical",
            "Konfigurasi VLAN bermanfaat untuk mengontrol size broadcast domain dan menjaga trafik local",
            "Hai, jika butuh bantuan jangan lupa kontak saya di linkedin channel https://www.linkedin.com/in/yohanes-wisnu-krisnantio-723b2646",
            "InterVLAN membutuhkan interface fisik router atau sub-interface router sebagai gateway masing-masing VLAN dan L3 switch",
            "VLAN ID digunakan oleh switch untuk mengetahui semua frame melalui trunk link",
            "VLAN Membagi single broadcast domain menjadi beberapa broadcast domain",
            "VLAN 1 dikenal juga sebagai Administrative VLAN atau Management VLAN",
            "Static VLAN Disebut juga sebagai Port-Based VLAN",
            "Hai, jika butuh bantuan jangan lupa kontak saya di linkedin channel https://www.linkedin.com/in/yohanes-wisnu-krisnantio-723b2646",
            "NAT adalah metode translasi IP private menjadi IP public",
            "Hai, jika butuh bantuan jangan lupa kontak saya di linkedin channel https://www.linkedin.com/in/yohanes-wisnu-krisnantio-723b2646",
            "Proses wr mem penting untuk dilakukan agar saat switch reboot atau shutdown file konfigurasi switch masih tetap disimpan di startupconfiguration (NVRAM)",
            "Koneksi switch menggunakan console, membutuhkan kabel console dan converter DB-9 to USB",
            "Hai, jika butuh bantuan jangan lupa kontak saya di linkedin channel https://www.linkedin.com/in/yohanes-wisnu-krisnantio-723b2646",
            "PAT Disebut juga sebagai NAT Dynamic Overload, Port Address Translation (PAT), atau NAT Overload",
            "NAT Dynamic Termasuk tipe many-to-many NAT, IP private dalam jumlah banyak kemudian ditranslate menjadi IP public yang banyak juga dengan menyediakan sebuah pool IP public",
            "Salah Satu Keuntungan NAT Yaitu Menghemat alamat IP secara legal",
            

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
    
