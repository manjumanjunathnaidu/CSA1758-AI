% Facts: name(Name, DOB).
name("Alice", "1990-05-14").
name("Bob", "1985-11-23").
name("Charlie", "2000-02-18").
name("Diana", "1995-07-09").

% Querying all people in the database
all_people(Name, DOB) :-
    name(Name, DOB).

% Querying a person by name
person_dob(Name, DOB) :-
    name(Name, DOB).

% Querying a person by DOB
person_by_dob(DOB, Name) :-
    name(Name, DOB).