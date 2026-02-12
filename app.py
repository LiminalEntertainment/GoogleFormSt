import streamlit as st

st.title("📚 School Quiz")
st.write("Answer the questions below and click Submit to see your score.")

# Questions

q1 = st.number_input("1. What is 5 + 7?", step=1)
q2 = st.text_input("2. What planet do we live on?")
q3 = st.number_input("3. How many days are in a week?", step=1)
q4 = st.text_input("4. What is the capital of France?")
q5 = st.number_input("5. What is 9 x 3?", step=1)
q6 = st.text_input("6. What gas do humans need to breathe?")
q7 = st.number_input("7. How many sides does a triangle have?", step=1)
q8 = st.text_input("8. What is the largest ocean on Earth?")
q9 = st.number_input("9. What is 100 divided by 10?", step=1)
q10 = st.text_input("10. What language is primarily spoken in Spain?")

submit = st.button("Submit Quiz")

if submit:
    score = 0

    # Checking answers
    if q1 == 12:
        score += 1

    if q2.lower() == "earth":
        score += 1

    if q3 == 7:
        score += 1

    if q4.lower() == "paris":
        score += 1

    if q5 == 27:
        score += 1

    if q6.lower() == "oxygen":
        score += 1

    if q7 == 3:
        score += 1

    if q8.lower() == "pacific ocean":
        score += 1

    if q9 == 10:
        score += 1

    if q10.lower() == "spanish":
        score += 1

    st.write("✅ Quiz Submitted!")
    st.write("Your score is:", score, "/ 10")

    if score == 10:
        st.write("🎉 Excellent! Perfect score!")
    elif score >= 7:
        st.write("👍 Great job!")
    elif score >= 4:
        st.write("🙂 Not bad, keep studying!")
    else:
        st.write("📖 Keep practicing and try again!")
else:
    st.write("Click Submit Quiz when you're ready!")
