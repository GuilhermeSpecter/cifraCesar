# Criptografia Simples em Python

Este projeto é uma implementação simples de um programa em Python para criptografar e descriptografar textos usando uma cifra de deslocamento (também conhecida como cifra de César).

## Funcionalidades

- Criptografar um texto informando um deslocamento.
- Descriptografar um texto usando o mesmo deslocamento, com sinal invertido.
- Suporta letras maiúsculas, minúsculas e números.
- Caracteres especiais permanecem inalterados.

## Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o script:

```bash
python cyper.py
```

## Como usar

Ao iniciar o programa, você poderá escolher entre duas opções:

- 1: Criptografar
- 2: Descriptografar

Em seguida, informe:

- o texto a ser processado;
- a chave de deslocamento (número inteiro).

## Exemplo

Se você digitar:

- opção: 1
- texto: `Olá Mundo`
- chave: `3`

O resultado será:

```text
Rr~ Pqgrq
```

## Estrutura do projeto

- `cyper.py`: contém a lógica principal do programa e a interface interativa.
- `cores.py`: define as constantes de cores ANSI usadas na saída do terminal.

## Observação

Este projeto é uma implementação didática e simples de criptografia, ideal para estudos de Python e lógica de programação.
