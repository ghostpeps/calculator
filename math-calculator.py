import streamlit as st

st.title(":material/Calculate: Math Calculator") #title
x = st.selectbox(label="Choose something to solve:", options=["Area of a Square", "Perimeter of a Square", "Area of a Rectangle", "Perimeter of a Rectangle", "Area of a Triangle", "Perimeter of a Triangle", "Hypotenuse of a Triangle", "Circumference of a Circle", "Area of a Circle"]) #creates the dropdown menu
while True: #runs until user selects something
  if x == "Area of a Square" or x == "Perimeter of a Square": #checks which one user selected
    st.image(image="s-removebg-preview.png")
    break
  elif x == "Area of a Rectangle" or x == "Perimeter of a Rectangle":
    st.image(image="r-removebg-preview.png")
    break
  elif x == "Area of a Triangle" or x == "Perimeter of a Triangle" or x == "Hypotenuse of a Triangle":
    st.image(image="t-removebg-preview.png")
    break
  elif x == "Circumference of a Circle" or x == "Area of a Circle":
    st.image(image="c-removebg-preview.png")
    break
