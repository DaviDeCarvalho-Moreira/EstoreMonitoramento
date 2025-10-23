from app.database.db_config import session
from app.models.products import Product
from app.models.store import Store
from sqlalchemy import select, func,cast, Date


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


def db_consult():
    
    PR = Product
    ST = Store
    
    group_name_product = select(PR.product_name,
                                PR.product_url,
                                PR.insert_date,
                                Store.store_name,
                                func.min(PR.price_avista).label('menor_preco_avista'),
                                func.min(PR.price_parcelado).label('menor_preco_parcelado')
                                ).join(ST,PR.store_id == ST.store_id).group_by(PR.product_name,ST.store_name)
    
    results = session.execute(group_name_product).all()
    
    return results
    





