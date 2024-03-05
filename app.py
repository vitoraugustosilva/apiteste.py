from flask import Flask, request

app = Flask(__name__)

roupas = [
    {"camiseta": "marca", "items":
        [
            {"marca": "adidas", "valor": 2500.00}
        ]
    },
     {"camiseta": "modelo", "items":
        [
            {"marca": "nike", "valor": 2500.00}
        ]
    }
    ]

@app.get("/roupas")
def get_roupas():
    return {"roupas": roupas}
@app.get("/roupas/<string:camiseta>")
def get_roupas_by_camiseta(camiseta):
    for roupa in roupas:
        if roupa["camiseta"] == camiseta:
            return roupas
    return {"message": "Roupas not found"}, 404
@app.get("/roupas/<string:camiseta>/item/")
def get_item_in_roupas(camiseta):
    for roupa in roupas:
        if roupa["camiseta"] == camiseta:
            return {"items": roupa["items"]}
    return {"message": "Roupas not found"}, 404

@app.post("/roupas")
def create_roupas():
    request_data = request.get_json() #pega o conteudo do body
    new_roupas = {"camiseta": request_data["camiseta"], "items": []}
   roupas.append(new_roupas) #insere o payload na roupas
    return new_roupas, 201

@app.post("/roupas/<string:camiseta>/item")
def create_item(camiseta):
    request_data = request.get_json()
    for roupa in roupas:
        if roupa["camiseta"] == camiseta:
            new_item = {"marca": request_data["marca"], "valor": request_data["valor"]}
            roupa["items"].append(new_item)
            return new_item, 201
    return {"message": "camiseta nao encontrado "}, 404


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)

