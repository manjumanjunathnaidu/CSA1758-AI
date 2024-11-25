% Facts: student_teacher_subject(Student, Teacher, Subject, SubjectCode).
student_teacher_subject("Alice", "Mr. Smith", "Mathematics", "MATH101").
student_teacher_subject("Bob", "Mrs. Johnson", "Physics", "PHYS201").
student_teacher_subject("Charlie", "Mr. Smith", "Mathematics", "MATH101").
student_teacher_subject("Diana", "Dr. Brown", "Chemistry", "CHEM301").
student_teacher_subject("Eve", "Mrs. Johnson", "Physics", "PHYS201").

% Rule to find a teacher for a specific student
teacher_for_student(Student, Teacher) :-
    student_teacher_subject(Student, Teacher, _, _).

% Rule to find the subject and code for a specific student
subject_for_student(Student, Subject, SubjectCode) :-
    student_teacher_subject(Student, _, Subject, SubjectCode).

% Rule to find all students taught by a specific teacher
students_of_teacher(Teacher, Student) :-
    student_teacher_subject(Student, Teacher, _, _).

% Rule to find all students studying a specific subject
students_of_subject(Subject, Student) :-
    student_teacher_subject(Student, _, Subject, _).