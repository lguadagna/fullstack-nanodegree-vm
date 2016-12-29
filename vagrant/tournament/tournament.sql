-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

-- use these to drop individual tables, above drops all 
-- DROP TABLE IF EXISTS player;
-- DROP TABLE IF EXISTS match;
-- DROP TABLE IF EXISTS playerStandings;

CREATE DATABASE tournament;
\c tournament;


CREATE TABLE player (
  id serial PRIMARY KEY, 
  playername varchar(50) UNIQUE NOT NULL,
  dateCreated timestamp DEFAULT current_timestamp
);

-- references table(value) is how to reference a foreign key
CREATE TABLE match (
  winner integer references player(id),
  loser integer references player(id) 
);

-- this is how to set the search path to default values
SET search_path TO showfinder,public;

