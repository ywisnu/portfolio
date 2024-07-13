import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Yohanes Wisnu", anchor=False)
    st.write(
        "Senior Engineer, Project Management & Telecomunication Proffesionals."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 12 Years experience of Telecomunication Engineering
    - Strong hands-on experience and knowledge in Program & Project Management
    - Good understanding of IT Networking, Network Planning & Design
    - Strong experience of BTS & IBC Multi Network Operator Fiberize Project
    - OSP & ISP Design, Implementation & Maintenance 
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - IT Network, Routing & Switching (Cisco)
    - Data Visualization: MS Excel 
    - Logistic optimization
    - FTTH & OLT Command Line, Provisioning & Troubleshooting
    - Fiber Optic Design & Tools (Google Earth, QGIS & Python)
    """
)
