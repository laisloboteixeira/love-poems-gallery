
from flask import Flask, render_template

app = Flask(__name__)

poemas = [
    {
        "titulo": "always",
        "texto": """um mês.
e já parece que te sonho há tanto tempo.
como se meu coração soubesse, lá no fundo,
que em algum canto desse mundo,
você existia.

te amar não foi surpresa —
foi abrigo.
foi encontrar um lugar onde tudo, enfim, faz sentido.

você me enxerga inteira,
mesmo quando eu me perco de mim.
e mesmo nas falhas,
me ama como quem escolhe recomeçar.

eu te amo.
com leveza, com verdade,
e com essa vontade bonita
de ser pra sempre."""
    },
    {
        "titulo": "Calmaria",
        "texto": """Sou tão sua que, se o mundo me olhasse,
veria o brilho dos seus olhos refletido em mim.
Você é o meu bem mais precioso,
e eu moraria na sua alma, se isso curasse
cada dor, cada dúvida, cada medo seu.

Quero estar cada vez mais perto,
mais dentro, mais sua.

Te amo com tudo o que sou,
pelo que já vivemos
e por tudo que ainda vamos viver.

Te amo por quem você é,
de um jeito que nem imaginei ser possível.

Te amo com leveza, com paz, com entrega.
E mesmo quando o amor transborda,
ainda é calmaria — porque é seu."""
    },
    {
        "titulo": "Good Friday",
        "texto": """Tentar alcançar o coração dela
era como me perder antes mesmo do toque.
Um mistério tão denso
que queimava por dentro sem pedir licença.

Ela deixava cicatrizes doces na minha pele,
com um olhar que despia sem piedade,
e mãos certeiras, guiadas por instinto.
O corpo dela colado ao meu
trazia um calor que fazia a noite sumir.

Coxa contra coxa,
seios em atrito,
os movimentos dela arrancando o ar do meu peito.
O prazer vinha em ondas cruas,
e o desejo era selvagem, incessante.
Eu queria mais —
eu queria ser dela até o fim."""
    },
    {
        "titulo": "Never be the same",
        "texto": """Teu cheiro repousa no meu quarto,
não no abraço que preciso,
mas na blusa que ficou comigo,
onde teu perfume se demora,
sussurrando promessas ao vento.

Teu aroma é feito de futuro,
não pertence ao agora,
nem se perde no ontem —
é a lembrança do que ainda seremos.

Como existir, sabendo que você pulsa no mundo,
sem poder morrer nos teus braços?

Mulher de beleza rara,
sensível às marés do sentir,
brisa quente de um amanhecer que dança,

teu sorriso desfaz meus medos,
teu toque me enlaça em silêncio,
teu beijo cala minha alma —
e em cada gesto teu,
me descubro inteiramente tua."""
    },
    {
        "titulo": "She gets the girl",
        "texto": """Mal virou a esquina e já era saudade,
daquelas que grudam na alma.
Saudade do teu olhar ancorado no meu,
da tua boca encaixada na minha,
dos teus dedos desenhando caminhos na minha pele.
Saudade de ser tua,
de te sentir inteira,
de caber em cada pedaço teu.

Vontade de te guardar no peito,
de carregar tuas dores no colo,
de juntar teus cacos com carinho,
só pra te chamar de minha.
Meu abrigo,
minha luz,
meu amor.

Tão linda quanto a brisa de uma noite chuvosa,
com a lua molhando o mar com seu brilho,
como quem espalha amor nas ondas,
feito o que nasceu, silencioso e forte,
aqui dentro de mim,
por você
e por tudo que só você sabe carregar."""
    },
    {
        "titulo": "Skin and bones",
        "texto": """Vaguei dentro de mim
e te encontrei onde a pele ainda sente tua falta.
Memória que não falha,
que não atrasa,
que não me esquece —
como você.
Te quis ontem,
te quero agora,
e sei que amanhã meu corpo vai te desejar do mesmo jeito.

Quero teu beijo com a sede dos meus silêncios.
Teu olhar preso no meu,
dizendo tudo o que as palavras não alcançam.
Quero minha boca descobrindo tua pele devagar,
meus lábios na curva da tua nuca,
meus dedos te desenhando como quem escreve um segredo.

Quero você,
mesmo quando finjo que não.
Mesmo quando o dia passa e eu não percebo.
Minha pele carrega teu gosto,
teu nome,
tua ausência.
E agora ela só pertence a você."""
    },
    {
        "titulo": "between the skin",
        "texto": """Carrega o mistério da noite
e a luz de quem nunca se apaga.
Teu olhar —
intenso, calmo,
como quem já me conhece
antes mesmo do toque —
me atravessa.

Teus lábios,
metáfora do que falta,
nascem para o encontro,
e o meu desejo reconhece
o destino no contorno do teu.

Na pele,
um mapa que não leva a lugar nenhum
— e ainda assim, me perco.

Diante dela,
meu corpo silencia
e o desejo aprende a linguagem do gesto.
Tudo é calmaria,
e em mim,
vontade de permanecer."""
    },
    {
        "titulo": "Urgência",
        "texto": """Me perco nos meus devaneios repentinos,
Onde seu olhar acende a última esperança,
E encontro abrigo no toque das suas mãos.
Penso e derreto na curva do seu sorriso,
No brilho dos seus olhos — cansados da vida, mas firmes —,
Que, ainda assim, iluminam o caos ao redor.

Te quero com a urgência de quem, enfim, entende
O que é sentir moradia dentro do peito.
Porque, quando ouço a sua voz,
Algo em mim repousa,
Como se o mundo parasse por um instante
Para te ouvir também.

Te imagino me olhando de perto,
Guardando segredos que não precisam ser ditos,
Porque já tenho a única certeza:
Minha pele agora carrega o seu nome.
Eu te chamo — e te pertenço.
Preciso de você da mesma forma
Que o ar me invade, sem pedir licença.

Preciso de você,
Porque já não sei viver sem a sua luz,
Sem seu calor junto ao meu,
Sem o gosto doce do seu beijo
Marcando eternamente o meu."""
    }
]

@app.route("/")
def poemas_view():
    return render_template("index.html", poemas=poemas)

@app.route("/texto")
def texto_view():
    return render_template("texto.html")

@app.route("/fotos")
def fotos_view():
    return render_template("fotos.html")

if __name__ == "__main__":
    app.run(debug=True)
