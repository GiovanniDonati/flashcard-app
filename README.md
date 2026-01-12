# Flashcards Inteligentes

App para formular flashcards de estudos, inicialmente um sistema web, voltado a mobile, sendo que posso ter as configurações:
- Categorias, para separar os grupos de flashcards, basicamente tags, pode ter várias (n-n)
- Coleções, que separa um conjunto de flascards (1-n)
- Flashcards, contendo as categorias e a coleção pertencente.
**EX: Flascard da coleção introdução ao Java, categorias - Java/Junior**

## Possíveis Telas
- Tela onde seleciona o que deseja estudar, podendo criar sequencia de estudos contendo coleções inteiras ou até mesmo categorias, sem ordem mesmo, definido isso por sequencia de execução, posso dar um nome também.

- Tela com os flashcards em si, onde tem o flashcard centralizado, em cima o nome da sequencia estudada, abaixo, ao virar o flashcard, três botões:
  * Sei / Mais ou Menos / Não Sei
  
- Tela para criar flashcards, podendo selecionar as categorias.

## Futuras Feactures
- Colocar a posibilidade de adicionar pdf com criação de flashcards automáticos.
- Fazer estilo playlist, aonde é possível compartilhar as coleções de flashcards.


### Estrutura Técnica
- API com Java/Spring, com banco de dados PostgreSQL
- FrontEnd em React com TS, usando Tailwindcss e Vite

- Usar Docker e Jenkins
- Testes unitários e automatizados
