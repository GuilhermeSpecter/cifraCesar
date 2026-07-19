from cores import BLUE, BOLD, CYAN, GREEN, RED, RESET, YELLOW


def aplicar_cifra(texto, deslocamento):
    resultado = []

    for caractere in texto:
        pos = ord(caractere)

        if 48 <= pos <= 57:
            nova_pos = (pos - 48 + deslocamento) % 10 + 48
        elif 65 <= pos <= 90:
            nova_pos = (pos - 65 + deslocamento) % 26 + 65
        elif 97 <= pos <= 122:
            nova_pos = (pos - 97 + deslocamento) % 26 + 97
        else:
            nova_pos = pos

        resultado.append(chr(nova_pos))

    return "".join(resultado)


print(f"\n{BOLD}{CYAN}")
print("███████╗██╗███████╗██████╗  █████╗      ██████╗███████╗███████╗ █████╗ ██████╗")
print("██╔════╝██║██╔════╝██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗")
print("██║     ██║█████╗  ██████╔╝███████║    ██║     █████╗  ███████╗███████║██████╔╝")
print("██║     ██║██╔══╝  ██╔══██╗██╔══██║    ██║     ██╔══╝  ╚════██║██╔══██║██╔══██╗")
print("╚██████╗██║██║     ██║  ██║██║  ██║    ╚██████╗███████╗███████║██║  ██║██║  ██║")
print(" ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝")
print(f"{RESET}")
print(f"\n{BLUE}{'=' * 50}{RESET}")
print(f"{BOLD}{CYAN}{'CRIPTOGRAFA e DESCRIPTOGRAFA'.center(50)}{RESET}")
print(f"{BLUE}{'=' * 50}{RESET}")
print(f"{GREEN}[1]{RESET} {YELLOW}Criptografar{RESET}")
print(f"{GREEN}[2]{RESET} {YELLOW}Descriptografar{RESET}")
print(f"{BLUE}{'=' * 50}{RESET}")

opcao = input(f"{CYAN}Escolha uma opção (1 ou 2): {RESET}").strip()

while opcao not in {"1", "2"}:
    print(f"\n{RED}Opção inválida. Tente novamente.{RESET}")
    opcao = input(f"{CYAN}Escolha uma opção (1 ou 2): {RESET}").strip()

texto = input(f"\n{YELLOW}Digite o texto: {RESET}")
deslocamento = int(input(f"{YELLOW}Digite a chave (deslocamento): {RESET}"))

if opcao == "2":
    deslocamento = -deslocamento

texto_resultado = aplicar_cifra(texto, deslocamento)

print(f"\n{YELLOW}{'-' * 50}{RESET}")
print(f"{GREEN}{'Mensagem criptografada:' if opcao == '1' else 'Mensagem descriptografada:'}{RESET}")
print(f"{YELLOW}{'-' * 50}{RESET}")
print(f"{BOLD}{CYAN}{texto_resultado}{RESET}")
print(f"{YELLOW}{'-' * 50}{RESET}")

input ()
