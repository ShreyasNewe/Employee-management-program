create table employeee(
id serial primary key,
fname varchar(50)not null,                      ------------ makes the table with the following columns(fname,lname,title,dept,salary,doj)
lname varchar(50)not null,
title varchar(50)not null,
dept varchar(50)not null,
salary int not null default 30000,
DOJ date not null default current_date
);
--------------------------------------------------
select * from employeee   ----- shows you the output table
--------------------------------------------------
delete from employeee
where id=0

---------------------------------------------------
DO $$ DECLARE
    tabname RECORD;
BEGIN
    FOR tabname IN
        SELECT tablename FROM pg_tables
        WHERE schemaname = 'public'
    LOOP
        EXECUTE 'TRUNCATE TABLE ' || quote_ident(tabname.tablename) || ' RESTART IDENTITY CASCADE';
    END LOOP;
END $$;
--   This block truncates all tables in the public schema, resetting their identity columns and cascading the truncation to any dependent tables.
