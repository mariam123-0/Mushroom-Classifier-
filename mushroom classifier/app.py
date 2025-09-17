import streamlit as st
st.set_page_config(page_title="Dark Purple Theme", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #1a001a;
        color: #ffffff;}
    .stApp {
        background-color: #1a001a;}
    </style>
    """,unsafe_allow_html=True)
st.title("🍄 Mushroom Classifier")
st.write("Select Features:")
import streamlit as st


with st.form(key="mushroom_form"):
    st.subheader("Cap Features")
    cap_shape = st.selectbox("Cap Shape", ["bell", "conical", "convex", "flat", "knobbed", "sunken"])
    cap_surface = st.selectbox("Cap Surface", ["fibrous", "grooves", "scaly", "smooth"])
    cap_color = st.selectbox("Cap Color", ["brown","buff","cinnamon","gray","green","pink","purple","red","white","yellow"])

    st.subheader("Bruises & Odor")
    bruises = st.selectbox("Bruises", ["bruises","no"])
    odor = st.selectbox("Odor", ["almond","anise","creosote","fishy","foul","musty","none","pungent","spicy"])

    st.subheader("Gills")
    gill_attachment = st.selectbox("Gill Attachment", ["attached","descending","free","notched"])
    gill_spacing = st.selectbox("Gill Spacing", ["close","crowded","distant"])
    gill_size = st.selectbox("Gill Size", ["broad","narrow"])
    gill_color = st.selectbox("Gill Color", ["black","brown","buff","chocolate","gray","green","orange","pink","purple","red","white","yellow"])

    st.subheader("Stalk")
    stalk_shape = st.selectbox("Stalk Shape", ["enlarging","tapering"])
    stalk_root = st.selectbox("Stalk Root", ["bulbous","club","cup","equal","rhizomorphs","rooted","missing"])
    stalk_surface_above_ring = st.selectbox("Stalk Surface Above Ring", ["fibrous","scaly","silky","smooth"])
    stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", ["fibrous","scaly","silky","smooth=s"])
    stalk_color_above_ring = st.selectbox("Stalk Color Above Ring", ["brown","buff","cinnamon","gray","orange","pink","red","white","yellow"])
    stalk_color_below_ring = st.selectbox("Stalk Color Below Ring", ["brown","buff","cinnamon","gray","orange","pink","red","white","yellow"])

    st.subheader("Veil")
    veil_type = st.selectbox("Veil Type", ["partial","universal"])
    veil_color = st.selectbox("Veil Color", ["brown","orange","white","yellow"])

    st.subheader("Ring")
    ring_number = st.selectbox("Ring Number", ["none","one","two"])
    ring_type = st.selectbox("Ring Type", ["cobwebby","evanescent","flaring","large","none","pendant","sheathing","zone"])

    st.subheader("Other Features")
    spore_print_color = st.selectbox("Spore Print Color", ["black","brown","buff","chocolate","green","orange","purple","white","yellow"])
    population = st.selectbox("Population", ["abundant","clustered","numerous","scattered","several","solitary"])
    habitat = st.selectbox("Habitat", ["grasses","leaves","meadows","paths","urban","waste","woods"])
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        features = {
            "cap-shape": cap_shape,
            "cap-surface": cap_surface,
            "cap-color": cap_color,
            "bruises": bruises,
            "odor": odor,
            "gill-attachment": gill_attachment,
            "gill-spacing": gill_spacing,
            "gill-size": gill_size,
            "gill-color": gill_color,
            "stalk-shape": stalk_shape,
            "stalk-root": stalk_root,
            "stalk-surface-above-ring": stalk_surface_above_ring,
            "stalk-surface-below-ring": stalk_surface_below_ring,
            "stalk-color-above-ring": stalk_color_above_ring,
            "stalk-color-below-ring": stalk_color_below_ring,
            "veil-type": veil_type,
            "veil-color": veil_color,
            "ring-number": ring_number,
            "ring-type": ring_type,
            "spore-print-color": spore_print_color,
            "population": population,
            "habitat": habitat}
        def predict_mushroom(feats: dict) -> str:
            if feats["odor"] in ["foul=f","fishy=y","pungent=p"]:
                return "Poisonous"
            else:
                return "Edible"
        prediction = predict_mushroom(features)
        st.subheader("Result:")
        st.write(prediction)