import mariadb


def migration_name():
    return "Update godwinds mods (switch Genbu and Seiryu)"


def check_preconditions(cur):
    return


def needs_to_run(cur):
    # Check if the key already exists
    cur.execute(
        "SELECT * FROM item_mods WHERE itemId = 18164 AND modId = 1178 AND value = 278;"
    )
    if cur.fetchone():
        return True
    return False


def migrate(cur, db):
    try:
        cur.execute("UPDATE item_mods SET value = 278 WHERE itemId = 18163 AND modId = 1178;")
        cur.execute("UPDATE item_mods SET value = 277 WHERE itemId = 18164 AND modId = 1178;")
        db.commit()
    except mariadb.Error as err:
        print("Something went wrong: {}".format(err))
