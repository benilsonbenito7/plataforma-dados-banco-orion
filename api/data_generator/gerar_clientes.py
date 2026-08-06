from faker import Faker
import requests
import random


fake = Faker("pt_BR")


def gerar_clientes(total, api_url):

    clientes = []


    for i in range(total):

        nome = fake.first_name()
        sobrenome = fake.last_name()


        # dados sujos propositalmente

        if random.random() < 0.20:
            nome = nome.upper()


        if random.random() < 0.20:
            sobrenome = " " + sobrenome + " "


        telefone = None

        if random.random() > 0.15:
            telefone = fake.msisdn()[:9]


        email = fake.email()


        # duplicados

        if random.random() < 0.05:
            email = "cliente.teste@gmail.com"



        data = {

            "primeiro_nome": nome,

            "ultimo_nome": sobrenome,

            "email": email,

            "telefone": telefone,

            "data_nascimento":
                fake.date_of_birth(
                    minimum_age=18,
                    maximum_age=80
                ).strftime("%Y-%m-%d")
        }


        response = requests.post(
            f"{api_url}/clientes",
            json=data
        )


        if response.status_code == 200:

            clientes.append(
                response.json()["id"]
            )

        else:
            print(
                "Erro cliente:",
                response.text
            )


    return clientes