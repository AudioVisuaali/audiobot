#THIS IS NOT USABLE
#THIS IS JUST A SCRATCH TABLE
#THIS PROCESS IS AUTOMATED (ADDING TABLES)

CREATE TABLE IF NOT EXISTS users (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id varchar(18) NOT NULL,
  name varchar(64) NOT NULL,
  namesecret int NOT NULL,
  power int NOT NULL,
  points int NOT NULL,
  online boolean NOT NULL,
  messages_total INT NOT NULL,
  bg_image varchar(64) NOT NULL,
  prof_border varchar(64) NOT NULL,
  info_info varchar(256) NOT NULL,
  info_owrank varchar(7) NOT NULL,
  info_country varchar(3) NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS points_and_xp (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id varchar(18) NOT NULL UNIQUE,
  name varchar(64) NOT NULL,
  points varchar(64) NOT NULL DEFAULT '0',
  xp varchar(64) NOT NULL DEFAULT '0',
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS points_history_roulette (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id varchar(18) NOT NULL,
  name varchar(64) NOT NULL,
  amount varchar(64) NOT NULL,
  outcome varchar(4) NOT NULL,
  all_in varchar(1) NOT NULL,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS points_daily_redeem (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id varchar(18) NOT NULL,
  name varchar(64) NOT NULL,
  amount varchar(64) NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS logging_messages (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id varchar(18) NOT NULL,
  name varchar(64) NOT NULL,
  server_id varchar(18) NOT NULL,
  message varchar(2000) NULL,
  image varchar(200) NULL,
  deleted int(1) NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

@AudioVisuaali no clean way. Have to parse both message attachments and message embeds

CREATE TABLE IF NOT EXISTS meme_list (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  meme_id INT NOT NULL,
  adder_d_id varchar(18) NOT NULL,
  name varchar(64) NOT NULL,
  server_id varchar(18) NOT NULL,
  link varchar(2000) NULL,
  deleted int(1) NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS message_last_add_point (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  sender_d_id varchar(18) NOT NULL,
  name varchar(64) NOT NULL,
  sent varchar(20) NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS server_stats (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  restarts INT NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS shop_items (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  item_name VARCHAR(128) NOT NULL,
  item_id INT NOT NULL,
  item_price_memes_or INT NULL,
  item_price_tokens_or INT NULL,
  item_price_memes_and INT NULL,
  item_price_tokens_and INT NULL,
  item_give_outcome INT NOT NULL,
  item_give_outcome_value VARCHAR(256) NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS shop_items_bought_users (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id INT(18) NOT NULL,
  server_d_id INT(18) NOT NULL,
  item_id INT NOT NULL,
  item_bought TINYINT(1) NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS permissions (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  admin_add_command VARCHAR(18) NULL,
  admin_remove_command VARCHAR(18) NULL,
  admin_meme_add VARCHAR(18) NULL,
  admin_toggle_event_casino VARCHAR(18) NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS events (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  event_casino TINYINT(1) NOT NULL DEFAULT 0,
  event_casino_channel_id VARCHAR(18) NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS stats_roll (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id VARCHAR(18) NOT NULL,
  number_1 VARCHAR(1) NULL,
  number_2 VARCHAR(2) NULL,
  is_double TINYINT(1) NOT NULL,
  victory_amount_memes INT NOT NULL,
  victory_amount_points INT NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS stats_roll (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  server_id VARCHAR(18) NOT NULL,
  d_id VARCHAR(18) NOT NULL,
  number_1 INT NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS lotto_join(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  server_id VARCHAR(18) NOT NULL,
  d_id VARCHAR(18) NOT NULL,
  number_1 INT NOT NULL,
  first_contact datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;






CREATE TABLE IF NOT EXISTS member_names (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id varchar(18) NOT NULL,
  name varchar(64) NOT NULL,
  amount varchar(64) NOT NULL,
  outcome varchar(4) NOT NULL,
  all_in varchar(1) NOT NULL,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS bg_image_list (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  border_number int NOT NULL,
  image_desc varchar(256) NOT NULL,
  image_name varchar(64) NOT NULL,
  last_updated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS admin_list (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  d_id varchar(18) NOT NULL,
  power_lvl varchar(18) Not NULL,
  last_updated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS modules (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  command varchar(64) NOT NULL,
  status int NOT NULL,
  add_date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_update datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS commands (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  command varchar(64) NOT NULL,
  response varchar(256) NOT NULL,
  info varchar(256) NOT NULL,
  added_by varchar(18) NOT NULL,
  times_used varchar(64) NOT NULL,
  last_updated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#### //NOT USED CURRENTLY
CREATE TABLE IF NOT EXISTS duel_results (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  challenger varchar(18) NOT NULL,
  challenged varchar(18) Not NULL,
  amount int NOT NULL,
  result int NOT NULL,
  done boolean NOT NULL,
  deny boolean NOT NULL,
  last_updated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS roulette_results (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user varchar(18) NOT NULL,
  amount int NOT NULL,
  result int NOT NULL,
  last_updated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS coin_results (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user varchar(18) NOT NULL,
  amount int NOT NULL,
  result int NOT NULL,
  last_updated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS timer (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  repsonse varchar(256) Not NULL,
  timeonline int NOT NULL,
  timeofline int NOT NULL,
  added_by varchar(18) NOT NULL,
  last_update datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  crated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

  CREATE TABLE IF NOT EXISTS points_given (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user varchar(18) Not NULL,
    receiver varchar(18) int NOT NULL,
    crated datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
  ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
