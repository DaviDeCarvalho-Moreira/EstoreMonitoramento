from app.database.db_config import session
from app.models.price import Price
from app.models.products import Product
from app.models.store import Store


def db_insert(cash, installment, title_product, url, store_id):
    
    product = Product(
        product_name=title_product,
        product_url=url,
        store_id=store_id
    )
    session.add(product)
    session.flush()  

    price = Price(
        price_avista=cash,
        price_parcelado=installment,
        product_id=product.product_id  
    )
    session.add(price)
    session.commit()
    
    
db = Store(store_name="TERABYTE")
session.add(db)
session.commit()
    





