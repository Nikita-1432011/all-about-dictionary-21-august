student_data = {"id1" :
    {"name": ["Nikita"],
     "class":["A"],
     "subject": ["English", "Maths", "Science"] },
    "id2" :
    {"name": ["unnat"],
     "class":["A"],
     "subject": ["English", "Maths", "Science"] },
    "id3" :
    {"name": ["Hrishaan"],
     "class":["A"],
     "subject": ["English", "Maths", "Science"] },
    "id4" :
    {"name": ["Nikita"],
     "class":["A"],
     "subject": ["English", "Maths", "Science"] },

}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)
    