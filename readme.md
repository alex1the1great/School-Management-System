# School Management System Model.
### [Models File](./uptechsys/school_management/models.py)

### Student
- id: IntegerField, PrimaryKey
- name: CharField
- age: IntegerField
- email: EmailField
- dob: DateField
- address: CharField
- father_name: CharField
- mother_name: CharField
- father_phone_number: IntegerField
- mother_phone_number: IntegerField
- father_occupation: CharField
- mother_occupation: CharField

### School
- id: IntegerField, PrimaryKey
- name: CharField
- address: CharField
- school_type: CharField
- phone_number: IntegerField
- student: ForeignKey(Student)
- established: DateField

### Teacher
- id: IntegerField, PrimaryKey
- name: CharField
- phone_number: IntegerField
- address: CharField
- school: ManyToManyField(School)
- salary: FloatField

### Faculty
- id: IntegerField, PrimaryKey
- name: CharField
- student: OneToOneField(Student)
- teacher: OneToOneField(Teacher)

### Subject
- id: IntegerField, PrimaryKey
- name: CharField
- subject_teacher: ManyToManyField(Teacher)
- subject_faculty: ManyToManyField(Faculty)

### Exam
- id: IntegerField, PrimaryKey
- name: CharField
- exam_date: DateTimeField
- student_exam: ForeignKey(Student)