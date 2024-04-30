CREATE TABLE my_table (
    id              CHAR(8),
    token           CHAR(64) PRIMARY KEY,
    id_app          CHAR(16),
    raw_data        text
);

GRANT SELECT, INSERT, UPDATE ON my_table TO gaby;

```
 SELECT * FROM my_table;
 TRUNCATE TABLE my_table;
```