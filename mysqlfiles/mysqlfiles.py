'''
Here are no join queries, I don't have any idea why I didn't use join
#TODO Convert all possible queries with join
#TODO tidy up and make a common procedure

1. ADDING POINTS FOR USER /POINT SYSTEM
2. CUSTOM COMMANDS ADD, DELETE, TETRIEVE
3. USER INFO
4. SERVER/BOT INFO
5. SERVER PERMISSIONS REMOVED
6. SHOP SYSTEM
7. EVENTS

######################################
1. ADDING POINTS FOR USER /POINT SYSTEM
'''

from config import MYSQL_DATABASE as sql_database
from config import MYSQL_PASSWORD as sql_password
from config import MYSQL_USERNAME as sql_username
from config import MYSQL_HOST as sql_host

from mysqlfiles.create_tables import check_for_all_tables
from pymysql import connect as pconnect


# Connection info and cursor
conn = pconnect(host=sql_host, user=sql_username, passwd=sql_password, db=sql_database, charset='utf8mb4',)
cur = conn.cursor()

# Checking if the tables are present
check_for_all_tables(conn, cur)

# Adding restart
cur.execute("UPDATE server_stats SET restarts = restarts+1;")
conn.commit()

def users_get_roll_stats(d_id):
    # Points here are tokens ;)
    cur.execute("""
            SELECT
                COUNT(CASE
                    WHEN `d_id` LIKE %s THEN 1 END)
                    AS `rows`,
                COUNT(CASE
                    WHEN `d_id` LIKE %s AND
                    `is_double` LIKE 1 THEN 1 END)
                    AS `doubles`,
                (SELECT
                    SUM(`victory_amount_memes`)
                    FROM `stats_roll`
                    WHERE `d_id`
                    LIKE %s)
                    AS `memes`,
                (SELECT
                    SUM(`victory_amount_points`)
                    FROM `stats_roll`
                    WHERE `d_id`
                    LIKE %s)
                    AS `tokens`
            FROM `stats_roll`;""", (d_id, d_id, d_id, d_id))

    sqlresult = cur.fetchone()
    return sqlresult

# Getting last messages
def message_last_interval_seconds(d_id):
    cur.execute("SELECT sender_d_id, sent FROM message_last_add_point WHERE last_Seen > date_sub(now(), interval 1 minute) and sender_d_id =%s;", (str(d_id),))
    sqlresult = cur.fetchone()
    return sqlresult

# Points add on message
def points_users_xp_add_on_message(points, user_d_id):
    cur.execute("UPDATE points_and_xp SET xp = xp +%s WHERE d_id =%s;", (points, str(user_d_id)))
    conn.commit()

# Memes add on message
def points_users_memes_add_on_message(points, user_d_id):
    cur.execute("UPDATE points_and_xp SET points = points +%s WHERE d_id =%s;", (points, str(user_d_id)))
    conn.commit()

# Get discord users xp and level
def get_xp_and_level_by_id(user_id):
    cur.execute("SELECT xp, level FROM points_and_xp WHERE d_id=%s;", (str(user_id),))
    sqlresult = cur.fetchone()
    return sqlresult

# gets users points
def users_get_points(user_id):
    cur.execute("SELECT points from points_and_xp where d_id = %s;", (user_id,))
    sqlresult = cur.fetchone()
    return sqlresult

# User add points on lose
def users_set_points_to_minus(points, d_id):
    cur.execute("UPDATE points_and_xp SET points = points-%s WHERE d_id =%s;", (points, d_id))
    conn.commit()

# User add points on win
def users_set_points_to_plus(points, d_id):
    cur.execute("UPDATE points_and_xp SET points = points+%s WHERE d_id =%s;", (points, d_id))
    conn.commit()

# gets users points
def users_get_bank_points(user_id):
    cur.execute("SELECT bank from points_and_xp where d_id = %s;", (user_id,))
    sqlresult = cur.fetchone()
    return sqlresult

# User add points on lose
def users_set_bank_to_minus(points, d_id):
    cur.execute("UPDATE points_and_xp SET bank = bank-%s WHERE d_id =%s;", (points, d_id))
    conn.commit()

# User add points on win
def users_set_bank_to_plus(points, d_id):
    cur.execute("UPDATE points_and_xp SET bank = bank+%s WHERE d_id =%s;", (points, d_id))
    conn.commit()

# Get tokens
def users_get_total_tokens(d_id):
    cur.execute("SELECT tokens FROM points_and_xp WHERE d_id =%s;", (str(d_id),))
    conn.commit()
    sqlresult = cur.fetchone()
    return sqlresult

# User remove tokens
def users_set_tokens_to_plus(points, d_id):
    cur.execute("UPDATE points_and_xp SET tokens = tokens+%s WHERE d_id =%s;", (points, d_id))
    conn.commit()

# User add tokens
def users_set_tokens_to_minus(points, d_id):
    cur.execute("UPDATE points_and_xp SET tokens = tokens+%s WHERE d_id =%s;", (points, d_id))
    conn.commit()

# get daily rows
def users_get_daily_redeems(d_id, time):
    cur.execute("SELECT * FROM points_daily_redeem WHERE d_id =%s AND name = 'daily' AND first_contact > DATE_SUB(NOW(), INTERVAL %s HOUR) ORDER BY first_contact DESC;", (str(d_id),int(time)))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

# get daily rows
def stats_roll_get_previous(d_id, time):
    cur.execute("SELECT d_id, number_1, number_2, is_double, victory_amount_memes, victory_amount_points, first_contact FROM stats_roll WHERE d_id =%s AND first_contact > DATE_SUB(NOW(), INTERVAL %s SECOND) ORDER BY first_contact DESC;", (str(d_id),int(time)))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

# get daily rows
def users_daily_redeem_by_day(d_id, day):
    cur.execute("SELECT d_id, day, amount, first_contact FROM daily_points WHERE d_id =%s AND day = %s ORDER BY first_contact DESC;", (str(d_id),int(day)))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

def users_daily_redeem_by_day_add(d_id, name, day, amount):
    cur.execute("INSERT INTO daily_points (d_id, name, day, amount) VALUES (%s, %s, %s, %s);", (d_id, name, day, amount))
    conn.commit()
    return

def stats_roll_add(d_id, number_1, number_2, is_double, victory_amount_memes, victory_amount_points):
    cur.execute("INSERT INTO stats_roll (d_id, number_1, number_2, is_double, victory_amount_memes, victory_amount_points) VALUES (%s, %s, %s, %s, %s, %s);", (d_id, number_1, number_2, is_double, victory_amount_memes, victory_amount_points))
    conn.commit()
    return

def tax_pot_history_add(server_id, d_id, tax):
    cur.execute("INSERT INTO tax_pot (server_id, d_id, number_1) VALUES (%s,%s,%s)", (server_id, d_id, tax))
    conn.commit()
    return

##### DAILY SYSTEM OPTION 2, RECEIVE IT EVERY 24H
# Add admin to admdin list with power
def points_daily_redeem(d_id, name, amount):
    cur.execute("INSERT INTO points_daily_redeem (d_id, name, amount) VALUES (%s, %s, %s);", (d_id, "daily", amount))
    conn.commit()
    return

# Points add on onlie, brb, dnd, etc
def user_add_points(points, d_id):
    cur.execute("UPDATE points_and_xp SET points = points+%s WHERE d_id =%s;", (points, d_id))
    conn.commit()
    return

# Points add on onlie, brb, dnd, etc
def user_add_points_in_bank(points, d_id):
    cur.execute("UPDATE points_and_xp SET bank = bank+%s WHERE d_id =%s;", (points, d_id))
    conn.commit()
    return

def points_stats_insert(server_id, d_id, mode_id, mode, stake1, stake2, outcome1, outcome2, info1, info2, info3, info4_hidden, info5_hidden, plus, minus):
    cur.execute("INSERT INTO point_history (server_id, d_id, mode_id, mode, stake1, stake2, outcome1, outcome2, info1, info2, info3, info4_hidden, info5_hidden, plus, minus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (str(server_id), str(d_id), int(mode_id), str(mode), str(stake1), str(stake2), str(outcome1), str(outcome2), str(info1), str(info2), str(info3), str(info4_hidden), int(info5_hidden), int(plus), int(minus)))
    conn.commit()
    return

def points_stats_get_win_high(limit):
    cur.execute("SELECT server_id, d_id, mode_id, mode, stake1, stake2, outcome1, outcome2, info1, info2, info3, info4_hidden, info5_hidden, first_contact FROM point_history ORDER BY plus DESC LIMIT %s;", (limit,))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

def points_stats_get_lost_high(limit):
    cur.execute("SELECT server_id, d_id, mode_id, mode, stake1, stake2, outcome1, outcome2, info1, info2, info3, info4_hidden, info5_hidden, first_contact FROM point_history ORDER BY minus DESC LIMIT %s;", (limit,))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

def points_stats_get_high(mode_id, value, limit):
    cur.execute("SELECT server_id, d_id, mode_id, mode, stake1, stake2, outcome1, outcome2, info1, info2, info3, info4_hidden, info5_hidden, first_contact FROM point_history WHERE mode_id = %s ORDER BY " + value + " DESC LIMIT %s;", (mode_id, limit))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

def points_stats_get_with_server():
    return

def points_stats_get_without_server(d_id, limit):
    cur.execute("SELECT server_id, mode_id, mode, stake1, stake2, outcome1, outcome2, info1, info2, info3, info4_hidden, first_contact FROM point_history WHERE d_id=%s ORDER BY first_contact DESC LIMIT %s;", (d_id, limit))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult


# In seconds
def get_users_lowest_bank_amount(mode, interval):
    cur.execute("SELECT d_id, MIN(info5_hidden) AS 'min' FROM point_history WHERE mode_id = %s AND first_contact > (DATE_SUB(CURDATE(), INTERVAL %s SECOND)) GROUP BY d_id;", (mode, interval))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

def get_users_lowest_bank_amount_by_id(mode, interval, d_id):
    cur.execute("SELECT MIN(info5_hidden) FROM point_history WHERE mode_id = %s AND first_contact > (DATE_SUB(CURDATE(), INTERVAL %s SECOND)) AND d_id = %s;", (mode, interval, d_id))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

def get_users_bank_amount(declined_users):

    command = "SELECT d_id, bank From points_and_xp WHERE bank != 0 AND d_id NOT IN ({});".format(", ".join(["%s" for _ in range(len(declined_users))]))

    cur.execute(command, declined_users)
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult


'''
######################################
2. CUSTOM RESPONSE COMMANDS ADD, DELETE, TETRIEVE
'''

# Command add
def command_add(server_id, command, response, info, added_by, times_used):
    command = command.lower()
    cur.execute("INSERT INTO commands (server_id, command, response, info, added_by, times_used) VALUES (%s, %s, %s, %s, %s, %s);", (server_id, command, response, info, added_by, times_used))
    conn.commit()
    return

# Command retrieve
def command_retrieve(command, server_id):
    command = command.lower()
    cur.execute("SELECT response FROM commands WHERE command=%s AND server_id = %s;", (command, server_id))
    conn.commit()
    sqlresult = cur.fetchone()
    return sqlresult

# Command remove
def command_remove(command, server_id):
    cur.execute("DELETE FROM commands WHERE command=%s AND server_id = %s;", (command, server_id))
    conn.commit()
    return

'''
######################################
3. USER INFO
'''

# User add points on win
def user_nicknames_get(server_id, d_id):
    cur.execute("SELECT name FROM member_nicknames WHERE server_id =%s AND d_id =%s;", (server_id, d_id))
    sqlresult = cur.fetchall()
    return sqlresult

'''
######################################
4. SERVER/BOT INFO
'''
# Server restarts
def server_stats_restarts():
    cur.execute("SELECT restarts FROM server_stats;")
    sqlresult = cur.fetchone()
    return str(sqlresult[0])

# On member join room
def on_member_join_room_id():
    cur.execute("SELECT on_member_join FROM server_stats;")
    sqlresult = cur.fetchone()
    return sqlresult

# On member join room
def on_member_remove_room_id():
    cur.execute("SELECT on_member_remove FROM server_stats;")
    sqlresult = cur.fetchone()
    return sqlresult

# server pot
def server_stats_tax_pot_get():
    cur.execute("SELECT tax_pot FROM server_stats;")
    sqlresult = cur.fetchone()
    return sqlresult

# server pot
def server_stats_tax_pot_add(tax_pot):
    cur.execute("UPDATE server_stats SET tax_pot = tax_pot+%s;", (tax_pot,))
    sqlresult = cur.fetchone()
    return
'''
######################################
6. Shop system
'''
def shop_get_items():
    cur.execute("SELECT item_name, item_id, item_price_memes_or, item_price_tokens_or, item_price_and, item_give_outcome, item_give_outcome_value FROM shop_items;")
    sqlresult = cur.fetchall()
    return sqlresult

def shop_insert_items(item_name, item_price_memes_or,item_price_tokens_or, item_price_and, item_give_outcome, item_give_outcome_value):
    cur.execute("INSERT INTO shop_items (item_name, item_price_memes_or,item_price_tokens_or, item_price_and, item_give_outcome, item_give_outcome_value) VALUES (%s,%s,%s,%s,%s,%s)",(item_name, item_price_memes_or,item_price_tokens_or, item_price__and, item_give_outcome, item_give_outcome_value))
    conn.commit()
    return

'''
######################################
7. Events
'''

def events_get_state_casino():
    cur.execute("SELECT event_casino, event_casino_channel_id FROM events;")
    conn.commit()
    sqlresult = cur.fetchone()
    return sqlresult

def events_change_state_casino(state_to):
    cur.execute("UPDATE events SET event_casino =%s;", (state_to,))
    conn.commit()
    return

def lotto_join_add_user(server_id, d_id, week_number):
    cur.execute("INSERT INTO lotto_join (server_id, d_id, week_number) VALUES (%s, %s, %s)", (server_id, d_id, week_number))
    conn.commit()
    return

def lotto_join_get_user_tickets(server_id, d_id, week_number):
    cur.execute("SELECT COUNT(*) FROM lotto_join WHERE server_id=%s AND d_id=%s AND week_number=%s;", (server_id, d_id, week_number))
    conn.commit()
    sqlresult = cur.fetchone()
    return sqlresult

def lotto_get_users_by_server_by_week(server_id, week_number):
    cur.execute("SELECT d_id FROM lotto_join WHERE server_id=%s AND week_number=%s", (server_id, week_number))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

###########################
# Basic query

# points add on offline
def query(query, info):
    cur.execute(query, info)
    conn.commit()
    return


########################################
# GET ALL COMMANDS

# Getting Wallpapers
def commands_get_all():
    cur.execute("SELECT command, response FROM `commands`;")
    sqlresult = cur.fetchall()
    return sqlresult
#######################################
# USER SETTINGS

# Command modify info
def profile_background(bg_number, d_id):
    cur.execute("SELECT image_name FROM bg_image_list WHERE border_number=%s;", (bg_number))
    bg_name = cur.fetchone()[0]
    cur.execute("UPDATE users SET bg_image=%s WHERE d_id=%s;", (bg_name, d_id))
    conn.commit()
    return

#######################################

# checks last offer from chrono gg
def chrono_gg_latest_game():
    cur.execute("SELECT chronogg FROM server_stats;")
    sqlresult = cur.fetchone()
    return str(sqlresult[0])

# Turn module on/off
def chrono_gg_update(game):
    cur.execute("UPDATE server_stats SET chronogg=%s;", (game,))
    conn.commit()
    return

#######################################
# USER INFO

# Add a meme
def server_stats_restarts():
    cur.execute("SELECT restarts FROM server_stats;")
    sqlresult = cur.fetchone()
    return str(sqlresult[0])

# Getting info about the user
def user_info_retrieve(d_id):
    cur.execute("SELECT d_id, name, points, bg_image, prof_border, info_info, info_country FROM users WHERE d_id=%s;", (d_id,))
    sqlresult = cur.fetchone()
    return sqlresult

# Adding last messages
def message_add(d_id, name, sent):
    cur.execute("INSERT INTO message_last_add_point (sender_d_id, name, sent) VALUES (%s, %s, %s);", (d_id, name, sent))
    conn.commit()
    return

######################################
# MEME COMMAND


# adding a nickname
def user_nicknames_add(server_id, d_id, name):
    cur.execute("INSERT INTO member_nicknames (server_id, d_id, name) VALUES (%s, %s, %s);", (server_id, d_id, name))
    conn.commit()


# adding status and game
def user_status_and_playing(server_id, d_id, name, game_from, game_to, streaming, status_from, status_to):
    cur.execute("INSERT INTO member_status_online (server_id, d_id, name, game_from, game_to, streaming, status_from, status_to) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (server_id, d_id, name, game_from, game_to, streaming, status_from, status_to))
    conn.commit()

# User add points on win
def user_nicknames_get(server_id, d_id):
    cur.execute("SELECT name FROM member_nicknames WHERE server_id =%s AND d_id =%s;", (server_id, d_id))
    sqlresult = cur.fetchall()
    return sqlresult

# getting a random meme from the database
def meme_get_random():
    cur.execute("SELECT link, meme_id FROM meme_list WHERE deleted != 1 ORDER BY RAND() LIMIT 1")
    sqlresult = cur.fetchone()
    return sqlresult


# Add a meme
def meme_insert_new(meme_id, adder_d_id, name, server_id, link):
    cur.execute("INSERT INTO meme_list (meme_id, adder_d_id, name, server_id, link, deleted) VALUES (%s, %s, %s, %s, %s, %s);", (meme_id, adder_d_id, name, server_id, link, "0"))
    conn.commit()
    return

# Add a meme
def meme_get_total_memes():
    cur.execute("SELECT COUNT(*) FROM meme_list;")
    sqlresult = cur.fetchone()
    return sqlresult

# Add a meme
def meme_get_meme_by_id(meme_id):
    cur.execute("SELECT link, meme_id FROM meme_list WHERE deleted != 1 AND meme_id =%s ORDER BY RAND() LIMIT 1", (meme_id))
    sqlresult = cur.fetchone()
    return sqlresult

######################################
# AUTOMATED STUFF FOR GETTING POINTS

# Add new user for points
def points_users_new_add(query, info):
    cur.execute(query, info)
    conn.commit()
    return

# points add on offline
def points_users_xp_add(query, info):
    cur.execute(query, info)
    conn.commit()
    return

# points add on offline
def points_users_points_add(query):
    cur.execute(query)
    conn.commit()
    return

# Points add on onlie, brb, dnd, etc
def users_get_points(user_id):
    cur.execute("SELECT points from points_and_xp where d_id = %s;", (user_id,))
    sqlresult = cur.fetchone()
    return sqlresult

# Points add on onlie, brb, dnd, etc
def users_get_xp(user_id):
    cur.execute("SELECT xp from points_and_xp where d_id = %s;", (user_id,))
    sqlresult = cur.fetchone()
    return sqlresult

# Points add on onlie, brb, dnd, etc
def users_get_daily_points(user_id):
    cur.execute("SELECT points, available_points FROM points_and_xp WHERE d_id =%s;", (user_id,))
    sqlresult = cur.fetchone()
    return sqlresult

# Points add on onlie, brb, dnd, etc
def users_set_daily_points(points, availeble_points, d_id):
    cur.execute("UPDATE points_and_xp SET points = points+%s, available_points =%s WHERE d_id =%s;", (points, availeble_points, d_id))
    conn.commit()
    return

# Points add on onlie, brb, dnd, etc
def get_xp_and_level_by_id(user_id):
    cur.execute("SELECT xp, level FROM points_and_xp WHERE d_id=%s;", (user_id,))
    sqlresult = cur.fetchone()
    return sqlresult

# User add points on win
def users_set_level_to(level, d_id):
    cur.execute("UPDATE points_and_xp SET level =%s WHERE d_id =%s;", (level, d_id))
    conn.commit()
    return

# User add points on lose
def users_set_points_to_minus(points, d_id):
    cur.execute("UPDATE points_and_xp SET points = points-%s WHERE d_id =%s;", (points, d_id))
    conn.commit()

# User add points on win
def users_set_points_to_plus(points, d_id):
    cur.execute("UPDATE points_and_xp SET points = points+%s WHERE d_id =%s;", (str(points), d_id))
    conn.commit()

# User add points on win
def users_get_top_points_with_bank(bot_id, limit):
    cur.execute("SELECT d_id, points, bank, (points+bank) AS total FROM points_and_xp WHERE NOT d_id =%s ORDER BY total DESC LIMIT %s;", (bot_id, int(limit)))
    sqlresult = cur.fetchall()
    return sqlresult


def users_get_points_and_bank(d_id):
    cur.execute("SELECT points, bank FROM points_and_xp WHERE d_id = %s", (d_id,))
    sqlresult = cur.fetchall()
    return sqlresult

# User add points on win
def users_get_top_points_by_wallet(bot_id, limit):
    cur.execute("SELECT d_id, points FROM points_and_xp WHERE NOT d_id =%s ORDER BY points DESC LIMIT %s;", (bot_id, limit))
    sqlresult = cur.fetchall()
    return sqlresult

# User add points on win
def users_get_top_points_by_bank(bot_id, limit):
    cur.execute("SELECT d_id, bank FROM points_and_xp WHERE NOT d_id =%s ORDER BY bank DESC LIMIT %s;", (bot_id, limit))
    sqlresult = cur.fetchall()
    return sqlresult

# User add points on win
def users_get_top_xp(bot_id, limit):
    cur.execute("SELECT d_id, xp FROM points_and_xp WHERE NOT d_id =%s ORDER BY xp DESC LIMIT %s;", (bot_id, int(limit)))
    sqlresult = cur.fetchall()
    return sqlresult
