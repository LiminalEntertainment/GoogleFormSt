import streamlit as st

st.title("School Information Form")
st.write("Please fill out the form below:")

# Question 1
name = st.text_input("1. What is your full name?")

# Question 2
age = st.number_input("2. What is your age?", min_value=5, max_value=100, step=1)

# Question 3
grade = st.number_input("3. What grade are you in?", min_value=1, max_value=12, step=1)

# Question 4
favorite_subject = st.text_input("4. What is your favorite subject?")

# Question 5
least_favorite_subject = st.text_input("5. What is your least favorite subject?")

# Question 6
hours_study = st.number_input("6. How many hours do you study per day?", min_value=0, max_value=24, step=1)

# Question 7
school_name = st.text_input("7. What is your school name?")

# Question 8
teacher_name = st.text_input("8. Who is your favorite teacher?")

# Question 9
activities = st.text_input("9. What extracurricular activities do you participate in?")

# Question 10
future_goal = st.text_input("10. What is your future career goal?")

# Submit button
submit = st.button("Submit Form")

# If/Else logic
if submit:
    if name == "" or favorite_subject == "" or school_name == "":
        st.write("⚠️ Please fill in all required text fields (Name, Favorite Subject, School Name).")
    else:
        st.write("✅ Form Submitted Successfully!")
        st.write("Here are your responses:")
        
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Grade:", grade)
        st.write("Favorite Subject:", favorite_subject)
        st.write("Least Favorite Subject:", least_favorite_subject)
        st.write("Hours Studied Per Day:", hours_study)
        st.write("School Name:", school_name)
        st.write("Favorite Teacher:", teacher_name)
        st.write("Extracurricular Activities:", activities)
        st.write("Future Career Goal:", future_goal)
else:
    st.write("Click the button above to submit your responses.")
