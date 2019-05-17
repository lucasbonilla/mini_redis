from flask import jsonify


def resposta(status, message, http_code=200, dados=None):
    """
    devolve um string json com formato especifico para as respostas dos endpoints
        :param status: True ou False
        :param message: string
        :param http_code=200: código da requisição
        :param dados=None: dados a serem apresentados no retorno
    """

    # 0 se status é false e 1 se é true
    sts = 1 if status else 0
    resposta = {"state": sts, "value": message}

    if dados is not None:
        z = resposta.copy()   # start with x's keys and values
        z.update(dados=dados)
        resposta = z

    response = jsonify(resposta)
    response.status_code = http_code

    return response