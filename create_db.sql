create table if not exists snotebooks(
    id integer primary key,
    name varchar(255)
);

create table if not exists notes(
    id integer primary key,
    name varchar(255),
    content text,
    date datetime
);

create table if not exists labels(
    id integer primary key,
    notebook_id integer,
    note_id integer,
    foreign key(notebook_id) references notebooks(id),
    foreign key(note_id) references notes(id)
);
