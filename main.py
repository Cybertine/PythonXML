import xml.etree.ElementTree as ET
import os.path

tree = ET.parse('data.xml')
root = tree.getroot()

def getData(item):
    return root.find(item).text

def setData(item, value):
    root.find(item).text = str(value)
    tree.write('data.xml')

def template(file, vars):
    return open(file, 'r').read() % vars

def makeUser(username, userid):
    return template('user.tpl', {
        'username': username,
        'userid': userid
    })

def newSystem(username, userid, sysname):
    if os.path.isfile(f'./systems/{username}.xml') == False:
        sysid = int(getData("systemid"))
        setData("systemid", sysid + 1)
        newFile = open(f'./systems/{username}.xml', mode='wt', encoding='utf-8')
        newFile.write(template('system.tpl', {
            'userdata': str(template('userdata.tpl', {
                'username': username, 
                'userid': userid
            })),
            'systemdata': str(template('systemdata.tpl', {
                'sysname': sysname
            }))
        }))
        newFile.close()

def newAlter(username, role, name, age, pronouns, proxy):
    if os.path.isfile(f'./systems/{username}.xml') == True:
        alterid = int(getData("alterid"))
        setData("alterid", alterid + 1)
        sysFile = open(f'./systems/{username}.xml', mode='a', encoding='utf-8')
        sysFile.write(template('alter.tpl', {
            'alterid': alterid,
            'role': role, 
            'name': name, 
            'age': age,
            'pronouns': pronouns,
            'proxy': proxy
        }))
        sysFile.close()


# I used my system/user/host info
newSystem("aces_bella", "1016399059914866869", "The Chaos System")
newAlter("aces_bella", "Host", "Isabella", "16", "She/It", "i;;text")