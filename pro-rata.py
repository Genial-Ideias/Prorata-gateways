from typing import List
from typer import Typer, echo

from sympy.abc import x
from sympy.solvers import solve


app = Typer()

DIAS_MES = 30

@app.command()
def test():
    taxa = 1.90
    antecipar_em = 15
    taxa_antecipacao = 1.00
    taxa_prorata = 1.90

    # a = 2.83 - ( 1.90 + ((x/30)*28) )

    echo(solve(taxa_prorata - (taxa + ( x / DIAS_MES * antecipar_em ) ) ))


@app.command()
def aplica_pro_rata(taxa: float, taxa_antecipacao: float, parcela: int, receber_em: List[int], ):

    parcela

    for dia in receber_em:
        antecipar_em = get_dias_antecipacao(dia)
        taxa_prorata = taxa + ( taxa_antecipacao / DIAS_MES * antecipar_em )
        taxa_prorata = round(taxa_prorata, 2)
        echo((dia, taxa_prorata))


@app.command()
def descobre_taxa_antecipacao(taxa_base: float, taxa_prorata: float, antecipar_em: int):
    dias_antecipados = get_dias_antecipacao(antecipar_em)
    taxa_antecipacao = solve(taxa_prorata - (taxa_base + ( x / DIAS_MES * dias_antecipados )) )
    echo( f'Taxa Antecipação: { round(taxa_antecipacao[0], 2) }' )


@app.command()
def aplica_taxa(valor: float, taxa: float):
    valor_corrigido = valor * taxa / 100
    valor_corrigido = round(valor_corrigido, 2)
    valor_taxa = valor - valor_corrigido
    echo((valor, valor_taxa, valor_corrigido))


def get_dias_antecipacao(receber_em: int):
    antecipar_em = (DIAS_MES - receber_em)
    return antecipar_em if antecipar_em >= 0 else 0


if __name__ == '__main__':
    app()



