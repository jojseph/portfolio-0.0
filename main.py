import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

st.title("Hi, I'm Joseph")
st.markdown("CS Student / Software Developer")
st.caption("Also known as Joseph Victor Novabos")

ui.badges(
    badge_list=[
        ("C", "default"),
        ("C++", "default"),
        ("C#", "default"),
        ("Python", "default"),
        ("Java", "default"),
        ("PHP", "outline"),
        ("HTML", "outline"),
        ("CSS", "outline"),
        ("JavaScript", "outline"),
        ("React", "outline"),
        ("MySQL", "outline"),
        ("Kotlin", "secondary"),
    ],
    class_name="flex flex-wrap gap-2",
    key="badges_techstack"
)

st.subheader("About Me")
st.write("""
    Computer Science student focused on building practical skills through real-world projects. 
    Currently improving through self-driven learning and collaboration, 
    with an interest in software development and problem-solving.
""")

ui.link_button(text="Github", url="https://github.com/jojseph", key="link_btn")

tab = ui.tabs(
    options=["Projects", "Contact", "Demo"],
    default="Projects",
    key="tabs",
)

if tab == "Projects":
    st.subheader("My Projects")

    with ui.card(key="card1"):
        ui.element("p", children=["Bijou Battle"], className="text-black-900 text-lg font-semibold mb-1", key="title1")
        ui.element("p", children=["Java / Swing"], className="text-gray-600 text-sm mb-2", key="tech1")
        ui.element(
            "p",
            children=[
                "A fast-paced 2D local multiplayer platformer engineered using Java and a modular ECS architecture. "
                "Features responsive input handling, basic physics, and real-time combat mechanics — built from scratch "
                "without a game engine, showcasing strong architectural thinking and game loop design."
            ],
            className="text-gray-800 text-sm",
            key="desc1"
        )

    with ui.card(key="card2"):
        ui.element("p", children=["Wodify"], className="text-black-900 text-lg font-semibold mb-1", key="title2")
        ui.element("p", children=["Kotlin"], className="text-gray-600 text-sm mb-2", key="tech2")
        ui.element(
            "p",
            children=[
                "A minimalist mobile word puzzle game inspired by Wordle, built using native Android development in Kotlin. "
                "Players guess a hidden word within limited attempts, receiving color-coded feedback to guide logical deduction. "
                "Built to sharpen UI/UX design, game logic, and state management skills."
            ],
            className="text-gray-800 text-sm",
            key="desc2"
        )

    with ui.card(key="card3"):
        ui.element("p", children=["PPPoE Management System"], className="text-black-900 text-lg font-semibold mb-1", key="title3")
        ui.element("p", children=["Java / JavaFX"], className="text-gray-600 text-sm mb-2", key="tech3")
        ui.element(
            "p",
            children=[
                "A desktop application to manage PPPoE internet access with an intuitive JavaFX GUI. "
                "Enables administrators to monitor sessions, enable/disable access, and view real-time status "
                "in a lightweight, responsive environment."
            ],
            className="text-gray-800 text-sm",
            key="desc3"
        )

elif tab == "Contact":
    st.subheader("Contact Me")
    name = ui.input("name", "Your Name")
    email = ui.input("email", "Your Email")
    message = ui.textarea("message", "Your Message")
    if ui.button("Send Message", key="send"):
        if name and email and message:
            st.success(f"✅ Thanks {name}, your message has been sent!")
        else:
            st.error("Please fill out all fields before sending.")

elif tab == "Demo":
    st.subheader(" Streamlit Components Demo")
    st.write("This page demonstrates various Streamlit widgets and charts to meet your 'use many components' requirement.")

    st.write("###  Input Widgets")
    st.checkbox("I agree to the terms")
    st.radio("Choose a pet", ["Cats", "Dogs", "Birds"])
    st.selectbox("Favorite programming language", ["Python", "Java", "C++", "Kotlin", "PHP"])
    st.multiselect("Technologies you use", ["HTML", "CSS", "React", "Streamlit", "MySQL"])
    st.slider("Select a value", 0, 100, 50)
    st.select_slider("Choose size", ["S", "M", "L", "XL"])
    st.text_input("Enter your name")
    st.number_input("Enter your age", 1, 120)
    st.text_area("Your feedback")
    st.date_input("Select a date")
    st.time_input("Pick a time")
    st.color_picker("Pick your favorite color")

    st.write("### File & Media Inputs")
    st.file_uploader("Upload a file (any type)")
    st.camera_input("Take a photo")
    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")

    st.write("###  Buttons and Links")
    st.button("Click me")
    st.link_button("Go to Streamlit Docs", "https://docs.streamlit.io")
    st.download_button("Download Example Text", data="Hello Streamlit!", file_name="example.txt")

    st.write("### Metrics and Status")
    st.metric(label="Completed Projects", value=12, delta="+3")
    st.metric(label="Hours Coded", value="500+", delta="↑10%")
    st.progress(70)
    with st.spinner("Loading..."):
        time.sleep(1)
    st.success("Task completed!")

    st.write("###  Demo Charts")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Python", "Java", "C++"]
    )

    st.line_chart(chart_data)
    st.bar_chart(chart_data)
    st.area_chart(chart_data)

    st.write("#### Scatter Chart")
    fig, ax = plt.subplots()
    ax.scatter(chart_data["Python"], chart_data["Java"])
    ax.set_xlabel("Python")
    ax.set_ylabel("Java")
    st.pyplot(fig)

    st.write("#### Pie Chart")
    fig2, ax2 = plt.subplots()
    ax2.pie([30, 25, 20, 15, 10], labels=["Python", "Java", "C++", "Kotlin", "PHP"], autopct="%1.1f%%")
    ax2.axis("equal")
    st.pyplot(fig2)

    st.write("###  Expanders and JSON Display")
    with st.expander("See JSON data"):
        st.json({"name": "Joseph", "role": "Developer", "skills": ["Python", "Java", "Streamlit"]})
    st.code("print('Hello Sir!')")

st.write("---")
st.caption("©2025 Joseph Victor Novabos. All Rights Reserved")
