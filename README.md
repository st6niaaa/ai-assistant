# Speech AI Assistant

Este projeto é um assistente de voz baseado em Python que utiliza reconhecimento de fala, síntese de voz e integração com uma API de IA para gerar respostas inteligentes a partir das entradas do usuário.

## Funcionalidades

- **Reconhecimento de Fala**: Converte fala em texto utilizando a biblioteca `speech_recognition`.
- **Síntese de Voz**: Responde em português utilizando a biblioteca `pyttsx3`.
- **Integração com API de IA**: Envia entradas do usuário para uma API de geração de texto (Eden AI) e retorna respostas geradas automaticamente.
- **Comandos Especiais**:
  - `parar`: Interrompe a fala do assistente.
  - `sair` ou `fechar`: Encerra o programa.

## Requisitos

- Python 3.8+
- Bibliotecas Python:
  - `SpeechRecognition`
  - `pyttsx3`
  - `requests`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/speech-ai-assistant.git
   cd speech-ai-assistant
