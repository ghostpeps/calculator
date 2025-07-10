import streamlit as st

st.title(":material/Calculate: Math Calculator") #title
x = st.selectbox(label="Choose something to solve:", options=["Area of a Square", "Perimeter of a Rectangle", "Area of a Triangle", "Perimeter of a Triangle", "Hypotenuse of a Triangle", "Circumference of a Circle", "Area of a Circle"]) #creates the dropdown menu
while True: #runs until user selects something
  if x == "Area of a Square": #checks which one user selected
    pass #replace with image
    break
