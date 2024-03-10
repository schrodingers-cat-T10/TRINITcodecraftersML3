from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
from utils import *
import numpy as np
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

tokenizer,model=load_tokenizer_and_model(
    tokenizer_path="models/tokenizer.pickle",
    model_path="models/caption_model.h5"
)




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app's domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.post("/upload/")
def upload_image(image: UploadFile = File(...)):
    img=image.read()
    img = Image.open(BytesIO(img))
    img=read_images_as_rgb(np.array(img)).reshape(1,224,224,3)
    img=vgg_predict_image(img)


    return predict_caption(model = model , image= img, tokenizer= tokenizer, max_length= 119)


