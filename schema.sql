drop table if exist peeps;
create table peeps (
  id integer primary key autoincrement,
  user_id INT,
  peep VARCHAR(333)
);
