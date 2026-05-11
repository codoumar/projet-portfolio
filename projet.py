import streamlit as st
st.title("Codou Mar FAYE")

st.subheader("Ingénieur Agronome")
st.markdown("--------------------------------------------------------------------------")

st.subheader("Profil")
st.markdown("Ingénieur agronome passionnée par la production animale, avec des connaissances en élevage, alimentation et gestion des animaux. Motivée, rigoureuse et intéressée par le développement du secteur agricole.Je maîtrise les pratiques liées à la mise bas chez la brebis et je sais également cultiver différentes productions agricoles. J’ai déjà étudié certaines bactéries en microbiologie et j’ai également eu l’occasion d’observer et de préparer des échantillons de cellules animales et végétales à observer au microscope.")
st.markdown("--------------------------------------------------------------------------")
st.subheader("Parcours académique")
st.markdown("""
- **2024-2027**:Licence en Sciences et Techniques Agricoles Alimentaires et Nutritionnelles,université Amadou Mahtar Mbow,Diamniadio.
- **2023-2024**:Baccalauréat en Sciences expérimentales,Institution Saint Louis Marie Grignion,Malika.""")
st.markdown("--------------------------------------------------------------------------")

st.subheader("Compétences techniques")
st.markdown("""
- Création d’interfaces interactives avec Streamlit
- Analyse de données avec Python et Colab
- Suite bureautique
- Canva
- Techniques de culture agricole:tomates,arachides,oignons vert,gros thym...
- Notions en santé animale
- Manipulation d'équipements de laboratoire""")


st.markdown("--------------------------------------------------------------------------")

st.subheader("Expériences pratiques")
st.markdown("""
- **Mise bas chez la brebis** : assistance, observation et soins post-natals.  
- **Suivi du bétail** : alimentation, santé et prévention.""")
st.markdown("--------------------------------------------------------------------------")
st.subheader("Projets réalisés")
col1,col2=st.columns(2)
    
with col1:
    st.markdown("**Participation aux soins du bétail et assistance lors des mises bas. Cette expérience a renforcé mes compétences en élevage et mon intérêt pour la production animale.**")

with col2:
    st.image("agneau.jpg",width=150)
    
col3,col4=st.columns(2)

with col3:
    st.markdown("A la maison,je m’occupe des poules avec sérieux et passion, en veillant à leur alimentation, leur santé et leur bien-être.")
with col4:
    st.image("poules.jpg",width=150)
col5,col6=st.columns(2)
with col5:
    st.markdown(" J’ai déja eu à cultiver des tomates, incluant la plantation, le suivi et l’entretien des cultures. Cette expérience m’a permis de développer des compétences pratiques en agriculture et de renforcer mon intérêt pour les productions végétales et les sciences agricoles.")
with col6:
    st.image("culture de tomates.png",width=200)
col7,col8=st.columns(2)
with col7:
    st.markdown("J’ai planté et entretenu cette culture de menthe durant mes vacances par bouturage.Ce qui m’a permis de mettre en oeuvre mes compétences théoriques en production végétale.")
with col8:
    st.image("culture de menthe.jpeg",width=200)
        
with st.sidebar:
    st.image("portrait.jpeg",width=200)
    st.markdown("Email:codoumarfaye3105@gmail.com")
    st.markdown("Dakar,sénégal")
    st.markdown("-------------------------------")
    st.markdown("Veuillez me joindre par mail pour toute information supplémentaire.")
