# Captura de Imagens com Duas Câmeras (Python + OpenCV)

Este projeto em Python realiza a **captura simultânea de imagens a partir de duas webcams**, utilizando OpenCV e processamento paralelo com threads. As imagens são automaticamente rotacionadas, nomeadas com identificadores únicos e salvas em uma pasta organizada na Área de Trabalho.

> Demonstra habilidades práticas em visão computacional, manipulação de hardware, concorrência com threads e boas práticas de organização de código em Python.

---

## ✨ Destaques do Projeto

- 🔁 **Captura paralela** em tempo real utilizando `threading`.
- 🧭 **Rotação automática** das imagens (90° sentido horário).
- 💾 **Nomes únicos** para os arquivos via UUID.
- 📂 **Criação automática de diretório** (`Imagens`).
- 🎯 **Resolução de alta qualidade** (1080x720) configurada por padrão.
- ✅ Código limpo, funcional e pronto para extensões como gravação em vídeo ou reconhecimento facial.

---

## 🧪 Tecnologias Utilizadas

- **Python 3.6+**
- **OpenCV (cv2)**
- **Threading (concorrência)**
- **UUID para nomes únicos de arquivos**
- **Gerenciamento de arquivos e paths multiplataforma**

---

## ⚙️ Como Funciona

1. O script acessa as duas webcams (índices 0 e 1) utilizando o backend `CAP_DSHOW` (para compatibilidade com Windows).
2. Inicia duas **threads independentes** para cada câmera, possibilitando captura simultânea.
3. Cada frame é rotacionado em 90° no sentido horário.
4. As imagens são salvas com nomes únicos no formato `webcam<índice>_<uuid>.jpg`.
5. Os arquivos são armazenados automaticamente na pasta `Imagens`, criada pelo usuário.

---

## 🛠️ Instalação

1. Instale as dependências com `pip`:

```bash
pip install opencv-python
```

2. Execute o script:

```bash
python captura_duas_cameras.py
```

⚠️ Certifique-se de que **duas webcams** estejam conectadas ao computador.

---

## 🖥️ Exemplo de Saída

As imagens serão salvas em:

```
Área de Trabalho/
└── Imagens/
    ├── webcam0_f2b7d8a9.jpg
    └── webcam1_c1e3f4bc.jpg
```

Saída no terminal:

```
start_time camera: 0
2025-05-27 14:30:02
start_time camera: 1
2025-05-27 14:30:02
```

---

## 🧩 Personalização

- **Duração da captura** (em segundos):

```python
capture_from_two_cameras(duration=3)  # Captura por 3 segundos
```

- **Resolução da câmera**:

```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
```

---

## 🌍 Aplicações Possíveis

- 🎥 Prototipagem de sistemas de vigilância
- 🧪 Coleta de dados para treinamento de modelos de visão computacional
- 🧰 Teste de múltiplos dispositivos de captura
- 📷 Captura multiângulo de fotos para análise
- 👨‍🏫 Projetos acadêmicos e de pesquisa em visão computacional

---

## 📁 Estrutura do Projeto

```
captura_duas_cameras.py
README.md
```

As imagens são armazenadas fora da pasta do projeto, organizadamente na Área de Trabalho.

---

## 🤝 Vamos nos conectar?

Se você é um **recrutador, engenheiro ou pesquisador** buscando profissionais com experiência prática em **visão computacional, automação ou desenvolvimento de soluções com Python**, fique à vontade para entrar em contato.

Este projeto é uma amostra direta da minha capacidade de lidar com hardware real, escrever código robusto e aplicar conceitos de concorrência em projetos aplicados.

---
