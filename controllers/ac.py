import services.database as db

def Incluir(ac):
    count = db.cursor.execute("""
    INSERT SalesLT.Product (
    Nome, 
    Conta, 
    Produto, 
    Qtde, 
    Valor
    ) OUTPUT INSERTED.ProductID 
    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    """,
    ac.nome, ac.conta, ac.produto, ac.qtde, ac.valor).rowcount 
    db.connectionString.commit()