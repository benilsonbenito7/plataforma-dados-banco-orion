import requests
import random



def gerar_pagamentos(total, contas, api_url):


    pagamentos=[]


    categorias=[

        "ENERGIA",
        "AGUA",
        "INTERNET",
        "SALARIO",
        "IMPOSTOS"

    ]


    for i in range(total):


        data={


            "conta":
                random.choice(contas),


            "descricao":
                random.choice(
                    [
                    "Pagamento mensal",
                    "Conta de energia",
                    "Internet",
                    "Serviço bancário"
                    ]
                ),


            "valor":
                round(
                    random.uniform(
                        10,
                        100000
                    ),
                    2
                ),


            "categoria":
                random.choice(categorias),


            "status":
                random.choice(
                    [
                    "PENDENTE",
                    "CONCLUIDO",
                    "FALHOU"
                    ]
                )

        }



        response=requests.post(
            f"{api_url}/pagamentos",
            json=data
        )


        if response.status_code==200:

            pagamentos.append(
                response.json()["id"]
            )


    return pagamentos