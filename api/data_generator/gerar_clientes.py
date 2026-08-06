from datetime import timedelta
import random

from faker import Faker

from config_gerador import *
from helpers import com_chance, talvez_none, talvez_vazio, sujar_texto, enviar

fake = Faker("pt_PT")

NOMES_MASCULINOS = [
    "Miguel", "João", "José", "António", "Manuel", "Carlos", "Marcos", "Ricardo",
    "Paulo", "Pedro", "Francisco", "Domingos", "Fernando", "Eduardo", "Augusto",
    "Abel", "Adão", "Alberto", "Alexandre", "Alfredo", "Américo", "Ângelo",
    "Aristides", "Artur", "Baltazar", "Benedito", "Bernardo", "Celestino",
    "Cipriano", "Daniel", "David", "Diogo", "Edson", "Elias", "Ernesto",
    "Evaristo", "Fábio", "Feliciano", "Felisberto", "Filipe", "Gabriel",
    "Gaspar", "Gilberto", "Hélder", "Henrique", "Hermenegildo", "Hilário",
    "Ivo", "Jaime", "Joel", "Jonas", "Jorge", "Justino", "Laurindo", "Lázaro",
    "Leandro", "Lino", "Lourenço", "Lucas", "Ludgero", "Luís", "Macário",
    "Mário", "Mateus", "Maurício", "Moisés", "Nelson", "Nuno", "Octávio",
    "Orlando", "Osvaldo", "Pascoal", "Patrício", "Raúl", "Renato", "Roberto",
    "Rui", "Salvador", "Samuel", "Sebastião", "Simão", "Teodoro", "Tiago",
    "Vasco", "Victor", "Vítor", "Waldemar", "Zeferino",
]

NOMES_FEMININOS = [
    "Ana", "Maria", "Isabel", "Cecília", "Lúcia", "Rosa", "Teresa", "Sónia",
    "Adelaide", "Albertina", "Alexandra", "Alice", "Amélia", "Angelina",
    "Antónia", "Arminda", "Augusta", "Aurora", "Bárbara", "Beatriz", "Benedita",
    "Bernardete", "Carla", "Carmina", "Carolina", "Catarina", "Celeste",
    "Célia", "Cristina", "Dalva", "Deolinda", "Dina", "Dolores", "Domingas",
    "Edite", "Elsa", "Ema", "Emília", "Ermelinda", "Esperança", "Eulália",
    "Eva", "Felismina", "Fernanda", "Filomena", "Fátima", "Gabriela", "Graça",
    "Helena", "Hortência", "Inês", "Irene", "Ivone", "Jacinta", "Joana",
    "Josefina", "Júlia", "Justina", "Laurinda", "Leonor", "Liliana", "Lurdes",
    "Luzia", "Madalena", "Marcelina", "Margarida", "Mariana", "Matilde",
    "Maura", "Micaela", "Miquelina", "Natália", "Nídia", "Noémia", "Olga",
    "Palmira", "Paulina", "Perpétua", "Quitéria", "Raquel", "Regina", "Rita",
    "Rosalina", "Salomé", "Sandra", "Sara", "Severina", "Sílvia", "Sofia",
    "Suzana", "Tereza", "Valentina", "Vera", "Vitória", "Zulmira",
]

NOMES_AFRICANOS_MASCULINOS = [
    "Kiala", "Bumba", "Dombaxi", "Tchissola", "Nsimba", "Massala", "Cahilo",
    "Sassa", "Quissanga", "Kitumba", "Miala", "Kassoma", "Tchilala", "Ngombo",
    "Chipenda", "Tunda", "Vungo", "Chicungo", "Mbala", "Zumba", "Cazombo",
    "Quipuco", "Ngola", "Kinanga", "Cahumbu", "Mussunga", "Tchingolo",
    "Salukombo", "Bula", "Cambinda", "Canganjo", "Mazala", "Ndumba",
    "Tchimanda", "Nzola", "Manuelito", "Cangongo", "Quissanga", "Muanza",
]

NOMES_AFRICANOS_FEMININOS = [
    "Nzambi", "Kiakanda", "Lemba", "Munjolo", "Candando", "Cassule",
    "Kissanga", "Ndjala", "Punga", "Quibinda", "Tchicala", "Zangui", "Camela",
    "Gingui", "Kambua", "Massanga", "Tchimali", "Vana", "Xana", "Nuninho",
    "Dikota", "Nzinga", "Quissanga", "Muenho", "Catumbela",
]

SOBRENOMES = [
    "Silva", "Costa", "Pereira", "Lopes", "Fernandes", "Martins", "Gomes",
    "dos Santos", "Mendes", "Dias", "Afonso", "de Almeida", "Nganga",
    "Mabiala", "Kiala", "Bango", "Neto", "Paulo", "Quiala", "Tchamba",
    "Fortunato", "Cassoma", "Catumbela", "Chipenda", "Muhongo", "Kandimba",
    "Kalunga", "Marques", "Moreira", "Nunes", "Pinheiro", "Rocha", "Rodrigues",
    "Simões", "Soares", "Sousa", "Tavares", "Teixeira", "Vasconcelos",
    "André", "António", "Baptista", "Barros", "Cardoso", "Carvalho",
    "Correia", "Coelho", "Cunha", "Domingos", "Esteves", "Ferreira",
    "Gonçalves", "Guerra", "Henriques", "Lourenço", "Machado", "Matos",
    "Miranda", "Nascimento", "Oliveira", "Pires", "Quintas", "Ramos", "Reis",
    "Ribeiro", "Sá", "Torres", "Vaz", "da Conceição", "Sebastião", "Caetano",
    "Dala", "Kitumba", "Lussati", "Massala", "Nzolani", "Paxe", "Suca",
    "Tchilala", "Vilinga", "Wambo", "Kaya", "Muana",
]

PROVINCIAS_MUNICIPIOS = {
    "Luanda": ["Luanda", "Cacuaco", "Belas", "Cazenga", "Ícolo e Bengo", "Quissama", "Talatona", "Viana"],
    "Bengo": ["Caxito", "Dande", "Bula Atumba", "Dembos", "Ambriz", "Nambuangongo", "Pango Aluquém"],
    "Benguela": ["Benguela", "Lobito", "Baía Farta", "Balombo", "Bocoio", "Caimbambo", "Catumbela", "Chongoroi", "Cubal", "Ganda"],
    "Bié": ["Cuíto", "Andulo", "Camacupa", "Catabola", "Chinguar", "Chitembo", "Cuemba", "Cunhinga", "Nharea"],
    "Cabinda": ["Cabinda", "Buco-Zau", "Cacongo", "Belize"],
    "Cuando Cubango": ["Menongue", "Calai", "Cuangar", "Cuchi", "Cuito Cuanavale", "Dirico", "Mavinga", "Nancova", "Rivungo"],
    "Cuanza Norte": ["N'dalatando", "Ambaca", "Banga", "Bolongongo", "Cambambe", "Cazengo", "Golungo Alto", "Gonguembo", "Lucala", "Quiculungo", "Samba Caju"],
    "Cuanza Sul": ["Sumbe", "Amboim", "Cassongue", "Cela", "Conda", "Ebo", "Libolo", "Mussende", "Porto Amboim", "Quibala", "Quilenda", "Seles"],
    "Cunene": ["Ondjiva", "Cuanhama", "Cahama", "Curoca", "Cuvelai", "Namacunde", "Ombadja"],
    "Huambo": ["Huambo", "Bailundo", "Caála", "Cachiungo", "Chicala-Cholohanga", "Chinjenje", "Ecunha", "Longonjo", "Mungo"],
    "Huíla": ["Lubango", "Caconda", "Caluquembe", "Chibia", "Chicomba", "Chipindo", "Cuvango", "Gambos", "Humpata", "Jamba", "Matala", "Quipungo"],
    "Lunda Norte": ["Dundo", "Cambulo", "Capenda-Camulemba", "Caungula", "Chitato", "Cuango", "Cuilo", "Lubalo", "Lucapa", "Xá-Muteba"],
    "Lunda Sul": ["Saurimo", "Cacolo", "Dala", "Muconda"],
    "Malanje": ["Malanje", "Cacuso", "Calandula", "Cambundi-Catembo", "Cangandala", "Caombo", "Cunda-Dia-Baze", "Luquembo", "Marimba", "Massango", "Mucari", "Quela", "Quirima"],
    "Moxico": ["Luena", "Alto Zambeze", "Bundas", "Camanongue", "Cameia", "Léua", "Luau", "Luchazes"],
    "Namibe": ["Moçâmedes", "Bibala", "Camucuio", "Tômbua", "Virei"],
    "Uíge": ["Uíge", "Alto Cauale", "Ambuíla", "Bembe", "Buengas", "Bungo", "Damba", "Milunga", "Mucaba", "Negage", "Puri", "Quimbele", "Quitexe", "Sanza Pombo", "Songo", "Zombo"],
    "Zaire": ["M'banza Kongo", "Cuimba", "Nóqui", "N'zeto", "Soyo", "Tomboco"],
}

RUA = [
    "Rua de Benguela", "Avenida 4 de Fevereiro", "Rua Amílcar Cabral",
    "Avenida Deolinda Rodrigues", "Rua Hoji-ya-Henda", "Rua da Missão",
    "Avenida Comandante Valódia", "Rua Rainha Ginga", "Rua do Maculusso",
    "Avenida dos Combatentes", "Rua Cónego Manuel das Neves", "Rua Pedro de Castro Van-Dúnem Loy",
    "Avenida Fidel Castro", "Rua dos Kwanza", "Rua de São Paulo", "Avenida Almirante Reis",
    "Rua Ngola Kiluanje", "Rua António Jacinto", "Rua Agostinho Neto", "Avenida Joaquim Kapango",
]

OPERADORAS = ["91", "92", "93", "94", "99", "98"]

PROFISSOES = [
    "Professor", "Enfermeiro", "Médico", "Motorista", "Comerciante",
    "Funcionário Público", "Agricultor", "Pescador", "Pedreiro", "Carpinteiro",
    "Eletricista", "Mecânico", "Advogado", "Contabilista", "Engenheiro",
    "Gestor", "Bancário", "Vendedor", "Cabeleireira", "Costureira",
    "Empregada Doméstica", "Segurança", "Militar", "Policial", "Empresário",
    "Estudante", "Reformado", "Desempregado", "Técnico de Informática", "Farmacêutico",
]

ESTADOS_CIVIS = ["Solteiro", "Solteira", "Casado", "Casada", "Divorciado", "Divorciada", "Viúvo", "Viúva", "União de Facto"]


def telefone_angola():
    """Gera números no padrão angolano (+244 9XX XXX XXX) com variações de formato."""
    numero = f"{random.choice(OPERADORAS)}{random.randint(1000000, 9999999)}"
    formato = random.choice([
        f"+244{numero}",
        f"+244 {numero[:3]} {numero[3:6]} {numero[6:]}",
        f"9{numero}",
        f"{numero[:3]} {numero[3:6]} {numero[6:]}",
        f"00244 {numero[:3]} {numero[3:6]} {numero[6:]}",
        f"+2449{numero}",
    ])
    return formato


def bi_angola():
    """Bilhete de Identidade angolano: 6 dígitos + 2 letras (ex: 0045362LA)."""
    letras = "".join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ", k=2))
    return f"{random.randint(100000, 999999)}{letras}"


def nif_angola():
    """NIF angolano: 10 dígitos."""
    return f"{random.randint(1000000000, 9999999999)}"


def email_angola(nome, sobrenome):
    provedores = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com", "gmail.co.ao"]
    separadores = ["", ".", "_", "-"]
    usuario = f"{nome}{random.choice(separadores)}{sobrenome}".replace(" ", "").lower()
    return f"{usuario}@{random.choice(provedores)}"


def rendimento_kwanza():
    """Rendimento mensal realista em Kz (log-distribuído)."""
    base = random.lognormvariate(12.5, 0.9)
    return round(max(15000, min(base, 8000000)), 2)


def gerar_clientes(total, api_url):
    clientes = []
    emails_gerados = []
    bis_gerados = []
    pessoas_geradas = []
    duplicados = 0

    for _ in range(total):
        nome_masculino = random.random() < 0.5
        africano = random.random() < 0.45

        if nome_masculino:
            nome = random.choice(NOMES_AFRICANOS_MASCULINOS if africano else NOMES_MASCULINOS)
            genero = "M"
        else:
            nome = random.choice(NOMES_AFRICANOS_FEMININOS if africano else NOMES_FEMININOS)
            genero = "F"

        # ~3% de pessoas duplicadas (mesmo nome + BI repetidos) -> ótimo para ETL
        if pessoas_geradas and com_chance(CHANCE_PESSOA_DUPLICADA):
            nome, sobrenome, bi = random.choice(pessoas_geradas)
            duplicados += 1
        else:
            sobrenome = random.choice(SOBRENOMES)
            bi = None if com_chance(CHANCE_BI_NULO) else bi_angola()
            pessoas_geradas.append((nome, sobrenome, bi))

        if africano:
            sobrenome = random.choice([sobrenome, random.choice(SOBRENOMES), random.choice(NOMES_AFRICANOS_MASCULINOS)])

        email = email_angola(nome, sobrenome)

        # duplicar emails deliberadamente (cerca de 10%)
        if emails_gerados and com_chance(CHANCE_EMAIL_DUPLICADO):
            email = random.choice(emails_gerados)
        else:
            emails_gerados.append(email)

        # duplicar BI deliberadamente
        if bis_gerados and com_chance(CHANCE_BI_DUPLICADO):
            bi = random.choice(bis_gerados)
        elif bi:
            bis_gerados.append(bi)

        provincia, municipios = random.choice(list(PROVINCIAS_MUNICIPIOS.items()))
        municipio = random.choice(municipios)

        data = {
            "primeiro_nome": sujar_texto(nome, chance_none=0.03, chance_vazio=0.02),
            "ultimo_nome": sujar_texto(sobrenome, chance_none=0.05, chance_vazio=0.02),
            "email": talvez_none(talvez_vazio(email, CHANCE_EMAIL_VAZIO), CHANCE_EMAIL_NULO),
            "telefone": talvez_none(talvez_vazio(telefone_angola(), CHANCE_TELEFONE_VAZIO), CHANCE_TELEFONE_NULO),
            "bi": sujar_texto(bi, chance_none=0.02, chance_vazio=0.02),
            "nif": talvez_none(nif_angola(), CHANCE_NIF_NULO),
            "morada": talvez_none(f"{random.randint(1, 300)} {random.choice(RUA)}, {municipio}", CHANCE_MORADA_NULA),
            "provincia": talvez_none(sujar_texto(provincia, chance_none=0.02, chance_vazio=0.02), 0.03),
            "municipio": talvez_none(municipio, 0.03),
            "data_nascimento": gerar_data_nascimento(),
            "genero": talvez_none(genero, CHANCE_GENERO_NULO),
            "estado_civil": talvez_none(random.choice(ESTADOS_CIVIS), CHANCE_ESTADO_CIVIL_NULO),
            "profissao": talvez_none(random.choice(PROFISSOES), CHANCE_PROFISSAO_NULA),
            "rendimento_mensal": talvez_none(rendimento_kwanza(), CHANCE_RENDIMENTO_NULO),
        }

        novo_id = enviar(api_url, "clientes", data)
        if novo_id:
            clientes.append(novo_id)

    print(f"  - Duplicados intencionais de pessoas: {duplicados}")
    return clientes


def gerar_data_nascimento():
    if com_chance(CHANCE_DATA_NASC_INVALIDA):
        return random.choice(["31/02/1990", "1990-13-40", "01-01-19", "não informada", ""])
    if com_chance(CHANCE_DATA_NASC_NULA):
        return None
    return fake.date_of_birth(minimum_age=18, maximum_age=85).strftime("%Y-%m-%d")
