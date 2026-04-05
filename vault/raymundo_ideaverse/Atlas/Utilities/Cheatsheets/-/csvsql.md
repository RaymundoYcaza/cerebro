

Generate SQL statements for a CSV file or execute those statements directly on a database. In the latter case supports both creating tables and inserting data:

```bash
usage: csvsql [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b]
              [-p ESCAPECHAR] [-z FIELD_SIZE_LIMIT] [-e ENCODING] [-L LOCALE]
              [-S] [--blanks] [--null-value NULL_VALUES [NULL_VALUES ...]]
              [--date-format DATE_FORMAT] [--datetime-format DATETIME_FORMAT]
              [-H] [-K SKIP_LINES] [-v] [-l] [--zero] [-V]
              [-i {firebird,mssql,mysql,oracle,postgresql,sqlite,sybase}]
              [--db CONNECTION_STRING] [--query QUERIES] [--insert]
              [--prefix PREFIX] [--before-insert BEFORE_INSERT]
              [--after-insert AFTER_INSERT] [--tables TABLE_NAMES]
              [--no-constraints] [--unique-constraint UNIQUE_CONSTRAINT]
              [--no-create] [--create-if-not-exists] [--overwrite]
              [--db-schema DB_SCHEMA] [-y SNIFF_LIMIT] [-I]
              [--chunk-size CHUNK_SIZE]
              [FILE [FILE ...]]
```

Web: [csvsql - csvkit 2.0.0 documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html)
