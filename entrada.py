def area_paredes():
    parede_altura = []
    parede_largura = []
    cont = 1
    parede_metros = []
    janela = 2.4
    porta = 1.52

    while True:
        altura = float(input(f"Digite a altura da {cont}ª parede: "))
        largura = float(input(f"Digite a largura da {cont}ª parede: "))
        metros = altura * largura
        if metros < 1 or metros > 15 or largura < 0 or altura < 0:
            print('A metragem da parede em m2 não poderá ser menor que 1m2 ou maior que 15m2')
            continue
        else:
            tot_janelas = int(input(f"Digite a quantidade de janelas da {cont}ª parede: "))
            tot_portas = int(input(f"Digite a quantidade de portas da {cont}ª parede: "))
            area_vazia = (tot_janelas * janela) + (tot_portas * porta)
            if area_vazia > (0.5 * metros):
                print('A metragem da(s) janala(s) e/ou porta(s) não poderá ser maior que 50% da parede')
                continue

            else:
                parede_largura.append(largura)
                parede_altura.append(altura)
                parede_metros.append(metros - area_vazia)
        cont += 1
        if cont == 5:
            break

    metros = sum(parede_metros)
    return metros
