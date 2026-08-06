import requests
import random


def gerar_contas(total, clientes, api_url):

    contas = []


    for i in range(total):

        data = {


            "cliente":
                random.choice(clientes),


            "numero_conta":
                str(random.randint(100000,999999)),


            "tipo_conta":
                random.choice(
                    [
                        "CORRENTE",
                        "POUPANCA",
                        "INVESTIMENTO"
                    ]
                ),


            "saldo":
                round(
                    random.uniform(
                        -10000,
                        500000
                    ),
                    2
                ),


            "limite":
                round(
                    random.uniform(
                        0,
                        100000
                    ),
                    2
                ),


            "status":
                random.choice(
                    [
                        "ATIVA",
                        "ATIVA",
                        "BLOQUEADA",
                        "ENCERRADA"
                    ]
                )

        }


        response = requests.post(
            f"{api_url}/contas",
            json=data
        )


        if response.status_code == 200:

            contas.append(
                response.json()["id"]
            )

        else:

            print(
                "Erro conta:",
                response.text
            )


    return contas