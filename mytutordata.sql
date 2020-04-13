--admin
INSERT INTO admin VALUES("Sam1", "Sam", "Admin123");
INSERT INTO admin VALUES("Zahra1", "Zahra", "Admin123");
INSERT INTO admin VALUES("Kaynen1", "Kaynen", "Admin123");

--student
INSERT INTO student Values("jack92", "Jack smith", "default1");
INSERT INTO student Values("Kate2002", "Kate Mia", "default2");
INSERT INTO student Values("Mike", "Mike Vause", "default3");

--tutor
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


--tutor_subject_expertise
INSERT INTO tutor_subject_expertise Values("BestTutor", "Math");
INSERT INTO tutor_subject_expertise Values("BestTutor", "Comp. Sci");
INSERT INTO tutor_subject_expertise Values ("James2020", "Biology");
INSERT INTO tutor_subject_expertise Values("Rachelle", "Math");
INSERT INTO tutor_subject_expertise Values("Shukla", "Chemistry");


--moderates
INSERT INTO moderates VALUES("Kaynen1", "jack92", "BestTutor");
INSERT INTO moderates VALUES("Sam1", "Kate2002", "Rachelle");

--payment
INSERT INTO payment values(1, 45.00, CURRENT_TIMESTAMP, "jack92", "Rachelle");

INSERT INTO payment(Amount, SUserName, TUserName)
VALUES(45.00, "jack92", "Shukla");

INSERT INTO payment(Amount, SUserName, TUserName)
VALUES(90, "Mike",  "BestTutor");


--review
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

--location
INSERT INTO location VALUES("T1X0L3", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T2C0P3", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T1X0L5", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T2C4T3", NULL, "Calgary", "Canada");
INSERT INTO location VALUES("T1C0T2", NULL, "Calgary", "Canada");


--student_meets_in
INSERT INTO student_meets_in VALUES("Mike", "T1X0L3");
INSERT INTO student_meets_in VALUES("Mike", "T2C0P3");

INSERT INTO student_meets_in VALUES("jack92", "T1C0T2");
INSERT INTO student_meets_in VALUES("jack92", "T2C4T3");

INSERT INTO student_meets_in VALUES("kate2002", "T1X0L3");
INSERT INTO student_meets_in VALUES("kate2002", "T1X0L5");
INSERT INTO student_meets_in VALUES("kate2002", "T2C4T3");


--tutor_meets_in
INSERT INTO tutor_meets_in VALUES("besttutor","T1X0L3");
INSERT INTO tutor_meets_in VALUES("besttutor","T1X0L5");

INSERT INTO tutor_meets_in VALUES("shukla","T1X0L3");
INSERT INTO tutor_meets_in VALUES("shukla","T2C0P3");
INSERT INTO tutor_meets_in VALUES("shukla","T1C0T2");


INSERT INTO tutor_meets_in VALUES("Rachelle","T2C0P3");
INSERT INTO tutor_meets_in VALUES("Rachelle","T1C0T2");

INSERT INTO tutor_meets_in VALUES("James2020","T1X0L3");



















