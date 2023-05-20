from datetime import datetime
import mysql.connector

def create_connection(config):
    return mysql.connector.connect(pool_name = "pool", pool_size = 6, **config)

def get_connection():
    return mysql.connector.connect(pool_name = "pool")

# RESTapi GET Calls
def get_endpoints(cur):
    cur.execute("SELECT * FROM `id`")
    results = cur.fetchall()
    parsed_results = []
    for result in results:
        parsed_result = {
            'mac': result[0],
            'time': result[1],
            'last_online': result[2]
        }
        parsed_results.append(parsed_result)
    return parsed_results

def get_endpoint(mac, cur):
    cur.execute("SELECT * FROM `id` WHERE `mac` = %s", (mac,))
    result = cur.fetchall()
    if(len(result) == 1):
        parse_result = {
            'mac': result[0][0],
            'time': result[0][1],
            'last_online': result[0][2]
        }
        return parse_result
    else:
        return None

def get_endpoint_firmware(mac, cur):
    cur.execute("SELECT * FROM `firmware` WHERE `mac` = %s", (mac,))
    result = cur.fetchall()
    if(len(result) == 1):
        parse_result = {
            'mac': result[0][0],
            'firmware': result[0][1]
        }
        return parse_result
    else:
        return None

def get_data(start, end, cur):
    cur.execute("SELECT * FROM `data` WHERE `time` BETWEEN %s and %s", (start, end))
    results = cur.fetchall()
    parsed_results = []
    for result in results:
        parsed_result = {
            'mac': result[0],
            'temp': result[1],
            'humidity': result[2],
            'time': result[3]
        }
        parsed_results.append(parsed_result)
    return parsed_results

def get_location(mac, cur):
    cur.execute("SELECT * FROM `location` WHERE `mac` = %s", (mac,))
    result = cur.fetchall()
    if(len(result) == 1):
        parse_result = {
            'mac': result[0][0],
            'location': result[0][1]
        }
        return parse_result
    else:
        return None

# RESTapi POST Calls
def create_endpoint(mac, cnx, cur):    
    date = datetime.now()
    q = "INSERT INTO `id` (`mac`, `time`, `last_online`) VALUES (%s, %s, %s)"
    cur.execute(q, (mac, date, date))
    cnx.commit()

    q = "SELECT * FROM `id` WHERE `mac` = %s"
    cur.execute(q, (mac,))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'time': result[1],
        'last_online': result[2]
    }
    return parse

def create_endpoint_firmware(mac, firmware, cnx, cur):
    q = "INSERT INTO `firmware` (`mac`, `firmware`) VALUES (%s, %s)"
    cur.execute(q, (mac, firmware))
    cnx.commit()

    q = "SELECT * FROM `firmware` WHERE `mac` = %s"
    cur.execute(q, (mac,))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'firmware': result[1]
    }
    return parse

def create_data(mac, temp, hum, cnx, cur):
    date = datetime.now()
    q = "INSERT INTO `data` (`mac`, `temp`, `humidity`, `time`) VALUES (%s, %s, %s, %s)"
    cur.execute(q ,(mac, temp, hum, date.strftime("%Y-%m-%d %H:%M:%S")))
    cnx.commit()

    q = "SELECT * FROM `data` WHERE (`mac` = %s AND `time` = %s)"
    cur.execute(q, (mac, date.strftime("%Y-%m-%d %H:%M:%S")))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'temp': result[1],
        'humidity': result[2],
        'time': result[3]
    }
    return parse

def create_location(mac, location, cnx, cur):
    q = "INSERT INTO `location` (`mac`, `location`) VALUES (%s, %s)"
    cur.execute(q, (mac, location))
    cnx. commit()

    q = "SELECT * FROM `location` WHERE (`mac` = %s AND `location` = %s)"
    cur.execute(q, (mac, location))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'location': result[1]
    }
    return parse

# RESTapi PATCH Calls
def update_endpoint(mac, cnx, cur):
    date = datetime.now()
    q = "UPDATE `id` SET `last_online` = %s WHERE `mac` = %s"
    cur.execute(q, (date, mac))
    cnx.commit()

    q = "SELECT * FROM `id` WHERE `mac` = %s"
    cur.execute(q, (mac, ))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'time': result[1],
        'last_online': result[2]
    }
    return parse

def update_endpoint_firmware(mac, firmware, cnx, cur):
    q = "UPDATE `firmware` SET `firmware` = %s WHERE `mac` = %s"
    cur.execute(q, (firmware, mac))
    cnx.commit()

    q = "SELECT * FROM `firmware` WHERE `mac` = %s"
    cur.execute(q, (mac,))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'firmware': result[1]
    }
    return parse

def update_location(mac, location, cnx, cur):
    q = "UPDATE `location` SET `location`= %s WHERE `mac` = %s"
    cur.execute(q, (location, mac))
    cnx. commit()

    q = "SELECT * FROM `location` WHERE (`mac` = %s AND `location` = %s)"
    cur.execute(q, (mac, location))
    result = cur.fetchone()
    parse = {
        'mac': result[0],
        'location': result[1]
    }
    return parse
