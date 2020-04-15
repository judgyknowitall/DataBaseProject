/*Create tables within schema*/

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
    Rate INT NOT NULL,
    CONSTRAINT TAFK
      FOREIGN KEY (AUserName) REFERENCES admin(AUserName)
        ON DELETE SET NULL

);

CREATE TABLE tutor_subject_expertise (
    TUserName   VARCHAR(20),
    SubjectExpertise VARCHAR(20),
    PRIMARY KEY (TUserName, SubjectExpertise),
    CONSTRAINT TSETFK
      FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)
        ON DELETE CASCADE

);

CREATE TABLE moderates(
    AUserName   VARCHAR(20),
    SUserName   VARCHAR(20),
    TUserName VARCHAR(20),
    PRIMARY KEY(AUserName, SUserName , TUserName),
    CONSTRAINT MAFK
      FOREIGN KEY (AUserName) REFERENCES admin(AUserName)
        ON DELETE CASCADE,
    CONSTRAINT MSFK
	  FOREIGN KEy (SUserName) REFERENCES student(SUserName)
        ON DELETE CASCADE,
    CONSTRAINT MTFK
      FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)
        ON DELETE CASCADE

);

/*Primary key of this table was not unique in the RM, new attribute called payment_id is added*/
CREATE TABLE payment(
    Payment_id INT AUTO_INCREMENT,
    Amount DECIMAL(6,2) NOT NULL,
    PaymentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    SUserName VARCHAR(20),
    TUserName VARCHAR(20),
    PRIMARY KEY(payment_id),
	CONSTRAINT PSFK
	  FOREIGN KEy (SUserName) REFERENCES student(SUserName)
        ON DELETE SET NULL,
    CONSTRAINT PTFK
      FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)
        ON DELETE SET NULL

);

/*Primary key of this table was not unique in the RM, new attribute called tutoring_id is added*/
CREATE TABLE tutors(
    Tutoring_id INT AUTO_INCREMENT,
    TUserName VARCHAR(20),
    SUserName VARCHAR(20),
    StartDate TIMESTAMP NOT NULL,
    EndDATE TIMESTAMP NOT NULL,
    PRIMARY KEY(Tutoring_id),
	CONSTRAINT TSFK
	  FOREIGN KEy (SUserName) REFERENCES student(SUserName)
        ON DELETE SET NULL,
    CONSTRAINT TTFK
      FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)
        ON DELETE SET NULL

);

CREATE TABLE review(
    TUserName VARCHAR(20),
    SUserName VARCHAR(20),
    Rating INT NOT NULL,
    CONSTRAINT Rating_Ck CHECK (Rating BETWEEN 1 AND 5),
    Comment VARCHAR(300) NOT NULL,
    Accuracy INT DEFAULT 0,
    PRIMARY KEY (TUserName, SUserName),
    CONSTRAINT RSFK
	  FOREIGN KEy (SUserName) REFERENCES student(SUserName)
        ON DELETE CASCADE,
    CONSTRAINT RTFK
      FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)
        ON DELETE CASCADE

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
    CONSTRAINT SMISFK
	  FOREIGN KEy (SUserName) REFERENCES student(SUserName)
        ON DELETE CASCADE,
	CONSTRAINT SMIPCFK
      FOREIGN KEY(PostalCode)REFERENCES location(PostalCode)
        ON DELETE CASCADE

);

/*This table didnt have a primary key in the RM, so a composite PM is chosen.*/
CREATE TABLE tutor_meets_in(
    TUserName VARCHAR(20) NOT NULL,
    PostalCode CHAR(6),
    PRIMARY KEY(TUserName, PostalCode),
    CONSTRAINT TMITFK
      FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)
        ON DELETE CASCADE,
    CONSTRAINT TMIPCFK
      FOREIGN KEY(PostalCode)REFERENCES location(PostalCode)
        ON DELETE CASCADE

);


CREATE TABLE course(
    CName VARCHAR(20) NOT NULL,
    CNumber VARCHAR(20) NOT NULL,
    Level VARCHAR(20),
    Subject VARCHAR(20),
    PRIMARY KEY(CName, CNumber)

);

CREATE TABLE enrolled_in(
    SUserName VARCHAR(20)   NOT NULL,
    CName VARCHAR(20)   NOT NULL,
    CNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY(SUserName, CName, CNumber),
    CONSTRAINT EISFK
	  FOREIGN KEy (SUserName) REFERENCES student(SUserName)
        ON DELETE CASCADE,
	CONSTRAINT EICFK
	  FOREIGN KEY(CName, CNumber) REFERENCES course(CName, CNumber)
        ON DELETE CASCADE

);


CREATE TABLE can_tutor(
    TUserName VARCHAR(20) NOT NULL,
    CName VARCHAR(20)   NOT NULL,
    CNumber VARCHAR(20) NOT NULL,
    PRIMARY KEY(TUserName, CName, CNumber),
    CONSTRAINT CTTFK
      FOREIGN KEY(TUserName) REFERENCES tutor(TUserName)
        ON DELETE CASCADE,
    CONSTRAINT CTCFK
	  FOREIGN KEY(CName, CNumber) REFERENCES course(CName, CNumber)
        ON DELETE CASCADE

);


CREATE TABLE school(
    SchoolName VARCHAR(45) PRIMARY KEY,
    PostalCode CHAR(6),
    CONSTRAINT SPCFK
      FOREIGN KEY(PostalCode)REFERENCES location(PostalCode)
        ON DELETE SET NULL

);


CREATE TABLE offers(
    SchoolName VARCHAR(45),
    CName VARCHAR(20),
    CNumber VARCHAR(20),
    PRIMARY KEY(SchoolName, CName, CNumber),
    CONSTRAINT OSNFK
      FOREIGN KEY(SchoolName) REFERENCES school(SchoolName)
        ON DELETE CASCADE,
    CONSTRAINT OCFK
	  FOREIGN KEY(CName, CNumber) REFERENCES course(CName, CNumber)
        ON DELETE CASCADE

);

describe offers;