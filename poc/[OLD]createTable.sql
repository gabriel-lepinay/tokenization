CREATE TABLE my_table (
    id              CHAR(8),               --define the number of char
    token           CHAR(64) PRIMARY KEY,   --define the number of char
    id_app          CHAR(16),               --define the number of char
    raw_data        CHAR(256)               --define the number of char  #change to 100 for encrypted value
);

GRANT SELECT, INSERT, UPDATE ON my_table TO gaby;
