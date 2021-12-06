def start_session(dcid, mode, step, data):
    playerarray.append([dcid, mode, step, data])
    print(f'Args = {dcid, mode, step, data}')

    print(f'playerarray = {playerarray}')


def find_session_data(dcid):
    print(f"in-context player array = {playerarray}")
    for i,k in enumerate(playerarray):
        if str(k[0]) == str(dcid): #k[0] should be the dcid (discord id)
            return k
    return false


def create_database():
    cur.execute('''CREATE TABLE users
                (minecraftname text, discordid text, reporterid text, reportreason text, proof text)''')

def add_user(minecraftname, discordid, reporterid, reportreason, proof):
    cur.execute(f"INSERT INTO users VALUES ('{minecraftname}','{discordid}','{reporterid}','{reportreason}','{proof}')")
    con.commit()
    con.close()   
