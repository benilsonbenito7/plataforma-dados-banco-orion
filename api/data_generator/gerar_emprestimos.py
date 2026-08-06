import requests
import random
from datetime import date, timedelta



def gerar_emprestimos(total, contas, api_url):


    emprestimos=[]


    for i in range(total):


        inicio = date.today() - timedelta(
            days=random.randint(1,1000)
        )


        fim = inicio + timedelta(
            days=random.randint(365,1500)
        )


        data={


            "conta":
                random.choice(contas),


            "valor":
                round(
                    random.uniform(
                        5000,
                        500000
                    ),
                    2
                ),


            "taxa_juros":
                round(
                    random.uniform(
                        1,
                        20
                    ),
                    2
                ),


            "data_inicio":
                inicio.isoformat(),


            "data_fim":
                fim.isoformat(),


            "parcelas":
                random.choice(
                    [6,12,18,24,36]
                ),


            "valor_parcela":
                round(
                    random.uniform(
                        500,
                        50000
                    ),
                    2
                ),


            "status":
                random.choice(
                    [
                    "PENDENTE",
                    "APROVADO",
                    "QUITADO",
                    "REJEITADO"
                    ]
                )
        }



        response=requests.post(
            f"{api_url}/emprestimos",
            json=data
        )


        if response.status_code==200:

            emprestimos.append(
                response.json()["id"]
            )

        else:
            print(response.text)



    return emprestimos