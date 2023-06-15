from BD_SMRP.database1 import Seller
from BD_SMRP.database1.base_meta1 import global_init, create_session
from BD_SMRP.database1.takeorder import Takeorder

global_init("database1/db.db")
session = create_session()

Orders = session.query(Takeorder).all()
for Order in Orders:
    print(Order)

sellers = session.query(Seller).all()
for seller in sellers:
    print(seller)

