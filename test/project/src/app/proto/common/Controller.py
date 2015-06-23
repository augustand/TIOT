#encoding=utf-8

class Controller(object):
    online_session = {}#在线设备列表

    def __init__(self):
        pass

    def get_online_session(self, name):
        if not self.online_session.get(name):
            print "您没有找到!"
            return None
        print "您得到的设备是:"+name
        return self.online_session.get(name)

    def add_client(self, name, transport):
        self.online_session[name] = transport
        print "您现在的设备是:"
        print self.online_session
        print "\n"

    def del_client(self, name):
        if self.online_session.get(name):
            print "您要删除的设备是:"+name
            del self.online_session[name]
        else:
            print "您要删除的设备不存在"
        print "您现在的设备是:"
        print self.online_session
        print "\n"
