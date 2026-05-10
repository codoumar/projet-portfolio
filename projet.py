import streamlit as st
st.title("Codou Mar FAYE")

st.subheader("Ingénieur Agronome")
st.markdown("--------------------------------------------------------------------------")

st.subheader("Profil")
st.markdown("Je maîtrise les pratiques liées à la mise bas chez la brebis et je sais également cultiver différentes productions agricoles. J’ai déjà étudié certaines bactéries en microbiologie et j’ai eu l’occasion d’observer des cellules animales en biologie animale.")
st.markdown("--------------------------------------------------------------------------")
st.subheader("Parcours académique")
st.markdown("* 2026-2027:Licence en Sciences et Techniques Agricoles Alimentaires et Nutritionnelles,université Amadou Mahtar Mbow,Diamniadio")
st.markdown("* 2023-2024:Baccalauréat en Sciences expérimentales,Institution Saint Louis Marie Grignion,Malika")
st.markdown("--------------------------------------------------------------------------")
st.subheader("Compétences professionelles")
st.markdown("* Suite bureautique")
st.markdown("* Canva")
st.markdown("* Technique de culture agricole:tomates,arachides,oignons vert,gros thym...")
st.markdown("* Notions en santé animale")
st.markdown("* Gestion de l'alimentation animale")
st.markdown("* Hygiène d'élevage")
st.markdown("* Soins du bétail")
st.markdown("--------------------------------------------------------------------------")
st.subheader("Projets réalisés")
col1,col2=st.columns(2)
    
with col1:
    st.markdown("Participation aux soins du bétail et assistance lors des mises bas. Cette expérience a renforcé mes compétences en élevage et mon intérêt pour la production animale..")

with col2:
    st.image("agneau.jpg",width=150)
    
col3,col4=st.columns(2)

with col3:
    st.markdown("Je m’occupe des poules avec sérieux et passion, en veillant à leur alimentation, leur santé et leur bien-être.")
with col4:
    st.image("poules.jpg",width=150)
col5,col6=st.columns(2)
with col5:
    st.markdown(" J’ai déjà pratiqué la culture de tomates, en assurant leur plantation, leur suivi et leur entretien. Cette expérience m’a permis de développer des compétences pratiques en agriculture, notamment dans la gestion de la croissance, l’arrosage et la récolte, renforçant ainsi mon intérêt pour les productions végétales et les sciences agricoles")
with col6:
    st.image("culture de tomates.png",width=150)
col7,col8=st.columns(2)
with col7:
    st.markdown("J’ai déjà cultivé de la menthe en prenant en charge sa plantation, son entretien et sa récolte. Cette pratique m’a permis d’acquérir un savoir-faire concret dans la gestion des plantes aromatiques, notamment en matière d’arrosage, de suivi de la croissance et de qualité de production.")
with col8:
    st.image("culture de menthe.jpeg",width=150)
        
with st.sidebar:
    st.image("portrait.jpeg",width=200)
    st.markdown(" Mail:codoumarfaye3105@gmail.com")
    st.markdown("Dakar,sénégal")
    st.markdown("-------------------------------")
    st.markdown("Veuillez me joindre par mail pour toute information supplémentaire.")
