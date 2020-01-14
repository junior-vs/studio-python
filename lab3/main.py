from filme import Filme
from junior import Junior
from pleno import Pleno
from serie import Serie


def inicio():
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)

    vingadores.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()

    atlanta.dar_likes()
    atlanta.dar_likes()

    listinha = [atlanta, vingadores]

    for programa in listinha:
        print(programa)


def teste_heranca_multipla():
    jose = Junior()
    jose.busca_perguntas_sem_resposta()

    luan = Pleno()
    luan.busca_perguntas_sem_resposta()
    luan.busca_cursos_do_mes()


if __name__ == "__main__":
    inicio()
    teste_heranca_multipla()
