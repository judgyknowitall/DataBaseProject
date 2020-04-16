/*All the tables are populated with the exception of tutors.*/

-- admin
INSERT INTO admin VALUES("Sam1", "Sam", "Admin123");
INSERT INTO admin VALUES("Zahra1", "Zahra", "Admin123");
INSERT INTO admin VALUES("Kaynen1", "Kaynen", "Admin123");


-- student
INSERT INTO student Values("jack92", "Jack smith", "default1");
INSERT INTO student Values("Kate2002", "Kate Mia", "default2");
INSERT INTO student Values("Mike", "Mike Vause", "default3");


-- tutor
INSERT INTO tutor Values(
"James2020", "James", "tdefault2", "I have over a decade of tutoring experience. I am extremely patient and understanding with students.",
"Sam1", TRUE, TRUE, 45
);

INSERT INTO tutor Values(
"BestTutor", "Jack", "tdefault1",
"I am a student a 3rd yr Engineering Student at UofA, I have 3yrs of experience tutoring more than 50 students.",
Null, FALSE, FALSE, 45
);


INSERT INTO tutor Values(
"Rachelle", "Rachelle, B.Sc.", "tdefault3",
"I am a student a 3rd yr Engineering Student at UofA, I have 3yrs of experience tutoring more than 50 students.",
Null, FALSE, FALSE, 45
);

INSERT INTO tutor Values(
"Shukla", "ShuklaC", "tdefault4",
"Master of Science in Chemistry and Bachelor of Education. Certified teacher , 20 Years teaching experience.",
"Zahra1", TRUE, TRUE, 50
);

INSERT INTO tutor Values(
"Claire90", "Claire", "tdefault5",
"Certified English teacher.",
"Sam1", TRUE, TRUE, 40
);


-- tutor_subject_expertise
INSERT INTO tutor_subject_expertise Values("BestTutor", "Math");
INSERT INTO tutor_subject_expertise Values("BestTutor", "Comp. Sci");
INSERT INTO tutor_subject_expertise Values ("James2020", "Biology");
INSERT INTO tutor_subject_expertise Values("Rachelle", "Math");
INSERT INTO tutor_subject_expertise Values("Shukla", "Chemistry");


-- moderates
INSERT INTO moderates VALUES("Kaynen1", "jack92", "BestTutor");
INSERT INTO moderates VALUES("Sam1", "Kate2002", "Rachelle");


-- payment
INSERT INTO payment values(1, 45.00, CURRENT_TIMESTAMP, "jack92", "Rachelle");

INSERT INTO payment(Amount, SUserName, TUserName)
VALUES(45.00, "jack92", "Shukla");

INSERT INTO payment(Amount, SUserName, TUserName)
VALUES(90, "Mike",  "BestTutor");


-- tutors
INSERT INTO tutors values(1, "Shukla", "jack92", "2020-01-01", NULL);
INSERT INTO tutors(TUserName, SUserName, StartDate, EndDate)
values("BestTutor", "Mike", "2020-01-10", "2020-04-15");
INSERT INTO tutors(TUserName, SUserName, StartDate, EndDate)
values("James2020", "Kate2002", "2018-12-31", "2019-01-01");


-- review
INSERT INTO review values(
"Shukla", "jack92", 4,
"I used Shukla to get prepared for my final exam and It was a great experience.",
NULL);

INSERT INTO review values(
"BestTutor","Mike", 4,
"He was great!", NULL);

INSERT INTO review values(
"James2020","Mike", 5,
"James was my tutor in the last semester, he is knowledgeable and was able to answer all of my Biology questions. Strongley recommended! ",
NULL);


-- location
INSERT INTO location VALUES("T1X0L3", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T2C0P3", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T1X0L5", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T2C4T3", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T1C0T2", NULL, "Calgary", "Canada");

INSERT INTO location VALUES("T2N2G5", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T2S0B5", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T2S0B8", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T2M2S2", NULL, "Calgary", "Canada");



-- student_meets_in
INSERT INTO student_meets_in VALUES("Mike", "T1X0L3");
INSERT INTO student_meets_in VALUES("Mike", "T2C0P3");
INSERT INTO student_meets_in VALUES("Mike","T2N2G5");
INSERT INTO student_meets_in VALUES("Mike","T2S0B5");


INSERT INTO student_meets_in VALUES("jack92", "T1C0T2");
INSERT INTO student_meets_in VALUES("jack92", "T2C4T3");
INSERT INTO student_meets_in VALUES("jack92","T2M2S2");

INSERT INTO student_meets_in VALUES("kate2002", "T1X0L3");
INSERT INTO student_meets_in VALUES("kate2002", "T1X0L5");
INSERT INTO student_meets_in VALUES("kate2002", "T2C4T3");


-- tutor_meets_in
INSERT INTO tutor_meets_in VALUES("besttutor","T1X0L3");
INSERT INTO tutor_meets_in VALUES("besttutor","T2S0B5");
INSERT INTO tutor_meets_in VALUES("besttutor","T2N2G5");

INSERT INTO tutor_meets_in VALUES("shukla","T1X0L3");
INSERT INTO tutor_meets_in VALUES("shukla","T2C0P3");
INSERT INTO tutor_meets_in VALUES("shukla","T2S0B5");


INSERT INTO tutor_meets_in VALUES("Rachelle","T2C0P3");
INSERT INTO tutor_meets_in VALUES("Rachelle","T1C0T2");
INSERT INTO tutor_meets_in VALUES("Rachelle","T2S0B5");


INSERT INTO tutor_meets_in VALUES("James2020","T2S0B5");
INSERT INTO tutor_meets_in VALUES("James2020","T2N2G5");
INSERT INTO tutor_meets_in VALUES("James2020","T2S0B8");


-- course
INSERT INTO course VALUES("Mathematics", "30-1", "High School", "Math");
INSERT INTO course VALUES("Mathematics", "20-1", "High School", "Math");
INSERT INTO course VALUES("Mathematics", "10-c", "High School", "Math");

INSERT INTO course VALUES("English", "30-1", "High School", "English");
INSERT INTO course VALUES("English", "30-2", "High School", "English");

INSERT INTO course VALUES("Science", "20", "High School", "Science");
INSERT INTO course VALUES("Science", "24", "High School", "Science");

INSERT INTO course VALUES("Social Studies", "30-1", "High School", "Social");
INSERT INTO course VALUES("Social Studies", "30-2", "High School", "Social");


-- enrolled_in
INSERT INTO enrolled_in Values("jack92", "Mathematics", "30-1");
INSERT INTO enrolled_in Values("jack92", "English", "30-1");

INSERT INTO enrolled_in Values("Mike", "Science", "20");

INSERT INTO enrolled_in Values("kate2002", "English", "30-1");
INSERT INTO enrolled_in Values("kate2002", "Mathematics", "30-1");


-- can_tutor
INSERT INTO can_tutor VALUES("besttutor", "Mathematics", "30-1");
INSERT INTO can_tutor VALUES("besttutor", "Mathematics", "20-1");
INSERT INTO can_tutor VALUES("besttutor", "Mathematics", "10-c");

INSERT INTO can_tutor VALUES("Shukla", "Science", "20");
INSERT INTO can_tutor VALUES("Shukla", "Science", "24");

INSERT INTO can_tutor VALUES("Claire90", "English", "30-1");
INSERT INTO can_tutor VALUES("Claire90", "English", "30-2");


-- school
INSERT INTO school VALUES("Queen Elizabeth High",  "T2N2G5");
INSERT INTO school VALUES("Western Canada High", "T2S0B5");
INSERT INTO school VALUES("Saint Marys High School", "T2S0B8");
INSERT INTO school VALUES("Crescent Heights High School", "T2M2S2");


-- offers
INSERT INTO offers VALUES("Queen Elizabeth High", "Mathematics", "30-1");
INSERT INTO offers VALUES("Queen Elizabeth High", "Mathematics", "20-1");
INSERT INTO offers VALUES("Queen Elizabeth High", "Mathematics", "10-c");
INSERT INTO offers VALUES("Queen Elizabeth High", "English", "30-2");
INSERT INTO offers VALUES("Queen Elizabeth High", "English", "30-1");


INSERT INTO offers VALUES("Crescent Heights High School", "Mathematics", "30-1");
INSERT INTO offers VALUES("Crescent Heights High School", "Mathematics", "20-1");
INSERT INTO offers VALUES("Crescent Heights High School", "Mathematics", "10-c");
INSERT INTO offers VALUES("Crescent Heights High School", "Social Studies", "30-1");
INSERT INTO offers VALUES("Crescent Heights High School", "Social Studies", "30-2");
INSERT INTO offers VALUES("Crescent Heights High School", "English", "30-2");


INSERT INTO offers VALUES("Saint Marys High School", "Mathematics", "30-1");
INSERT INTO offers VALUES("Saint Marys High School", "Mathematics", "20-1");
INSERT INTO offers VALUES("Saint Marys High School", "Mathematics", "10-c");
INSERT INTO offers VALUES("Saint Marys High School", "Social Studies", "30-1");
INSERT INTO offers VALUES("Saint Marys High School", "Social Studies", "30-2");
INSERT INTO offers VALUES("Saint Marys High School", "English", "30-2");


INSERT INTO offers VALUES("Western Canada High", "Science", "20");
INSERT INTO offers VALUES("Western Canada High", "Science", "24");
INSERT INTO offers VALUES("Western Canada High", "Social Studies", "30-1");
INSERT INTO offers VALUES("Western Canada High", "Social Studies", "30-2");
