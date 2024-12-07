# Projeto de Visão Computacional - Detecção de Animais
Projeto de Fundamentos de Inteligência Artificial (FIA) por João Omar, Lucas Acunha e Nicholas Knopp.

O projeto visa detectar animais em vídeos e saber identificá-los.

Para executar o código, é necessário criar um ambiente virtual e instalar as dependências.

## Configuração do Ambiente Virtual

### Passos para criar e ativar um ambiente virtual:

1. **Criar o ambiente virtual:**

   ```bash
   python -m venv env-trab
   ```

2. **Ativar o ambiente virtual:**

   No macOS e Linux:

   ```bash
   source ./env-trab/bin/activate
   ```

   No Windows:

   ```bash
   source ./env-trab/Scripts/activate
   ```

## Instalação de Dependências

Certifique-se de que seu ambiente virtual esteja ativado. Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Ao executar isto, serão instaladas as bibliotecas opencv-python, numpy e ultralytics.

## Desativação do Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o comando:

```bash
deactivate
```