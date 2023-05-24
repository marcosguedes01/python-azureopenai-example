import sys
import os

# Obtém o diretório principal do projeto
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Adiciona o diretório principal ao caminho de busca de módulos do Python
sys.path.append(project_root)