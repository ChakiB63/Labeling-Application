import time
import streamlit as st # type: ignore
import numpy as np
from model.Phenomena import Phenomena
from model.Image import Image 
from model.Comparaison import Comparaison

@st.cache_data()
def generate_comparaison(layer, _user):
    return Comparaison(layer, _user)

def phenomena_infos(phenomena_presence, phenomena_nimg): # the second argument t encouter the exception of checkbox with the same key values
                if phenomena_presence=="Oui":
                    c1, c2, c3, c4, _ = st.columns(5)
                    with c1:
                        nw = st.checkbox("NO", key=phenomena_nimg+"_NO")
                    with c2:
                        ne = st.checkbox("NE", key=phenomena_nimg+"_NE")
                    with c3:
                        se = st.checkbox("SE", key=phenomena_nimg+"_SE")
                    with c4:
                        sw = st.checkbox("SO", key=phenomena_nimg+"_SO")
                    return [nw, ne,se,sw]
                else:
                    c1, c2, c3, c4, _ = st.columns(5)
                    with c1:
                        st.checkbox("NO", key=phenomena_nimg+"_NO",disabled=True)
                    with c2:
                        st.checkbox("NE", key=phenomena_nimg+"_NE",disabled=True)
                    with c3:
                        st.checkbox("SE", key=phenomena_nimg+"_SE",disabled=True)
                    with c4:
                        st.checkbox("SO", key=phenomena_nimg+"_SO",disabled=True)
                    return [False, False, False, False]


@st.cache_data()
def test_cache():
    print("cache")

user = "cb"
use = "bd"
# Define your Streamlit app layout
def main():
    
    st.set_page_config(layout="wide")

    st.session_state.user = user
    if st.button("test"):
        print(st.session_state.user)
        #test_cache
        

    #st.html('<h1>Application de comparaison des image satellitaires</h1>')
    st.header('Application pour l\'évaluation de similarité des images satellitaires', divider= 'rainbow')

    # st.toggle("Vue côte-à-côte"):

    
    # The selectbox to choose the layer of the images
    layers = np.array(['Airmass', 'Convection', 'Dust', 'NaturalEnhncd'])
    layer = st.selectbox('Veuillez sélectionner le spectre des images à comparer :', layers)
    layer = layer.lower()

    # Generating the pictures or a message informing that all the images were compared
    comparaison = generate_comparaison(layer, user) #pour avoir une cache
    if comparaison.get_fin_archive() : 
            st.warning("Toutes les images contenues dans l'archive pour ce spectre ont été comparés. Merci pour vos efforts.  \nPour plus d'informations, contacter votre assistant technique.")
            st.stop()

    # Displaying the pictures
    _,co1, co2 = st.columns([1,5,5],gap="medium")
    with co1:
        st.image(comparaison.get_img1(), caption=comparaison.get_dt1())
        image1 = Image(comparaison.get_dt1(), user)
        ex1 = image1.verify_existence(user)
        if ex1:
                st.info("Les informations sur cette images ont été saisies précédement.")
        else:
            phenomena_presence1  = st.radio("Présence des phénomènes dans l'image à gauche : ", ["Oui", "Non"],horizontal=True)
    with co2:
        st.image(comparaison.get_img2(), caption=comparaison.get_dt2())
        image2 = Image(comparaison.get_dt2(), user)
        ex2 = image2.verify_existence(user)
        if ex2:
            st.info("Les informations sur cette images ont été saisies précédement.")
        else:
            phenomena_presence2  = st.radio("Présence des phénomènes dans l'image à droite : ", ["Oui", "Non"],horizontal=True)

    # Displaying the table of the phenomenas infos
    co0, co1, co2 = st.columns([1,5,5])
    with co0:
        if not ex1 or not ex2:
            st.write("Convection :")
            st.write("Poussière :")
            st.write("Brouillard :")
            st.write("Feu forêt :")
            st.write("Goutte froide:")

    with co1:
        if not ex1 or not ex2:
            if not ex1:
                image1.set_phenomena_presence(phenomena_presence1=="Oui")

                convection_infos1 = phenomena_infos(phenomena_presence1,"convection1")
                convection_ph1 = Phenomena(True in convection_infos1,convection_infos1)
                image1.set_convection(convection_ph1)

                dust_infos1 = phenomena_infos(phenomena_presence1,"dust1")
                dust_ph1 = Phenomena(True in dust_infos1,dust_infos1)
                image1.set_dust(dust_ph1)

                fog_infos1 = phenomena_infos(phenomena_presence1, "fog1")
                fog_ph1 = Phenomena(True in fog_infos1,fog_infos1)
                image1.set_fog(fog_ph1)

                fire_forest_infos1 = phenomena_infos(phenomena_presence1, "fire_forest1")
                fire_forest_ph1 = Phenomena(True in fire_forest_infos1,fire_forest_infos1)
                image1.set_fire_forest(fire_forest_ph1)

                cold_drop_infos1 = phenomena_infos(phenomena_presence1, "cold_drop1")
                cold_drop_ph1 = Phenomena(True in cold_drop_infos1,cold_drop_infos1)
                image1.set_cold_drop(cold_drop_ph1)
            else:
                phenomena_infos("Non", "convection1")
                phenomena_infos("Non", "dust1")
                phenomena_infos("Non", "fog1")
                phenomena_infos("Non", "fire_forest1")
                phenomena_infos("Non", "cold_drop1")

    with co2:
        if not ex1 or not ex2:
            if not ex2:
                image2.set_phenomena_presence(phenomena_presence2=="Oui")

                convection_infos2 = phenomena_infos(phenomena_presence2,"convection2")
                convection_ph2 = Phenomena(True in convection_infos2,convection_infos2)
                image2.set_convection(convection_ph2)

                dust_infos2 = phenomena_infos(phenomena_presence2,"dust2")
                dust_ph2 = Phenomena(True in dust_infos2,dust_infos2)
                image2.set_dust(dust_ph2)

                fog_infos2 = phenomena_infos(phenomena_presence2, "fog2")
                fog_ph2 = Phenomena(True in fog_infos2,fog_infos2)
                image2.set_fog(fog_ph2)

                fire_forest_infos2 = phenomena_infos(phenomena_presence2, "fire_forest2")
                fire_forest_ph2 = Phenomena(True in fire_forest_infos2, fire_forest_infos2)
                image2.set_fire_forest(fire_forest_ph2)

                cold_drop_infos2 = phenomena_infos(phenomena_presence2, "cold_drop2")
                cold_drop_ph2 = Phenomena(True in cold_drop_infos2, cold_drop_infos2)
                image2.set_cold_drop(cold_drop_ph2)

            else:
                phenomena_infos("Non", "convection2")
                phenomena_infos("Non", "dust2")
                phenomena_infos("Non", "fog2")
                phenomena_infos("Non", "fire_forest2")
                phenomena_infos("Non", "cold_drop2")

    similarity_percentage = st.slider("Le pourcentage de similarité :", 0, 100)
    similarity_label = st.radio("Le degrès de similarité est : ", ["Très faible", "Faible", "Modérée", "Forte", "Très forte"], horizontal=True)
    
    comparaison.set_percentage(similarity_percentage)
    comparaison.set_label(similarity_label)
    

    if st.button("Enregistrer "):
        if not ex1:
            image1.add()
        if not ex2:
            image2.add()

        comparaison.add()

        st.success("Données enregistrées! Des images nouvelles seront affichées.")
        time.sleep(1.5)
        st.cache_data.clear()
        st.rerun()

# Run the app
if __name__ == "__main__":
    main()

