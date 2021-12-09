import nextcord
import sqlite3

global playerarray
playerarray = []

client = nextcord.Client()
con = sqlite3.connect('reportdb.db')
cur = con.cursor()

class cdata():
  def __init__(self, dcid, reportuser, reportreason):
    self.dcid = dcid
    self.reportuser = reportuser
    self.reportreason = reportreason


class cuser():
  def __init__(self, dcid, mode, step, data):
    self.dcid = dcid
    self.step = step
    self.data = data
    self.mode = mode
  


def start_session(dcid, mode, step, data):
    user = cuser(dcid, mode, step, data)
    playerarray.append(user)
    print(f'Args = {dcid, mode, step, data}')
    print(f'playerarray = {playerarray}')
    print(f'user dcid =', user.dcid)
    print(playerarray[0].dcid)

def getsessiondata(dcid):
    print(f"in-context player array = {playerarray}")
    for i,k in enumerate(playerarray):
        if str(k.dcid) == str(dcid): #k[0] should be the dcid (discord id)
            return k
    return False

def end_session(dcid):
    for i,k in enumerate(playerarray):
      if str(k.dcid) == str(dcid): #k[0] should be the dcid (discord id)
        del playerarray[i]
      return
      

def create_database():
    cur.execute('''CREATE TABLE users
                (minecraftname text, discordid text, reporterid text, reportreason text, proof text)''')

def add_user(minecraftname, discordid, reporterid, reportreason, proof):
    cur.execute(f"INSERT INTO users VALUES ('{minecraftname}','{discordid}','{reporterid}','{reportreason}','{proof}')")
    con.commit()
    con.close()   

