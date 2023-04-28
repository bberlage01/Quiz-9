#Problem3
import dbm
# Houses=dbm.open("captions","c")
# Houses["House1.png"]="3 bathroom blue house"
# Houses["House2.png"]="2 bedroom yellow house"
# Houses["House3.png"]="9 bathroom mansion"
# Houses["House4.png"]="4 bedroom victorian"
# Houses["House5.png"]="3 bathroom red house in Chicago"
# Houses["House6.png"]="1 bedroom apartment in NYC"

#Problem4
Houses=dbm.open("captions","c")
Houses["House1.png"]="16 bedroom large house"
Houses["House2.png"]="6 bedroom blue house in San Diego"
Houses["House3.png"]="9 bathroom mansion"
Houses["House4.png"]="4 bedroom victorian"
Houses["House5.png"]="3 bathroom red house in Chicago"
Houses["House6.png"]="1 bedroom apartment in NYC"

for item in Houses:
    print(item,Houses[item])
Houses.close()
