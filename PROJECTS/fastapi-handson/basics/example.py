from fastapi import FastAPI, status, Request

app = FastAPI()


students_db = [
    {
        'id': 1,
        'name': 'Groot',
        'college': 'MJIT',
        'gpa': 4.8,
        'stream': 'Electronics'
    },
    {
        'id': 2,
        'name': 'Ravi',
        'college': 'NGIT',
        'gpa': 2.9,
        'stream': 'Civil'
     }
    ,
    {
        'id': 3,
        'name': 'Rolex',
        'college': 'CU',
        'gpa': 4.8,
        'stream': 'Computers'
    }
]


# root endpoint
@app.get("/")
async def root() -> dict:
    return {"message": "Hi, Greetings from fastapi rest service, UP & Running."}


# get endpoint
@app.get("/api/greet")
async def greet() -> str:
    return f'Hello Welcome to fast api session'


# get endpoint with path variable
@app.get("/api/greet/{name}")
async def greet_user(name: str) -> dict:
    return {"message": f"Hello {name}"}


# get endpoint with query params
@app.get("/api/add")
async def addition(num1: int, num2: int) -> dict:
    return {"addition": num1 + num2}


# get endpoint with query params
@app.get("/api/student", status_code=status.HTTP_200_OK)
async def read_item(student_id: int = None, student_name: str | None = None):
    for student in students_db:
        print(student, student_id)
        if student_id == student.get('id') or student_name == student.get('name'):
            return {'data': student}
    else:
        return {'message': f'no student with id {student_id}'}


# post endpoint accepts dict as request
@app.post("/api/student", status_code=status.HTTP_201_CREATED)
async def add_student(student: dict) -> dict:
    students_db.append(student)
    return {'count': len(students_db), 'data': students_db}
