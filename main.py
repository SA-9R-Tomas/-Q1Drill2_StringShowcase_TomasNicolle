from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    # ✅ Assign input values to variables
    fname = document.querySelector("#fname").value
    lname = document.querySelector("#lname").value
    birthdate = document.querySelector("#birthdate").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value
    subject = document.querySelector("#subject").value

    # ✅ Clear old output
    document.querySelector("#output").innerText = ""

    # ✅ Multiline string with escape characters (\t, \", \\)
    message = f"""👤 Student Profile
\tFirst Name : \"{fname}\"
\tLast Name  : \"{lname}\"
\tBirthdate  : {birthdate}
\tAge        : {age}
\tSchool     : {school}
\tFav. Subj. : {subject}\\Choice

✏️ Notes:
{fname} {lname} is {age} years old, studies at \"{school}\",
was born on {birthdate}, and their as a favorite subject is {subject}.
"""

    # ✅ Display formatted profile
    display(message, target="output")

