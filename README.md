# CodeScript LLM

This repository contains the large language model for CodeScript.

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. Clone the repository

```zsh
git clone git@github.com:jjpark987/codescript-llm.git
```

2. Download [Ollama](https://ollama.com/) and run server

```zsh
ollama serve
```

3. Download DeepSeek model (for more models click [here](https://ollama.com/library/deepseek-r1:7b))

```zsh
ollama run deepseek-r1:7b
```

4. Create a virtual environment if there isn't one already

```zsh
python -m venv .venv
```

5. Activate virtual environment

```zsh
source .venv/bin/activate
```

6. Install dependencies

```zsh
pip install -r requirements.txt
```
