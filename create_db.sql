create table if not exists labels(
    id integer primary key,
    name varchar(255) unique
);

create table if not exists notes(
    id integer primary key,
    name varchar(255) unique,
    content text,
    date timestamp default current_timestamp
);

create table if not exists relation(
    id integer primary key,
    label_id integer,
    note_id integer,
    unique(label_id, note_id),
    foreign key(label_id) references labels(id) on delete cascade,
    foreign key(note_id) references notes(id) on delete cascade
);
