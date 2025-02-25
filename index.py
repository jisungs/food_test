from flask import Flask, render_template,request, jsonify, redirect, url_for
import pickle


def get_recommendations(title):
    idx = stores[stores['MAIN_TITLE'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[2:10]
    store_indices = [i[0] for i in sim_scores]

    images = []
    titles = []
    for i in store_indices:
        image_path = stores['MAIN_IMG_NORMAL'][i]
        if isinstance(image_path, str) and image_path:
            images.append(image_path)
        else:
            image_path = 'static/images/no_image.jpg'
            images.append(image_path) # Default image path

        titles.append(stores['MAIN_TITLE'][i])

    return images, titles


stores = pickle.load(open('stores.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

DEFAULT_IMAGE_PATH =  "/static/images/no_image.jpg"
stores['MAIN_IMG_NORMAL'] = stores['MAIN_IMG_NORMAL'].fillna(DEFAULT_IMAGE_PATH)
stores['MAIN_IMG_NORMAL'] = stores['MAIN_IMG_NORMAL'].apply(lambda x: x if x.strip() else DEFAULT_IMAGE_PATH)

app = Flask(__name__)

selected_region_text =''
selected_stores = stores[stores['GUGUN_NM']== '해운대구'].sample(n=8)

@app.route("/")
def index():
    global selected_region_text
    global selected_stores 

    context = {
        'store_list': selected_stores.to_dict(orient='records'),
        'selected_region': selected_region_text
    }
    return render_template('index.html', context=context)


@app.route("/selected_region", methods=["POST", "GET"])
def selected_region():
    global selected_stores
    global selected_region_text
    data = request.get_json()
    recived_region = data.get("text", "")
    selected_region_text = recived_region

    selected_stores = stores[stores['GUGUN_NM']== f'{selected_region_text}'].sample(n=8)
    
    return redirect(url_for('index'))


@app.route("/store_detail/<store_name>" , methods=["POST", "GET"])
def store_detail(store_name):
    store_info = stores[stores['MAIN_TITLE']== f'{store_name}']
    images, titles = get_recommendations(store_name)
    
    context = {
        'store_info' : store_info.to_dict(orient='records')[0],
        'images' : images,
        'titles' : titles,
    }
    return render_template('store_detail.html', store_name = store_name, context=context, zip=zip)

if __name__=='__main__':
    app.run(debug=True, port=8000)