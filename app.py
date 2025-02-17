import pickle
import streamlit as st

def get_recommendations(title):
    idx = stores[stores['MAIN_TITLE'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    store_indices = [i[0] for i in sim_scores]

    images = []
    titles = []
    for i in store_indices:
        image_path = stores['MAIN_IMG_NORMAL'][i]
        if isinstance(image_path, str) and image_path:
            images.append(image_path)
        else:
            image_path = 'no_image.jpg'
            images.append(image_path) # Default image path

        titles.append(stores['MAIN_TITLE'][i])

    return images, titles

stores = pickle.load(open('stores.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout="wide")
st.header('Busan Food Recommendation System')

store_list = stores['MAIN_TITLE'].values
title = st.selectbox('Select a store', store_list)

if st.button('Recommend'):
    images, titles = get_recommendations(title)

    idx = 0 
    for i in range(0,2):
        cols = st.columns(5)
        for col in cols:
            col.image(images[idx], use_container_width=True)
            col.write(titles[idx])
            idx += 1