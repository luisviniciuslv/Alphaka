# Lexer

Passa caractere por caractere e vai quebrar o texto em uma lista de
tokens, o token é um objeto simples, e tem um tipo e opcionalmente
um valor. Cada token vem de apenas um pequeno seguimento do código
por exemplo um número inteiro, um identificador, um operador, etc.

# Parser

Cria uma árvore sintática do programa a partir dos tokens criados pelo lexer

Exemplo

1 + 2 \* 3

                   | BinOp (PLUS) |
                      I       I
            | Number (1) |    | BinOp (MUL) |
                                I             I
                          | Number (2) |  | Number (3) |

(INT:1,PLUS,(INT:2,MUL,INT:3))

Esta árvore nos mostra todas as operações que devem ser feitas e suas ordens.
