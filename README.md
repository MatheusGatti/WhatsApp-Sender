<div align="center">
  <h3>WhatsApp Sender</h3>
  <img src="https://img.shields.io/github/issues/MatheusGatti/WhatsApp-Sender"/>
  <img src="https://img.shields.io/github/forks/MatheusGatti/WhatsApp-Sender"/>
  <img src="https://img.shields.io/github/stars/MatheusGatti/WhatsApp-Sender?color=yellow"/>
  <img src="https://img.shields.io/github/license/MatheusGatti/WhatsApp-Sender"/>
  <p><small>Robô desenvolvido para enviar mensagens no WhatsApp em massa para todos os contatos da sua lista de contatos no formato vCARD (iPhone/IOS/MacOS)</small></p>
</div>

<hr>

### Tecnologias utilizadas
* Python

<br>

### Bibliotecas utilizadas e necessárias para o funcionamento do robô
* selenium
* webdriver_manager

<br>

### Configurações
- No arquivo **```mensagem.txt```** configure a mensagem desejada, pode utilizar espaços, enter, quebra de linha e até emojis.
- Se está se perguntando onde colocar a lista de contatos é só você abrir o aplicativo de contatos do seu Mac e exporta-los no formato **vCard** ou qualquer outra lista que esteja no formato **vCard (```.vcf```)** e quando iniciar o robô ele pedirá o nome do arquivo junto com a extensão.


#### Configuração feita? É só iniciar o robô.

<hr>

### Como funciona?
#### O robô abrirá sua lista de contatos vCard (```.vcf```) e extrariá os números de telefone da sua lista que provavelmente estarão nesse formato:
~~~
BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//Mac OS X 10.15.7//EN
N:Nome;Sobrenome;;;
FN:Nome Sobrenome
TEL;type=CELL;type=VOICE;type=pref:+55DDD900000000
END:VCARD
~~~
#### Em seguida abrirá o navegador pedindo para conectar no seu WhatsApp via WhatsApp Web, após conectar começara a pesquisar os números no seu WhatsApp para enviar as mensagens.
#### Obs: só enviará a mensagem se você tiver o contato salvo no seu celular ou se já enviou pelo menos alguma vez uma mensagem para a pessoa (evita spam).
##### Obs 2: o robô foi feito para usuários de iPhone/IOS/MacOS ou qualquer outra pessoa que consiga ter uma lista de contatos ```.vcf```.

<br>

> **Atenção: não abuse de enviar mensagens em massa para quem não quer recebe-las, isso evita de ser banido do WhatsApp.**
