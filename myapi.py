from  fastapi import FastAPI,Path
app= FastAPI()

students = {
    1: {
        "name":"fathima",
        "age":17,
        "class":"year 12"
    }
}
@app.get("/")
def index():
    return {"name":"first data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(None, description="The ID of the student you want to view",gt=0,lt=3)):
    return(students[student_id])

@app.get("/get-by-name")
def get_student(student_name: str):
    for student_id in students:
        if students[student_id]["name"]== student_name:
            return(students[student_id])
    return("Data":"not found")

