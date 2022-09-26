import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Portfolio", page_icon=":maple_leaf:", layout="wide")


# Use request for animation loading
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_4kx2q32n.json") #("https://assets7.lottiefiles.com/packages/lf20_xRmNN8.json")
img_profile_picture = Image.open("images/img_profile_picture.png")
img_computer_vision = Image.open("images/img_computer_vision.png")
img_deep_learning = Image.open("images/img_deep_learning.png")
img_data_visualization = Image.open("images/img_data_visualization.png")
img_data_science = Image.open("images/img_data_science.png")
img_embedded_system = Image.open("images/img_embedded_system.jpg")
img_work_tools = Image.open("images/img_work_tools.png")

# ---- HEADER SECTION ----
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_profile_picture, width=300)
    with text_column:
        st.subheader("Hi, I am Siddhey :wave:")
        st.title("A Data Scientist From Germany")
        st.write(
            "I provide data centric software solutions for intelligent systems involving sensor technology, "
            "image processing, machine learning, database management & embedded systems."
        )
        st.write("[LinkedIn Profile >](http://www.linkedin.com/in/siddhey-ratnaparkhi)")
        with open("files/Resume_Siddhey_Singular.pdf", "rb") as file:
            btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="files/Resume_Siddhey_Singular.pdf"
            )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.markdown('<div style="text-align: center; font-size: 250%;"><b>Intelligent Systems: A Portfolio</b></div>',
                unsafe_allow_html=True)
    _, center_column, right_column = st.columns(3)
    with right_column:
        st.write("##")
        st.subheader(
            """
            My portfolio consists of following topics:
            - Computer Vision
            - Deep Learning
            - Data Visualization
            - Data Science
            - Embedded System

            """
        )
    with center_column:
        st_lottie(lottie_coding, height=400, key="coding")

# ---- PROJECTS ----

# Project 1: Computer Vision
with st.container():
    st.write("---")
    st.markdown('<div style="text-align: center; font-size: 220%;"><b>My Projects</b></div>',
                unsafe_allow_html=True)
    st.write("##")
    st.markdown('<div style="text-align: center; font-size: 200%;"><b>Computer Vision</b></div>',
                unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.write(" ")
    with col_2:
        st.image(img_computer_vision)
    with col_3:
        st.write(" ")
    st.subheader("Generation of synthetic image dataset with OpenCV & SciPy at TRUMPF GmbH.")
    st.write("Task Details:")
    st.write(
        """
        Developed image generation pipeline to render synthetic images of 2D laser-cut sheet metal parts using
        OpenCV library. Implemented operations of object detection, image blur, scale, rotate, flip, crop,
        gaussian crop, brightness, warp, threshold, overlay, resize, reshape. This optimized the image rendering
        pipeline to produce large number of images to build image datasets for developing prediction &
        classification networks.
        """
    )
    st.markdown("[Watch Video...](https://youtu.be/7Tj-zJlwxus)")
    st.write("##")

# Project 2: Deep Learning
with st.container():
    st.write("##")
    st.markdown('<div style="text-align: center; font-size: 200%;"><b>Deep Learning</b></div>',
                unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.write(" ")
    with col_2:
        st.image(img_deep_learning)
    with col_3:
        st.write(" ")
    st.subheader("Implementation of deep neural networks using Tensorflow & Keras at TRUMPF GmbH.")
    st.write("Task Details:")
    st.write(
        """
        Image segmentation – As per the system requirement, I implemented semantic segmentation model using U-Net
        architecture (2D CNN) on synthetic images generated from image rendering pipeline. The model inference on
        test dataset of synthetic images was compared with test dataset of real annotated images which performed
        well with IoU score of c.a. 88 percent. This improved the sorting process of 2D laser-cut sheet metal parts.
         Google’s TensorFlow open-source AI was used as the framework along with Keras API. The pipeline was
         maintained using Git and Azure.
        """
    )
    st.write(
        """
        Image classification – The results of segmentation model were used to implement a binary image
        classification model using AlexNet architecture (2D CNN with dense connected layers). This task required to
        generate noisy label images to match the segmentation results. Conducted integration of the segmentation &
        classification models to perform final inference using real images acquired from several customers using
        industrial camera sensors, achieving 85% accuracy.
        """
    )
    st.markdown("[Visit Company...](https://www.trumpf.com/en_INT/)")
    st.write("##")

# Project 3: Data Visualization
with st.container():
    st.write("##")
    st.markdown('<div style="text-align: center; font-size: 200%;"><b>Data Visualization</b></div>',
                unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.write(" ")
    with col_2:
        st.image(img_data_visualization)
    with col_3:
        st.write(" ")
    st.subheader("Sensor data visualization & creation of Dashboard using R and SQL at TRUMPF GmbH.")
    st.write("Task Details:")
    st.write(
        """
        R Shiny dashboard – Developed real time dashboard using R Shiny to visualize & detect a falling 2D laser-cut
        sheet metal using light grid sensor data. Implemented client-server features to compare sensor data plots,
        calculate area of falling part, lasso select with user interactive features of Boolean Q&As, comment box.
        The developed dashboard was used as a data labelling tool to later develop a learning model.
        """
    )
    st.write(
        """
        Information retrieval – Established setup for connection to server data using ODBC driver to query light
        grid sensor data with R. Exercised relational database (RDBMS) using MySQL workbench to read & write data
        formats of .json, HEX, text, Boolean elements.
        """
    )
    st.markdown("[Watch Video...](https://youtu.be/rLqvj9Z3Zbc)")
    st.write("##")

# Project 4: Data Science
with st.container():
    st.write("##")
    st.markdown('<div style="text-align: center; font-size: 200%;"><b>Data Science</b></div>',
                unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.write(" ")
    with col_2:
        st.image(img_data_science)
    with col_3:
        st.write(" ")
    st.subheader("Implementation of ML classification models using scikit-learn on sensor data from LFL Bayern.")
    st.write("Task Details:")
    st.write(
        """
        The tasks is based on analysis of sensor data from cows, with sensors attached at different points of time
        when a cow leaves the herd. The original dataset is provided by the LFL Bayern (Bayerische Landesanstalt
        für Landwirtschaft). The dataset consists of sensor values collected from more than sixty cows from July
        2018 to January 2019 using a stomach sensor which measures the activity and stomach temperature every 10
        minutes and a collar sensor which collects the rumination data of cow for every 2 hours. The extent of
        difficulty in calving for cows is measured in levels numbered from 0 to 4. Level 0 being the least
        difficult calving and Level 4 is the most difficult calving. The mapping of extracted features and
        corresponding level of difficult calving would be used for training the classifier models.
        """
    )
    st.write(
        """
        Amongst different classifiers such as Logistic Regression, Support Vector Machine, Naive Bayes & Random
        Forest, Decision Tree precisely classifies all difficulty levels with high recall score as seen above.
        The visualization of trained decision tree classifier created using Scikit-learn library clearly depicts
        that Level 0 can be predicted if the rumination average is less than 41.48 and THI value is less than 71.04
        and also if the rumination average is greater than 44.77 and stomach activity is less than 12.85. Also,
        Level 2 can be predicted if rumination average is between 44.51 and 44.77 and rest of the cases are
        classified as Level 1.
        """
    )
    st.markdown("[Visit Company...](https://www.lfl.bayern.de/)")
    st.write("##")

# Project 5: Embedded System
with st.container():
    st.write("##")
    st.markdown('<div style="text-align: center; font-size: 200%;"><b>Embedded System</b></div>',
                unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.write(" ")
    with col_2:
        st.image(img_embedded_system)
    with col_3:
        st.write(" ")
    st.subheader("PCB design, development & programming of Gesture Controlled Robotic Vehicle using ATMEL "
                 "microcontroller (8, 16 & 32 bit).")
    st.write("Task Details:")
    st.write(
        """
        Design: The vehicle prototype consists of ATMEGA-8 IC along with Radio Frequency module (RF 433MHz RX)
        mounted on a chasis having 4 wheels. The PCB was implemented in-house using Eagle Design Software
        supported by AVR Studio and Embedded C.
        """
    )
    st.write(
        """
        Behaviour: The vehicle navigates wirelessly using hand gesture signals which are recorded by Accelerometer
        sensor and transmitted wirelessly over the radio frequency (RF 433MHz TX). An Encoder-Decoder pair IC
        avoids signal interference & noise.
        """
    )
    st.markdown("_Note: The above picture does not depict the actual hardware setup._")
    st.write("##")

# Skill-set
with st.container():
    st.write("---")
    first_column, second_column, third_column = st.columns(3)
    with first_column:
        st.subheader("Programming Skills")
        st.write(
            """
            - C, C++, Embedded C
            - Python
            - R
            - SQL, NoSQL
            - JavaScript
            """
        )
    with second_column:
        st.subheader("Data Science")
        st.write(
            """
            - Scikit-learn
            - NumPy
            - Pandas
            - Matplotlib
            - Plotly
            """
        )
    with third_column:
        st.subheader("Computer Vision")
        st.write(
            """
            - OpenCV
            - TensorFlow
            - Keras
            - PyTorch
            - SciPy
            """
        )

# Work Tools
with st.container():
    st.write("---")
    st.write("##")
    st.markdown('<div style="text-align: center; font-size: 220%;"><b>Work Tools</b></div>',
                unsafe_allow_html=True)
    first_column, second_column, third_column = st.columns(3)
    with first_column:
        st.write(" ")
    with second_column:
        st.image(img_work_tools)
    with third_column:
        st.write(" ")


# ----------------------------------------------------------------------------------------------------------------------
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! MENTION RELEVANT EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/siddhey1@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
