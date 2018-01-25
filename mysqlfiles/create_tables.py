
def create_tables_for_database(conn, cur):

    tables_list = [{
        'sql': """CREATE TABLE IF NOT EXISTS `admin_list` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `d_id` varchar(18) NOT NULL,
          `power_lvl` varchar(18) NOT NULL,
          `last_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `commands` (
          `id` int(11) NOT NULL,
          `command` varchar(64) NOT NULL,
          `response` varchar(2000) NOT NULL,
          `info` varchar(256) NOT NULL,
          `added_by` varchar(18) NOT NULL,
          `times_used` varchar(64) NOT NULL,
          `last_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `events` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `event_casino` tinyint(1) NOT NULL DEFAULT '0',
          `event_casino_channel_id` varchar(18) DEFAULT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `logging_messages` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `d_id` varchar(18) COLLATE utf8mb4_unicode_ci NOT NULL,
          `name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
          `server_id` varchar(18) COLLATE utf8mb4_unicode_ci NOT NULL,
          `room_id` varchar(18) COLLATE utf8mb4_unicode_ci NOT NULL,
          `message_id` varchar(18) COLLATE utf8mb4_unicode_ci NOT NULL,
          `message` varchar(2000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
          `image` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
          `private` int(1) NOT NULL,
          `deleted` int(1) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `lotto_join` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `server_id` varchar(18) NOT NULL,
          `d_id` varchar(18) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `member_nicknames` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `server_id` varchar(18) NOT NULL,
          `d_id` varchar(18) NOT NULL,
          `name` varchar(64) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `member_status_online` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `server_id` varchar(18) NOT NULL,
          `d_id` varchar(18) NOT NULL,
          `name` varchar(64) NOT NULL,
          `game_from` varchar(64) NOT NULL,
          `game_to` varchar(64) NOT NULL,
          `streaming` tinyint(1) NOT NULL,
          `status_from` varchar(64) NOT NULL,
          `status_to` varchar(64) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `meme_list` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `meme_id` int(11) NOT NULL,
          `adder_d_id` varchar(18) NOT NULL,
          `name` varchar(64) NOT NULL,
          `server_id` varchar(18) NOT NULL,
          `link` varchar(2000) DEFAULT NULL,
          `deleted` int(1) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `message_last_add_point` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `sender_d_id` varchar(18) NOT NULL,
          `name` varchar(64) NOT NULL,
          `sent` varchar(20) DEFAULT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `modules` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `command` varchar(64) NOT NULL,
          `status` int(11) NOT NULL,
          `add_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_update` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `permissions` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `admin_add_command` varchar(18) DEFAULT NULL,
          `admin_remove_command` varchar(18) DEFAULT NULL,
          `admin_meme_add` varchar(18) DEFAULT NULL,
          `admin_toggle_event_casino` varchar(18) DEFAULT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `points_and_xp` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `d_id` varchar(18) NOT NULL,
          `name` varchar(64) NOT NULL,
          `points` int(11) NOT NULL DEFAULT '0',
          `available_points` int(11) NOT NULL DEFAULT '0',
          `xp` int(11) NOT NULL DEFAULT '0',
          `level` int(11) NOT NULL DEFAULT '0',
          `tokens` int(11) NOT NULL DEFAULT '0',
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `points_daily_redeem` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `d_id` varchar(18) NOT NULL,
          `name` varchar(64) NOT NULL,
          `amount` varchar(64) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `points_history_roulette` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `d_id` varchar(18) NOT NULL,
          `name` varchar(64) NOT NULL,
          `amount` varchar(64) NOT NULL,
          `outcome` varchar(4) NOT NULL,
          `multiplier` tinyint(1) DEFAULT '0',
          `multiplier_value` float DEFAULT NULL,
          `all_in` tinyint(1) NOT NULL,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `server_stats` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `server_id` varchar(18) NOT NULL UNIQUE,
          `restarts` int(11) NOT NULL DEFAULT '0',
          `chronogg` varchar(200) NOT NULL,
          `on_member_join` varchar(18) DEFAULT NULL,
          `on_member_remove` varchar(18) DEFAULT NULL,
          `tax_pot` int(11) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `shop_items` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `item_name` varchar(128) NOT NULL,
          `item_id` int(11) NOT NULL,
          `item_price_memes_or` int(11) DEFAULT '0',
          `item_price_tokens_or` int(11) DEFAULT '0',
          `item_price_and` tinyint(1) NOT NULL DEFAULT '0',
          `item_give_outcome` int(11) NOT NULL,
          `item_give_outcome_value` varchar(256) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `shop_items_bought_users` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `d_id` int(18) NOT NULL,
          `server_d_id` int(18) NOT NULL,
          `item_id` int(11) NOT NULL,
          `item_bought` tinyint(1) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `stats_roll` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `d_id` varchar(18) NOT NULL,
          `number_1` varchar(1) DEFAULT NULL,
          `number_2` varchar(2) DEFAULT NULL,
          `is_double` tinyint(1) NOT NULL,
          `victory_amount_memes` int(11) NOT NULL,
          `victory_amount_points` int(11) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
          `last_seen` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    },
    {
        'sql': """CREATE TABLE IF NOT EXISTS `tax_pot` (
          `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          `server_id` varchar(18) NOT NULL,
          `d_id` varchar(18) NOT NULL,
          `number_1` int(11) NOT NULL,
          `first_contact` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    }]

    # Run each table query
    for pod in tables_list:

        # If any errors stop
        try:
            cur.execute(pod['sql'])
        except Exception as e:
            exit(e)

# Checks all the tables
def check_for_all_tables(conn, cur):

    table_list = ['admin_list', 'commands', 'events', 'logging_messages', 'lotto_join', 'member_nicknames', 'member_status_online', 'meme_list', 'message_last_add_point', 'modules', 'permissions', 'points_and_xp', 'points_daily_redeem', 'points_history_roulette', 'server_stats', 'shop_items', 'shop_items_bought_users', 'stats_roll', 'tax_pot']
    tables_in_database = []
    not_all_tables = False

    cur.execute("SHOW TABLES;")
    all_tables_in_database = cur.fetchall()

    # Adding to list for compare
    for item in all_tables_in_database:
        tables_in_database.append(item[0])

    # Chcking tables
    if len(tables_in_database) == len(table_list):
        for item in all_tables_in_database:
            if item[0] not in table_list:
                not_all_tables = True

    # Adding tables if not in database
    if not_all_tables:
        #do set tables up TODO
        create_tables_for_database(conn, cur)
        pass
