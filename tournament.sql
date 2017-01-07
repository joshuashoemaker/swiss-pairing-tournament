-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.

DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players(
    id serial PRIMARY KEY,
    name text
);

CREATE TABLE matches(
    match_id serial,
    loser integer,
    winner integer,
    PRIMARY KEY (match_id),
    FOREIGN KEY (loser) REFERENCES players (id),
    FOREIGN KEY (winner) REFERENCES players (id)
);

CREATE VIEW v_matches_played AS
  SELECT players.id, COUNT(players.id) AS played
    FROM players, matches
    WHERE players.id = matches.loser OR players.id = matches.winner
    GROUP BY players.id 
    ORDER BY played DESC;

CREATE VIEW v_number_of_wins AS
  SELECT players.id, COUNT(matches.winner) AS wins
  FROM matches, players
  WHERE players.id = matches.winner
  GROUP BY players.id
  ORDER BY wins DESC;