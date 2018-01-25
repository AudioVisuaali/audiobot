from mysqlfiles.create_tables import check_for_all_tables
from config import MYSQL_DATABASE as sql_database
from config import MYSQL_PASSWORD as sql_password
from config import MYSQL_USERNAME as sql_username
from config import MYSQL_HOST as sql_host
from pymysql import connect as pconnect

# Connection info and cursor
conn = pconnect(host=sql_host, user=sql_username, passwd=sql_password, db=sql_database, charset='utf8mb4',)
cur = conn.cursor()

# Checking if the tables are present
check_for_all_tables(conn, cur)

# Adding restart
cur.execute("UPDATE server_stats SET restarts = restarts+1;")
conn.commit()

'''
Here are no join queries, I don't have any idea why I didn't use join
#TODO Convert all possible queries with join
#TODO tidy up and make a common procedure

1. ADDING POINTS FOR USER /POINT SYSTEM
2. CUSTOM COMMANDS ADD, DELETE, TETRIEVE
3. USER INFO
4. SERVER/BOT INFO
5. SERVER PERMISSIONS
6. SHOP SYSTEM
7. EVENTS

######################################
1. ADDING POINTS FOR USER /POINT SYSTEM
'''

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

# Get tokens
def users_get_gamble_history(d_id, amount):
    cur.execute("SELECT d_id, amount, outcome, multiplier, multiplier_value, all_in FROM points_history_roulette where d_id=%s ORDER BY last_seen DESC LIMIT %s;", (str(d_id),amount))
    conn.commit()
    sqlresult = cur.fetchall()
    return sqlresult

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

'''
######################################
2. CUSTOM RESPONSE COMMANDS ADD, DELETE, TETRIEVE
'''

# Command add
def command_add(command, response, info, added_by, times_used):
    command = command.lower()
    cur.execute("INSERT INTO commands (command, response, info, added_by, times_used) VALUES (%s, %s, %s, %s, %s);", (command, response, info, added_by, times_used))
    conn.commit()
    return

# Command retrieve
def command_retrieve(command):
    command = command.lower()
    cur.execute("SELECT response FROM commands WHERE command=%s;", (command,))
    conn.commit()
    sqlresult = cur.fetchone()
    return sqlresult


# Command remove
def command_remove(command):
    cur.execute("DELETE FROM commands WHERE command=%s;", (command,))
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
    return strsqlresult

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
5. Server permissions
'''
#Checking for admin id
def profile_id_get(id):
    cur.execute("SELECT d_id, power_lvl FROM admin_list WHERE d_id=%s;", (id,))
    sqlresult = cur.fetchone()
    return sqlresult

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

#execute("UPDATE points_and_xp SET points = points-%s WHERE d_id =%s;", (points, d_id))







###########################
# Basic query

# points add on offline
def query(query, info):
    try:
        cur.execute(query, info)
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")


############################
# ADMINLIST

# Add admin to admdin list with power
def profile_id_add(d_id, power_lvl):
    try:
        cur.execute("INSERT INTO admin_list (d_id, power_lvl) VALUES (%s, %s);", (d_id, power_lvl))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

# Add admin to admdin list with power
def profile_id_remove(d_id):
    try:
        cur.execute("DELETE FROM admin_list WHERE d_id=%s;", (d_id,))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

# Add admin to admdin list with power
def profile_id_power_update(d_id, power):
    try:
        cur.execute("UPDATE admin_list SET power_lvl=%s WHERE d_id=%s;", (power, d_id))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

##############################
# MODIFY COMMANDS

# Command modify info
def modify_command_info(info, command):
    try:
        cur.execute("UPDATE commands SET info=%s WHERE command=%s;", (info, command))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

# Command modify response
def modify_command_reponse(response, command):
    try:
        cur.execute("UPDATE commands SET response=%s WHERE command=%s;", (response, command))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

########################################
# Modify modules

# Turn module on/off
def modify_command_info(status, command):
    try:
        cur.execute("UPDATE modules SET status=%s WHERE command=%s;", (status, command))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

########################################
# GET WALLPAERS

# Getting Wallpapers
def wallpaper_retrieve():
    try:
        cur.execute("SELECT * FROM bg_image_list WHERE status='1' LIMIT 10;")
        sqlresult = cur.fetchone()
        for row in sqlresult:
            print(row)
        return sqlresult
    except TypeError:
        return None


########################################
# GET ALL COMMANDS

# Getting Wallpapers
def commands_get_all():
    try:
        cur.execute("SELECT command, response FROM `commands`;")
        sqlresult = cur.fetchall()
        return sqlresult
    except TypeError:
        return None
#######################################
# USER SETTINGS

# Command modify info
def profile_background(bg_number, d_id):
    try:
        cur.execute("SELECT image_name FROM bg_image_list WHERE border_number=%s;", (bg_number))
        bg_name = cur.fetchone()[0]
        cur.execute("UPDATE users SET bg_image=%s WHERE d_id=%s;", (bg_name, d_id))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

#######################################
# CHRONO GG

# checks last offer from chrono gg
def chrono_gg_latest_game():
    cur.execute("SELECT chronogg FROM server_stats;")
    sqlresult = cur.fetchone()
    return str(sqlresult[0])

# Turn module on/off
def chrono_gg_update(game):
    try:
        cur.execute("UPDATE server_stats SET chronogg=%s;", (game,))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")


#######################################
# USER INFO

# Add a meme
def server_stats_restarts():
    try:
        cur.execute("SELECT restarts FROM server_stats;")
        sqlresult = cur.fetchone()
        return str(sqlresult[0])
    except TypeError:
        return ("ERROR")


# Getting info about the user
def user_info_retrieve(d_id):
    try:
        cur.execute("SELECT d_id, name, points, bg_image, prof_border, info_info, info_country FROM users WHERE d_id=%s;", (d_id,))
        sqlresult = cur.fetchone()
        return sqlresult
    except TypeError:
        return None



# Adding last messages
def message_add(d_id, name, sent):
    try:
        cur.execute("INSERT INTO message_last_add_point (sender_d_id, name, sent) VALUES (%s, %s, %s);", (d_id, name, sent))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return None




######################################
# MEME COMMAND


# adding a nickname
def user_nicknames_add(server_id, d_id, name):
    try:
        cur.execute("INSERT INTO member_nicknames (server_id, d_id, name) VALUES (%s, %s, %s);", (server_id, d_id, name))
        conn.commit()
    except TypeError:
        return ("ERROR")

# adding status and game
def user_status_and_playing(server_id, d_id, name, game_from, game_to, streaming, status_from, status_to):
    try:
        cur.execute("INSERT INTO member_status_online (server_id, d_id, name, game_from, game_to, streaming, status_from, status_to) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (server_id, d_id, name, game_from, game_to, streaming, status_from, status_to))
        conn.commit()
    except TypeError:
        return ("ERROR")

# User add points on win
def user_nicknames_get(server_id, d_id):
    try:
        cur.execute("SELECT name FROM member_nicknames WHERE server_id =%s AND d_id =%s;", (server_id, d_id))
        sqlresult = cur.fetchall()
        return sqlresult
    except TypeError:
        return ("ERROR")

# getting a random meme from the database
def meme_get_random():
    try:
        cur.execute("SELECT link, meme_id FROM meme_list WHERE deleted != 1 ORDER BY RAND() LIMIT 1")
        sqlresult = cur.fetchone()
        return sqlresult
    except TypeError:
        return ("ERROR")


# Add a meme
def meme_insert_new(meme_id, adder_d_id, name, server_id, link):
    try:
        cur.execute("INSERT INTO meme_list (meme_id, adder_d_id, name, server_id, link, deleted) VALUES (%s, %s, %s, %s, %s, %s);", (meme_id, adder_d_id, name, server_id, link, "0"))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

# Add a meme
def meme_get_total_memes():
    try:
        cur.execute("SELECT COUNT(*) FROM meme_list;")
        sqlresult = cur.fetchone()
        return sqlresult
    except TypeError:
        return ("ERROR")

# Add a meme
def meme_get_meme_by_id(meme_id):
    try:
        cur.execute("SELECT link, meme_id FROM meme_list WHERE deleted != 1 AND meme_id =%s ORDER BY RAND() LIMIT 1", (meme_id))
        sqlresult = cur.fetchone()
        return sqlresult
    except TypeError:
        return ("ERROR")

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
    try:
        cur.execute("UPDATE points_and_xp SET points = points-%s WHERE d_id =%s;", (points, d_id))
        conn.commit()
    except TypeError:
        return ("ERROR")

# User add points on win
def users_set_points_to_plus(points, d_id):
    try:
        cur.execute("UPDATE points_and_xp SET points = points+%s WHERE d_id =%s;", (str(points), d_id))
        conn.commit()
    except TypeError:
        return ("ERROR")



# Trash
# Trash
# Trash
# Trash
# Trash
# Trash
# Trash
### ROULETTE TRASH TODO
# User add points on win
def users_get_top_points(bot_id):
    try:
        cur.execute("SELECT d_id, points FROM points_and_xp WHERE NOT d_id =%s ORDER BY points DESC LIMIT 10;", (bot_id,))
        sqlresult = cur.fetchall()
        return sqlresult
    except TypeError:
        return ("ERROR")

# User add points on win
def users_get_top_xp(bot_id):
    try:
        cur.execute("SELECT d_id, xp FROM points_and_xp WHERE NOT d_id =%s ORDER BY xp DESC LIMIT 10;", (bot_id,))
        sqlresult = cur.fetchall()
        return sqlresult
    except TypeError:
        return ("ERROR")

# Add admin to admdin list with power
def points_history_roulette_add(d_id, name, amount, outcome, all_in):
    try:
        cur.execute("INSERT INTO points_history_roulette (d_id, name, amount, outcome, all_in) VALUES (%s, %s, %s, %s, %s);", (d_id, name, amount, outcome, all_in))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")

# Add admin to admdin list with power
def points_history_roulette_add_with_multiplier(d_id, name, amount, outcome, all_in, multiplier):
    try:
        cur.execute("INSERT INTO points_history_roulette (d_id, name, amount, outcome, all_in, multiplier, multiplier_value) VALUES (%s, %s, %s, %s, %s, %s, %s);", (d_id, name, amount, outcome, all_in, 1, multiplier))
        conn.commit()
        return ("SUCCESS")
    except TypeError:
        return ("ERROR")
