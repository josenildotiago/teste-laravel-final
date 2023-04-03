import json
import os

# Função para criar a pasta "Helpers" dentro da pasta "app"
def create_helpers_folder():
    helpers_folder_path = os.path.join("app", "Helpers")
    if not os.path.exists(helpers_folder_path):
        os.makedirs(helpers_folder_path)

# Função para criar o arquivo "isActive.php" dentro da pasta "Helpers"
def create_is_active_file():
    is_active_path = os.path.join("app", "Helpers", "isActive.php")
    if not os.path.exists(is_active_path):
        with open(is_active_path, "w") as f:
            f.write("<?php\n\nfunction isActive($routeName)\n{\n    return request()->routeIs($routeName) ? 'active' : '';\n}")

# Executar as funções para criar a pasta e o arquivo necessários
create_helpers_folder()
create_is_active_file()

# Abrir o arquivo composer.json
with open('composer.json', 'r') as f:
    data = json.load(f)

# Adicionar o arquivo app/Helpers/isActive.php na seção "files" do autoload
data['autoload']['files'] = [
    "app/Helpers/isActive.php"
]

# Salvar as alterações no arquivo composer.json
with open('composer.json', 'w') as f:
    json.dump(data, f)

print("Done!")
