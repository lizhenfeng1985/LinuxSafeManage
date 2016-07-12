# -*- coding: utf-8 -*-

import ConfigParser


gConfig = {
    'Service' : {
        'IP'   : '127.0.0.1',
        'Port' : '9001',
    },
    'Center' : {
        'IP'   : '127.0.0.1',
        'Port' : '9002',
    },
}

gLogin = {
    'User'  : '',
    'Tokey' : '',
}

def ReadConfigFile(conffile):
    conf = ConfigParser.ConfigParser() 
    conf.read(conffile)
    gConfig['Service']['IP'] = conf.get("Service", "IP")
    gConfig['Service']['Port'] = conf.get("Service", "Port")
    gConfig['Center']['IP'] = conf.get("Center", "IP")
    gConfig['Center']['Port'] = conf.get("Center", "Port")
    #ServicePort = conf.getint("Service", "Port")
    return gConfig

def UpdateConfigFile(conffile, config):
    gConfig = config
    conf = ConfigParser.ConfigParser() 
    conf.read(conffile)
    for section, items in config.items():
        for k, v in items.items():
            conf.set(section, k, v)
    conf.write(open(conffile, "w"))

if __name__ == '__main__':
    conffile = "config.ini"
    cfg = ReadConfigFile(conffile)
    print cfg
    cfg['Service']['Port'] = '9001'
    UpdateConfigFile(conffile, cfg)
