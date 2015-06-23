import binascii
from pipe import Pipe
from common.util import toFactory, toProtocol, parsePkgs, hexStr_to_hex


@Pipe
def hello(two,one):
    print two,one

# "one" | hello("two")

a = 10
class Hello:
    hello = 10
# print eval('Hello()').hello
# n = eval('Hello')
# print n().hello

# print 'hello'.__contains__('H')
# print 'hHHHlo'.lower()
# a = 'hello'
# print a[0].upper()
# print a[0].upper()+a[1:]



# from common.util import firstChar_toUpper
# x = "xBee" | firstChar_toUpper
# p = __import__("xBee" + '.' + x + 'Protocol')
# print eval('p.' + x + 'Protocol.' + x + 'Protocol')
# tt = __import__('xBee.test.test')
# print eval("tt.test.test.Hello")
# print eval('tt.test.test.a')
# print eval("tt.test.test.Hello")().hello


# x1 = "xBee" | toFactory
# x2 = "xBee" | toProtocol
# print 'rfidListener' | toFactory
# print x1("xx",'xx')
# print x2


# print "toFactory".replace("Factory","")
# print "toFactory".__contains__("Factory")

import platform
# print platform.uname()
def TestPlatform():
    print ("----------Operation System--------------------------")
    #Windows will be : (32bit, WindowsPE)
    #Linux will be : (32bit, ELF)
    print(platform.architecture())

    #Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
    #Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final
    print(platform.platform())

    #Windows will be : Windows
    #Linux will be : Linux
    print(platform.system())

    print ("--------------Python Version-------------------------")
    #Windows and Linux will be : 3.1.1 or 3.1.3
    print(platform.python_version())

# TestPlatform()

def UsePlatform():
  sysstr = platform.system()
  if(sysstr =="Windows"):
    print ("Call Windows tasks")
  elif(sysstr == "Linux"):
    print ("Call Linux tasks")
  else:
    print ("Other System tasks")

# UsePlatform()


from construct import Struct, OptionalGreedyRange, Embed, Enum, Switch,String
from construct import UBInt8, UBInt16, UBInt32, UBInt64, Byte
from construct.macros import Array
rfid = Struct("frame",
                   UBInt8("flagID"),
                   String("f",1),
                     Array(4, String("nodeID",1)),
                   )
mm = rfid.parse("F1070E0100138E0000F21D65" | hexStr_to_hex)
print mm
print [binascii.b2a_hex(x) for x in mm.nodeID]
# print binascii.b2a_hex(mm.f)
# print mm.flagID
# print '01' | hex_to_dec
# print [binascii.b2a_hex(x) for x in mm.nodeID ]

a = {'or':2}
# print a[::-1]
if not a.get('order'):
    print 12
