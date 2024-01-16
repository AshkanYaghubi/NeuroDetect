from pathlib import Path
#import pickle
from cv2 import imread, resize
from numpy import reshape
from PIL import Image, ImageTk
import os
from tkinter import filedialog, Tk, Canvas, Entry, Text, Button, PhotoImage
#import gzip
import tf.keras.models.load_model

current_dir = os.path.dirname(__file__)
assets_path = os.path.join('assets', 'frame')


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(assets_path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#global svm_model

'''
compressed_model_path = os.path.join(current_dir, 'Models', 'compressed_model.pkl.gz')
decompressed_model_path = os.path.join(current_dir, 'Models', 'NeuroDetector_SVM.pkl')

if Path(decompressed_model_path).is_file():
    with open(decompressed_model_path, 'rb') as f:
        svm_model = pickle.load(f)
else:
    with gzip.open(compressed_model_path, 'rb') as f:
        svm_model = pickle.load(f)

#model_path = os.path.join(current_dir, "Models", "NeuroDetector_SVM.sav")
#svm_model = pickle.load(open(model_path, 'rb'))
'''
global model, binary_model

model_path = os.path.join(current_dir, 'Models', 'model.h5')
binary_model_path = os.path.join(current_dir, 'Models', 'model_binary.h5')

model = load_model(model_path)
binary_model = load_model(binary_model_path)

window = Tk()
window.title("NeuroDetect")
window.attributes("-alpha", 0.95)
window.bind("<Escape>", window.quit())
window.iconbitmap("assets\ico.ico")

window.geometry("850x550")
window.configure(bg = "#FFFFFF")

def open_dialog():
    global path
    path = filedialog.askopenfile().name
    image = Image.open(path).resize((258,198))
    image = ImageTk.PhotoImage(image)
    button_1.configure(image = image)
    button_1.image = image



def predict():
    img1 = imread(path,0)
    img = resize(img1, (200,200))
    img = reshape(img, (1,-1))
    img = img/255
    pred = model.predict(img)
    dec = {0 : "No_Tumor", 1 : "Glioma_Tumor", 2 : "Meningioma_Tumor", 3 : "Pituitary_Tumor", 4 : "Potential_Tumor"}
    if pred[0] == 0:
        pred_binary = binary_model.predict(img)
        if pred_binary[0] != 0:
            pred[0] = 4
    image_6_path = 'image_6_' + str(dec[pred[0]]) + '.png'
    image_6_photo = PhotoImage(file=relative_to_assets(image_6_path))
    button_4.configure(image = image_6_photo)
    button_4.image = image_6_photo




canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=491.0,
    y=61.0,
    width=258.0,
    height=198.0
)

canvas.create_text(
    491.0,
    294.0,
    anchor="nw",
    text="Import patient scan",
    fill="#151E3D",
    font=("Habibi Regular", 12 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    168.0,
    275.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_dialog,
    relief="flat"
)
button_2.place(
    x=613.0,
    y=289.0,
    width=125.0,
    height=33.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=predict,
    relief="flat"
)
button_3.place(
    x=557.0,
    y=341.0,
    width=117.15447998046875,
    height=30.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    800.0,
    536.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    746.0,
    538.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    169.0,
    111.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    615.0,
    222.0,
    image=image_image_5
)

canvas.create_text(
    25.0,
    197.0,
    anchor="nw",
    text="Introducing \"NeuruDetect\": Your Advanced",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    217.0,
    anchor="nw",
    text="Brain Tumor Detection Desktop App",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    246.0,
    anchor="nw",
    text="NeuruDetect is an innovative desktop",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    266.0,
    anchor="nw",
    text="application designed to aid in the early detection",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    286.0,
    anchor="nw",
    text="of brain tumors through the analysis of CT",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    306.0,
    anchor="nw",
    text="Scan or MRI images.",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    330.0,
    anchor="nw",
    text="With just one simple step, users can upload their",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    350.0,
    anchor="nw",
    text="CT Scan or MRI images directly into NeuruDetect.",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    377.0,
    anchor="nw",
    text="Note: TumorDetect is designed to assist medical",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    397.0,
    anchor="nw",
    text="professionals and individuals in the initial",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    417.0,
    anchor="nw",
    text="assessment of brain tumor presence based on",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    437.0,
    anchor="nw",
    text="imaging data. It is not intended to replace a",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    457.0,
    anchor="nw",
    text="comprehensive medical evaluation by qualified",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    477.0,
    anchor="nw",
    text="healthcare professionals. Always consult a medical",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    497.0,
    anchor="nw",
    text="expert for accurate diagnosis",
    fill="#000000",
    font=("Habibi", 13 * -1)
)

canvas.create_text(
    25.0,
    517.0,
    anchor="nw",
    text="and treatment recommendations.",
    fill="#000000",
    font=("Habibi", 13 * -1)
)
button_image_4 = PhotoImage(
    file=relative_to_assets("image_6.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_4.place(
    x=482.0,
    y=445.0,
    width=266.0,
    height=49.0
)
window.resizable(False, False)
window.mainloop()
