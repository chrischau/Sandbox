BEGIN TRANSACTION CreateUserTable

    IF OBJECT_ID('DatabaseSchema') IS NOT NULL
        DROP TABLE DatabaseSchema

    IF OBJECT_ID('Users') IS NOT NULL
        DROP TABLE Users

    CREATE TABLE DatabaseSchema (
        DatabaseSchemaNumber INT NOT NULL
    )
    GO

    CREATE TABLE Users (
        UserId BIGINT IDENTITY(1,1) NOT NULL,
        FirstName NVARCHAR (250) NOT NULL,
        MiddleName NVARCHAR (250) NULL,
        LastName NVARCHAR (250) NOT NULL,
        HomePhoneNumber NVARCHAR (20) NULL,
        HomePhoneCountry INT NULL,
        Nationality INT NOT NULL,
        Email NVARCHAR (250) NULL,        
        CreatedTimestamp DATETIME NOT NULL,
        UpdatedTimestamp DATETIME NOT NULL,
        CreatedBy BIGINT NOT NULL,
        UpdatedBy BIGINT NOT NULL        
    )
    GO
    
    INSERT INTO DatabaseSchema (DatabaseSchemaNumber)
    VALUES (1)
    GO

COMMIT TRANSACTION CreateUserTable
