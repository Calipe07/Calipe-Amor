# Código Python para gerar a página HTML
html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mensagem Carinhosa</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f7f7f7;
            padding: 20px;
        }
        .container {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        img {
            width: 80%;
            max-width: 400px;
            border-radius: 10px;
        }
        h1 {
            color: #FF6347;
            font-size: 2rem;
        }
        p {
            font-size: 1.2rem;
            color: #333;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Mensagem para Você</h1>
        <img src="caminho-da-imagem/Dia-da-Neve.jpeg" alt="Nossa foto">
        <p>Minha amada, sempre estarei ao seu lado. Te amo muito e estou feliz com cada momento que passamos juntos. ❤️</p>
    </div>

</body>
</html>
"""

# Salvar o HTML gerado
with open("mensagem_carinhosa.html", "w") as file:
    file.write(html_content)

print("Arquivo HTML gerado com sucesso!")
