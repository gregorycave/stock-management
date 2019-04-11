
class StockItem:
  def __init__(self,stockID,category,description,qtyInStock):
    self._stockID=stockID
    self._category=category
    self._description=description
    self._qtyInStock=qtyInStock

  def get_stockID(self):
    return self._stockID

  def get_category(self):
    return self._category

  def get_description(self):
    return self._description

  def get_qtyInStock(self):
    return self._qtyInStock
  
  def set_stockID(self,new_stockID):
    self._manufact=new_stockID

  def set_manufact(self,new_category):
    self._manufact=new_category

  def set_model(self,new_description):
    self._model=new_description

  def set_qtyInStock(self,new_qtyInStock):
    self._retail_price=new_qtyInStock
