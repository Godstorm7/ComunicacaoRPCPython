import requests

def menu():
    print("\n--- MENU CARROS RPC ---")
    print("1. Criar carro")
    print("2. Ler carro")
    print("3. Atualizar carro")
    print("4. Deletar carro")
    print("5. Listar carros")
    print("0. Sair")
    return input("Escolha uma opção: ")

def callRpc(method, params, id):
    response = requests.post("http://localhost:5000", json={
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": id
    })
    print(f"Status: {response.status_code}")
    print(f"Resposta: {response.text}\n")

while True:
    op = menu()
    if op == "1":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        callRpc("createCar", [marca, modelo, ano], 1)
    elif op == "2":
        _id = int(input("ID do carro: "))
        callRpc("readCar", [_id], 2)
    elif op == "3":
        _id = int(input("ID do carro: "))
        marca = input("Nova marca (ou Enter p/ manter): ")
        modelo = input("Novo modelo (ou Enter p/ manter): ")
        ano = input("Novo ano (ou Enter p/ manter): ")
        ano_val = int(ano) if ano else None
        marca_val = marca if marca else None
        modelo_val = modelo if modelo else None
        callRpc("updateCar", [_id, marca_val, modelo_val, ano_val], 3)
    elif op == "4":
        _id = int(input("ID do carro: "))
        callRpc("deleteCar", [_id], 4)
    elif op == "5":
        callRpc("listCars", [], 5)
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
