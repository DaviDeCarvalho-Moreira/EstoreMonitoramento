from app.database.db_config import session

from app.models.products import Product
from app.models.store import Store


def db_insert(cash, installment, title_product, url, store_id):
    
    product = Product(
        product_name=title_product,
        product_url=url,
        price_avista=cash,
        price_parcelado=installment,
        store_id=store_id
    )
    session.add(product)
    session.commit()

# db = Store(store_name="TERABYTE")
# session.add(db)
# session.commit()
    





