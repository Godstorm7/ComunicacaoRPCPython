from jsonrpcserver import method, serve, Success, Error

# Banco de dados em memória para carros (usando lista)
car_db = []
car_id_counter = [1]

@method
def create_car(marca, modelo, ano):
    _id = car_id_counter[0]
    carro = {"id": _id, "marca": marca, "modelo": modelo, "ano": ano}
    car_db.append(carro)
    car_id_counter[0] += 1
    return Success(carro)

@method
def read_car(_id):
    for carro in car_db:
        if carro["id"] == _id:
            return Success(carro)
    return Error("Carro não encontrado")

@method
def update_car(_id, marca=None, modelo=None, ano=None):
    for carro in car_db:
        if carro["id"] == _id:
            if marca is not None:
                carro["marca"] = marca
            if modelo is not None:
                carro["modelo"] = modelo
            if ano is not None:
                carro["ano"] = ano
            return Success(carro)
    return Error("Carro não encontrado")

@method
def delete_car(_id):
    for i, carro in enumerate(car_db):
        if carro["id"] == _id:
            del car_db[i]
            return Success(f"Carro com id {_id} deletado")
    return Error("Carro não encontrado")

@method
def list_cars():
    return Success(car_db)

serve('localhost', 5000)
