
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection coniguration
db_config = {
    'user': 'root',
    'password': '1234#SQL',
    'host': 'localhost',
    'database': 'DB1'
}

# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Matches routes
@app.route('/matches')
def matches():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MATCHES")
    matches = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('matches.html', matches=matches)

@app.route('/update_match/<match_id>', methods=['GET', 'POST'])
def update_match(match_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        match_date = request.form['match_date']
        match_time = request.form['match_time']
        team_1_name = request.form['team_1_name']
        team_2_name = request.form['team_2_name']
        loser = request.form['loser']
        winner = request.form['winner']
        stadium = request.form['stadium']
        umpire_id = request.form['umpire_id']
        
        cursor.execute("""
            UPDATE MATCHES
            SET match_date=%s, match_time=%s, team_1_name=%s, team_2_name=%s, loser=%s, winner=%s, stadium=%s, umpire_id=%s
            WHERE match_id=%s
        """, (match_date, match_time, team_1_name, team_2_name, loser, winner, stadium, umpire_id, match_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('matches'))
    
    cursor.execute("SELECT * FROM MATCHES WHERE match_id = %s", (match_id,))
    match = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_match.html', match=match)

@app.route('/delete_match/<match_id>')
def delete_match(match_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MATCHES WHERE match_id = %s", (match_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('matches'))

# Players routes
@app.route('/players')
def players():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PLAYER")
    players = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('players.html', players=players)

@app.route('/update_player/<player_id>', methods=['GET', 'POST'])
def update_player(player_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        team_id = request.form['team_id']
        no_of_worldcups = request.form['no_of_worldcups']
        number_of_matches = request.form['number_of_matches']
        batting_average = request.form['batting_average']
        no_of_sixes = request.form['no_of_sixes']
        no_of_fours = request.form['no_of_fours']
        no_of_totalruns = request.form['no_of_totalruns']
        no_of_t20 = request.form['no_of_t20']
        no_of_odi = request.form['no_of_odi']
        no_of_test = request.form['no_of_test']
        no_of_wickets = request.form['no_of_wickets']
        type_of_bowler = request.form['type_of_bowler']
        economy = request.form['economy']
        
        cursor.execute("""
            UPDATE PLAYER
            SET team_id=%s, no_of_worldcups=%s, number_of_matches=%s, batting_average=%s, no_of_sixes=%s, no_of_fours=%s, no_of_totalruns=%s, no_of_t20=%s, no_of_odi=%s, no_of_test=%s, no_of_wickets=%s, type_of_bowler=%s, economy=%s
            WHERE player_id=%s
        """, (team_id, no_of_worldcups, number_of_matches, batting_average, no_of_sixes, no_of_fours, no_of_totalruns, no_of_t20, no_of_odi, no_of_test, no_of_wickets, type_of_bowler, economy, player_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('players'))
    
    cursor.execute("SELECT * FROM PLAYER WHERE player_id = %s", (player_id,))
    player = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_player.html', player=player)

@app.route('/delete_player/<player_id>')
def delete_player(player_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PLAYER WHERE player_id = %s", (player_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('players'))

# Teams routes
@app.route('/teams')
def teams():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM TEAM")
    teams = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('teams.html', teams=teams)

@app.route('/update_team/<team_id>', methods=['GET', 'POST'])
def update_team(team_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        team_rank = request.form['team_rank']
        team_name = request.form['team_name']
        country_name = request.form['country_name']
        no_of_wins = request.form['no_of_wins']
        no_of_loses = request.form['no_of_loses']
        no_of_draws = request.form['no_of_draws']
        no_of_bowlers = request.form['no_of_bowlers']
        no_of_batsmans = request.form['no_of_batsmans']
        
        cursor.execute("""
            UPDATE TEAM
            SET team_rank=%s, team_name=%s, country_name=%s, no_of_wins=%s, no_of_loses=%s, no_of_draws=%s, no_of_bowlers=%s, no_of_batsmans=%s
            WHERE team_id=%s
        """, (team_rank, team_name, country_name, no_of_wins, no_of_loses, no_of_draws, no_of_bowlers, no_of_batsmans, team_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('teams'))
    
    cursor.execute("SELECT * FROM TEAM WHERE team_id = %s", (team_id,))
    team = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_team.html', team=team)

@app.route('/delete_team/<team_id>')
def delete_team(team_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TEAM WHERE team_id = %s", (team_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('teams'))

# Umpires routes
@app.route('/umpires')
def umpires():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM UMPIRE")
    umpires = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('umpires.html', umpires=umpires)

@app.route('/update_umpire/<umpire_id>', methods=['GET', 'POST'])
def update_umpire(umpire_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        umpire_name = request.form['umpire_name']
        no_of_matches = request.form['no_of_matches']
        country = request.form['country']
        
        cursor.execute("""
            UPDATE UMPIRE
            SET umpire_name=%s, no_of_matches=%s, country=%s
            WHERE umpire_id=%s
        """, (umpire_name, no_of_matches, country, umpire_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('umpires'))
    
    cursor.execute("SELECT * FROM UMPIRE WHERE umpire_id = %s", (umpire_id,))
    umpire = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_umpire.html', umpire=umpire)

@app.route('/delete_umpire/<umpire_id>')
def delete_umpire(umpire_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM UMPIRE WHERE umpire_id = %s", (umpire_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('umpires'))

if __name__ == '__main__':
    app.run(debug=True)
