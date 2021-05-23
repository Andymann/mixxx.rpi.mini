import sqlite3


con = sqlite3.connect('/home/pi/.mixxx/mixxxdb.sqlite')
cur = con.cursor()

res = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    print(name[0])

# track_locations is the most interesting one
loc_OLDLOC = "/Users/andyfischer/Music/"
loc_NEWLOC = "/home/pi/Music"
cur.execute("SELECT id, location, directory FROM track_locations")
rows = cur.fetchall()
for row in rows:
    print(row)
    sID = row[0]
    sLOC = row[1]
    sDIR = row[2]
    if str(sLOC).startswith(loc_OLDLOC):
        # den vorderen Teil abschneiden:
        sLOC = sLOC[len(loc_OLDLOC):]

        sLOC = loc_NEWLOC + "/" + sLOC
        cur2 = con.cursor()
        sql_update_query = """Update track_locations set location = ?, directory = ? where id = ?"""
        data = (sLOC, loc_NEWLOC, sID)
        cur2.execute(sql_update_query, data)
        con.commit()
        print("Record Updated successfully")
        cur2.close()
    # print(sLOC)
    # cur.close()
