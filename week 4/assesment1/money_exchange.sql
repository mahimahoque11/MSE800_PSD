-- Money Exchange System Database Schema

CREATE TABLE IF NOT EXISTS CUSTOMER (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address TEXT
);

CREATE TABLE IF NOT EXISTS CURRENCY (
    CurrencyCode CHAR(3) PRIMARY KEY,
    CurrencyName VARCHAR(50),
    Symbol VARCHAR(5),
    Country VARCHAR(50),
    Description TEXT
);

CREATE TABLE IF NOT EXISTS ACCOUNT (
    AccountID INT PRIMARY KEY,
    AccountNumber VARCHAR(20) UNIQUE,
    AccountType VARCHAR(20),
    Balance DECIMAL(18, 2),
    CurrencyCode CHAR(3),
    CustomerID INT,
    FOREIGN KEY (CurrencyCode) REFERENCES CURRENCY(CurrencyCode),
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID)
);

CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Role VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS "TRANSACTION" (
    TransactionID INT PRIMARY KEY,
    TransactionDate DATETIME,
    Amount DECIMAL(18, 2),
    FromCurrency CHAR(3),
    ToCurrency CHAR(3),
    ExchangeRate DECIMAL(10, 6),
    AccountID INT,
    EmployeeID INT,
    FOREIGN KEY (AccountID) REFERENCES ACCOUNT(AccountID),
    FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEE(EmployeeID),
    FOREIGN KEY (FromCurrency) REFERENCES CURRENCY(CurrencyCode),
    FOREIGN KEY (ToCurrency) REFERENCES CURRENCY(CurrencyCode)
);