from student import student_details
def test_student_details():
    name = "Alice"
    USN = 272
    division = "E"
    age = 20
    expected_output = {
        "Name": "Alice",
        "USN": 272,
        "Division": "E",
        "Age": 20,
    }
    assert student_details(name, USN, division, age) == expected_output