
import re

def identify_card_brand(card_number):
    card_number = str(card_number).replace(' ', '').replace('-', '')

    if not card_number.isdigit():
        return 'Número de cartão inválido: contém caracteres não numéricos.'

    # Visa: Starts with 4, length 13 or 16
    if re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', card_number):
        return 'Visa'
    # MasterCard: Starts with 51-55, length 16
    elif re.match(r'^5[1-5][0-9]{14}$', card_number):
        return 'MasterCard'
    # American Express: Starts with 34 or 37, length 15
    elif re.match(r'^3[47][0-9]{13}$', card_number):
        return 'American Express'
    # Discover: Starts with 6011, 644-649, 65, length 16 or 19
    elif re.match(r'^6(?:011|5[0-9]{2}|4[4-9][0-9]{1})[0-9]{12}(?:[0-9]{3})?$', card_number):
        return 'Discover'
    # Diners Club: Starts with 300-305, 309, 36, 38-39, length 14 or 16
    elif re.match(r'^3(?:0[0-5]|[689])[0-9]{11}(?:[0-9]{2})?$', card_number):
        return 'Diners Club'
    # JCB: Starts with 3528-3589, length 16 or 19
    elif re.match(r'^(?:2131|1800|35\d{3})\d{11}$', card_number):
        return 'JCB'
    # Elo: Starts with 401178, 401179, 431274, 438935, 451416, 457393, 457631, 504175, 506699-506778, 509000-509999, 627780, 636297, 636368, 650031-650033, 650035-650051, 650405-650439, 650485-650538, 650541-650598, 650700-650718, 650720-650727, 650901-650978, 651652-651679, 655000-655019, 655021-655058, length 16
    elif re.match(r'^(?:401178|401179|431274|438935|451416|457393|457631|504175|506699|5067[0-7][0-9]|509[0-9]{3}|627780|636297|636368|65003[1-3]|6500[3-5][0-9]|6504[0-3][0-9]|65048[5-9]|65049[0-9]|6505[0-3][0-9]|65054[1-9]|6505[5-9][0-9]|65070[0-9]|65071[0-8]|65072[0-7]|65090[1-9]|6509[1-7][0-9]|65165[2-9]|6516[6-7][0-9]|65500[0-9]|65501[0-9]|65502[1-9]|6550[3-5][0-9])[0-9]{10}$', card_number):
        return 'Elo'
    else:
        return 'Bandeira desconhecida ou número inválido.'

if __name__ == '__main__':
    print("Bem-vindo ao Identificador de Bandeiras de Cartão de Crédito!")
    while True:
        card_input = input("Digite o número do cartão (ou 'sair' para encerrar): ")
        if card_input.lower() == 'sair':
            break
        brand = identify_card_brand(card_input)
        print(f"A bandeira do cartão é: {brand}\n")



