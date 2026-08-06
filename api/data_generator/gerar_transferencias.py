import requests
import random



def gerar_transferencias(total, contas, api_url):


    transferencias=[]


    for i in range(total):


        origem=random.choice(contas)

        destino=random.choice(contas)



        data={


            "conta_origem":
                origem,


            "conta_destino":
                destino,


            "valor":
                round(
                    random.uniform(
                        50,
                        200000
                    ),
                    2
                ),


            "status":
                random.choice(
                    [
                    "PENDENTE",
                    "CONCLUIDA",
                    "FALHOU",
                    "CANCELADA"
                    ]
                )

        }


        response=requests.post(
            f"{api_url}/transferencias",
            json=data
        )


        if response.status_code==200:

            transferencias.append(
                response.json()["id"]
            )


    return transferencias