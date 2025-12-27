def student_details(name,USN,division,age):
    result = (
    f"Name: {name}"
    f"USN: {USN}"
    f"Division: {division}"
    f"Age: {age}"
    )
    return result 
if __name__ == "__main__":
    name = "Alice"
    USN = 272
    Division = "E"
    Age = 20
    student_details(name,USN,Division,Age)
