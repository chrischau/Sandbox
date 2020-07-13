BEGIN TRANSACTION ParkT2MarginCalls

    IF OBJECT_ID('DatabaseSchema') IS NOT NULL
        DROP TABLE DatabaseSchema

    IF OBJECT_ID('Managers') IS NOT NULL
        DROP TABLE Managers

    IF OBJECT_ID('Employees') IS NOT NULL
        DROP TABLE Employees

    
    GO
        
    CREATE TABLE DatabaseSchema (
        DatabaseSchemaNumber INT NOT NULL
    )
    GO

    CREATE TABLE Employees (
        EmployeeId BIGINT IDENTITY(1,1) NOT NULL,
        FirstName NVARCHAR (250) NOT NULL,
        MiddleName NVARCHAR (250) NULL,
        LastName NVARCHAR (250) NOT NULL,
        HomePhoneNumber NVARCHAR (20) NOT NULL,
        HomePhoneCountry INT NOT NULL,
        Department INT NOT NULL,
        CreatedTimestamp DATETIME NOT NULL,
        UpdatedTimestamp DATETIME NOT NULL,
        CreatedBy BIGINT NOT NULL,
        UpdatedBy BIGINT NOT NULL,
        Nationality INT NULL,
        Email NVARCHAR (250) NULL
    )
    GO

    CREATE TABLE Managers (
        ManagerId BIGINT NOT NULL,
        EmployeeId BIGINT NOT NULL,
        Region INT NOT NULL
    )
    GO

    ALTER TABLE Employees ADD CONSTRAINT PK_Employees PRIMARY KEY (EmployeeId)
    ALTER TABLE Employees WITH CHECK ADD CONSTRAINT FK_1_10_Managers_CreatedBy_REFERENCES_Employees_EmployeeId FOREIGN KEY (CreatedBy) REFERENCES Employees (EmployeeId)
    ALTER TABLE Employees WITH CHECK ADD CONSTRAINT FK_1_11_Managers_UpdatedBy_REFERENCES_Employees_EmployeeId FOREIGN KEY (UpdatedBy) REFERENCES Employees (EmployeeId)
    
    ALTER TABLE Managers WITH CHECK ADD CONSTRAINT FK_1_1_Managers_ManagerId_REFERENCES_Employees_EmployeeId FOREIGN KEY (ManagerId) REFERENCES Employees (EmployeeId)
    ALTER TABLE Managers WITH CHECK ADD CONSTRAINT FK_1_2_Managers_EmployeeId_REFERENCES_Employees_EmployeeId FOREIGN KEY (EmployeeId) REFERENCES Employees (EmployeeId)
    
    GO

    INSERT INTO DatabaseSchema (DatabaseSchemaNumber)
    VALUES (1)
    GO

COMMIT TRANSACTION ParkT2MarginCalls
