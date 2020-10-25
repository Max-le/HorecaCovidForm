DROP TABLE IF EXISTS visitors;
DROP TABLE IF EXISTS resto_admin;

CREATE TABLE visitors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT,
  last_name TEXT,
  tel_number TEXT, 
  email TEXT, 
  date_visit TEXT, 
  hour_visit TEXT
);


CREATE TABLE resto_admin (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  admin_name TEXT,
  password_hash TEXT
);