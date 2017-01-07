# tournament.py -- implementation of a Swiss-system tournament

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE from matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE from players")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT COUNT(*) FROM players")
    db.commit()
    results = cur.fetchone()[0]
    db.close()
    return results


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    name_val = str(name)
    db = connect()
    cur = db.cursor()
    data = (name_val, )
    SQL = "INSERT INTO players (name) VALUES (%s);" 
    cur.execute(SQL, data)
    db.commit()
    db.close()




def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cur = db.cursor()
    SQL = """SELECT * FROM v_player_standings"""
    cur.execute(SQL)
    results = cur.fetchall()
    db.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cur = db.cursor()
    cur.execute("""INSERT INTO matches 
                (winner, loser) VALUES (%s, %s)""", 
                (winner, loser,))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    results = []

    # Zips every other element starting with the first element
    # and the second from standings array
    for player1, player2 in zip(standings[0::2], standings[1::2]):
        results.append((player1[0], player1[1], player2[0], player2[1]))
        
    return results


