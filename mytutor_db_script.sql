CREATE TABLE admin (
    AUserName   VARCHAR(20) PRIMARY kEY,
    AName   VARCHAR(20) NOT NULL,
    APassword   VARCHAR(16) NOT NULL

);

CREATE TABLE student (
    SUserName   VARCHAR(20) PRIMARY KEY,
    SName   VARCHAR(20)   NOT NULL,
    SPassword   VARCHAR(20) NOT NULL

);


CREATE TABLE tutor(
    TUserName VARCHAR(20) PRIMARY KEY,
    Tname   VARCHAR(20) NOT NULL,
    Tpassword   VARCHAR(16) NOT NULL,
    Background  VARCHAR(200),
    AUserName   VARCHAR(20),
    Result  BOOLEAN DEFAULT FALSE,
    PoliceCheck BOOLEAN DEFAULT FALSE,
    Rate(hr) INT NOT NULL,
    FOREIGN KEY (AUserName) REFERENCES admin(AUserName)

);

CREATE TABLE tutor_subject_expertise (
    TUserName   VARCHAR(20),
    SubjectExpertise VARCHAR(20),
    PRIMARY KEY (TUserName, SubjectExpertise),
    FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)

);

CREATE TABLE moderates(
    AUserName   VARCHAR(20),
    SUserName   VARCHAR(20),
    TUserName VARCHAR(20),
    PRIMARY KEY(AUserName, SUserName , TUserName),
    FOREIGN KEY(AUserName) REFERENCES admin(AUserName),
    FOREIGN KEy (SUserName) REFERENCES student(SUserName),
    FOREIGN KEy (TUserName) REFERENCES tutor(TUserName)

);

/*Primary key of this table was not unique in the RM, new attribute called payment_id is added*/
CREATE TABLE payment(
    Payment_id INT AUTO_INCREMENT,
    Amount DECIMAL(6,2) NOT NULL,
    PaymentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    SUserName VARCHAR(20),
    TUserName VARCHAR(20),
    PRIMARY KEY(payment_id),
    FOREIGN KEY(SUserName)REFERENCES student(SUserName),
    FOREIGN KEY(TUserName)REFERENCES tutor(TUserName)

);

/*Primary key of this table was not unique in the RM, new attribute called tutoring_id is added*/
CREATE TABLE tutors(
    Tutoring_id INT AUTO_INCREMENT,
    TUserName VARCHAR(20),
    SUserName VARCHAR(20),
    StartDate TIMESTAMP NOT NULL,
    EndDATE TIMESTAMP NOT NULL,
    PRIMARY KEY(Tutoring_id),
    FOREIGN KEY(SUserName)REFERENCES student(SUserName),
    FOREIGN KEY(TUserName)REFERENCES tutor(TUserName)

);

CREATE TABLE review(
    TUserName VARCHAR(20),
    SUserName VARCHAR(20),
    Rating INT NOT NULL CHECK (0<=Rating<=5),
    Comment VARCHAR(120) NOT NULL,
    Accuracy INT DEFAULT 0,
    PRIMARY KEY (TUserName, SUserName),
    FOREIGN KEY(SUserName)REFERENCES student(SUserName),
    FOREIGN KEY(TUserName)REFERENCES tutor(TUserName)

);




CREATE TABLE location(
    PostalCode CHAR(6) NOT NULL PRIMARY KEY,
    District VARCHAR(20),
    City VARCHAR(20) NOT NULL,
    Country VARCHAR(20) DEFAULT 'Canada'

);


/*This table didnt have a primary key in the RM, so a composite PM is chosen.*/
CREATE TABLE student_meets_in(
    SUserName VARCHAR(20) NOT NULL,
    PostalCode CHAR(6),
    PRIMARY KEY(SUserName, PostalCode),
    FOREIGN KEY(SUserName)REFERENCES student(SUserName),
    FOREIGN KEY(PostalCode)REFERENCES location(PostalCode)

);

/*This table didnt have a primary key in the RM, so a composite PM is chosen.*/
CREATE TABLE tutor_meets_in(
    TUserName VARCHAR(20) NOT NULL,
    PostalCode CHAR(6),
    PRIMARY KEY(TUserName, PostalCode),
    FOREIGN KEY(TUserName)REFERENCES tutor(TUserName),
    FOREIGN KEY(PostalCode)REFERENCES location(PostalCode)

);


CREATE TABLE course(
    CName VARCHAR(20) NOT NULL,
    CNumber VARCHAR(20) NOT NULL,
    Level INT,
    Subject VARCHAR(20),
    PRIMARY KEY(CName, CNumber)

);

CREATE TABLE enrolled_in(
    SUserName VARCHAR(20)   NOT NULL,
    CName VARCHAR(20)   NOT NULL,
    CNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY(SUserName, CName, CNumber),
    FOREIGN KEY(SUserName) REFERENCES student(SUserName),
    FOREIGN KEY(CName, CNumber) REFERENCES course(CName, CNumber)

);


CREATE TABLE can_tutor(
    TUserName VARCHAR(20) NOT NULL,
    CName VARCHAR(20)   NOT NULL,
    CNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY(TUserName, CName, CNumber),
    FOREIGN KEY(TUserName) REFERENCES tutor(TUserName),
    FOREIGN KEY(CName, CNumber) REFERENCES course(CName, CNumber)

);


CREATE TABLE school(
    SchoolName VARCHAR(20) PRIMARY KEY,
    PostalCode CHAR(6),
    FOREIGN KEY(PostalCode)REFERENCES location(PostalCode)

);


CREATE TABLE offers(
    SchoolName VARCHAR(20),
    CName VARCHAR(20),
    CNumber VARCHAR(20),
    PRIMARY KEY(SchoolName, CName, CNumber),
    FOREIGN KEY(SchoolName) REFERENCES school(SchoolName),
    FOREIGN KEY(CName, CNumber) REFERENCES course(CName, CNumber)

);

describe offers;