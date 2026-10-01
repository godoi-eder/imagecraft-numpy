# **ImageCraft-Numpy**

**ImageCraft-NumPy** é uma ferramenta de linha de comando (CLI) para processamento de imagens, constuída com Python e NumPy para as manipulações de pixel.

Este projeto serve como um exemplo prático de como imagens podem ser tratadas como arrays multidimensionais e como filtros e efeitos podem ser aplicados através de operações matemáticas, sem depender de bibliotecas de imagem de alto nível como OpenCV.

## **Funcionalidades**

- Conversões para escala de cinza.
- Inversão de cores.
- Ajuste de brilho.
- Aplicação de filtro de blur(desfoque) com intensidade variável.

## **Instalação**

1. **Cloen o repositório:**

```bash
git clone https://github.com/godoi-eder/imagecraft-numpy.git
cd imagecraft-numpy
```

2. **Crie e ative um ambiente virtual:**

```bash
# Crie o ambiente
python -m venv .venv

# Ative o ambiente
# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

3. \*\*Instale as dependências:

```bash
pip install -r requirements.txt
```

## **Como usar**

A ferramenta é executada via linha de comando. O formato básico é: `python main.py <imagem_de_entrada> <caminho_de_saida> [operações]`

## **Exemplos de uso**

Suponha que você tenha uma imagem chamada `input.jpg` na pasta `exemples/`.

1. **Converter para escala de cinza:**

```bash
python main.py exemple/input.jpg examples/output/grayscale.png --grayscale
```

2. **Inverter as cores:**

```bash
python main.py examples/input.jpg examples/output/inverted.png --invert
```

3. **Aumentar o brilho em 50 pontos:**

```bash
python main.py examples/input.jpg examples/output/bright.png --brightness 50
```

4. **Aplicar um blur de força 5:**

```bash
python main.py examples/input.jpg examples/output/blurred.png --blur 5
```

5. **Combinar operações (blur e depois inversão):**

```bash
python main.py example/input.jpg examples/output/blurred_iverted.png ==blur 3 --invert
```

## **Como conbribuir**

Contribuições são bem-vindas! Para adicionar um novo filtro:

1. **Crie a função de processamento:** Adicione sua função no arquivo `imagecraft/core.py`. Ela deve receber um array NumPy e retornar um array NumPy.
2. **Adicione o argumento na CLI:** Edite o arquivo `main.py` para adicionar um novo argumento no `argparse`.
3. **Invoque a função:** No `main.py`, chame sua nova função quando o argumento correspondente for passado.
4. **Documente:** Adicione a nova funcionalidade e exemplos de uso neste README.
5. Envie um **Pull Request**.
