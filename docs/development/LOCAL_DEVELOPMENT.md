\# SBAI Local Development



This document describes how to set up SBAI on a new development machine.



\## Requirements



\- Git

\- Python 3.13

\- Access to the SBAI GitHub repository



\---



\# Windows Setup



\## 1. Clone the repository



```powershell

git clone https://github.com/SBAI-STARTUP/SBAI.git

cd SBAI

```



\## 2. Switch to the implementation branch



```powershell

git fetch origin

git switch architecture-v1

```



\## 3. Create a virtual environment



```powershell

python -m venv .venv

```



\## 4. Activate the environment



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



\## 5. Upgrade pip



```powershell

python -m pip install --upgrade pip

```



\## 6. Install SBAI and development dependencies



```powershell

python -m pip install -e ".\[dev]"

```



\## 7. Run tests



```powershell

python -m pytest -q

```



\## 8. Run the API Gateway



```powershell

python -m uvicorn sbai\_api\_gateway.main:app --reload

```



Open:



\- http://127.0.0.1:8000/health

\- http://127.0.0.1:8000/docs



\---



\# Termux Setup



\## 1. Go to the repository



```bash

cd /storage/emulated/0/SBAI

```



\## 2. Activate the SBAI environment



```bash

source \~/.venvs/sbai/bin/activate

```



\## 3. Update the repository



```bash

git pull origin architecture-v1

```



\## 4. Install the project and development dependencies



```bash

python -m pip install -e ".\[dev]"

```



\## 5. Run tests



```bash

python -m pytest -q

```



\## 6. Run the API Gateway



```bash

cd services/api-gateway

python -m uvicorn sbai\_api\_gateway.main:app --host 127.0.0.1 --port 8000

```



\---



\# Daily Development



\## Windows



```powershell

cd SBAI

.\\.venv\\Scripts\\Activate.ps1

git pull origin architecture-v1

python -m pytest -q

```



\## Termux



```bash

cd /storage/emulated/0/SBAI

source \~/.venvs/sbai/bin/activate

git pull origin architecture-v1

python -m pytest -q

```# SBAI Local Development



This document describes how to set up SBAI on a new development machine.



\## Requirements



\- Git

\- Python 3.13

\- Access to the SBAI GitHub repository



\---



\# Windows Setup



\## 1. Clone the repository



```powershell

git clone https://github.com/SBAI-STARTUP/SBAI.git

cd SBAI

```



\## 2. Switch to the implementation branch



```powershell

git fetch origin

git switch architecture-v1

```



\## 3. Create a virtual environment



```powershell

python -m venv .venv

```



\## 4. Activate the environment



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



\## 5. Upgrade pip



```powershell

python -m pip install --upgrade pip

```



\## 6. Install SBAI and development dependencies



```powershell

python -m pip install -e ".\[dev]"

```



\## 7. Run tests



```powershell

python -m pytest -q

```



\## 8. Run the API Gateway



```powershell

python -m uvicorn sbai\_api\_gateway.main:app --reload

```



Open:



\- http://127.0.0.1:8000/health

\- http://127.0.0.1:8000/docs



\---



\# Termux Setup



\## 1. Go to the repository



```bash

cd /storage/emulated/0/SBAI

```



\## 2. Activate the SBAI environment



```bash

source \~/.venvs/sbai/bin/activate

```



\## 3. Update the repository



```bash

git pull origin architecture-v1

```



\## 4. Install the project and development dependencies



```bash

python -m pip install -e ".\[dev]"

```



\## 5. Run tests



```bash

python -m pytest -q

```



\## 6. Run the API Gateway



```bash

cd services/api-gateway

python -m uvicorn sbai\_api\_gateway.main:app --host 127.0.0.1 --port 8000

```



\---



\# Daily Development



\## Windows



```powershell

cd SBAI

.\\.venv\\Scripts\\Activate.ps1

git pull origin architecture-v1

python -m pytest -q

```



\## Termux



```bash

cd /storage/emulated/0/SBAI

source \~/.venvs/sbai/bin/activate

git pull origin architecture-v1

python -m pytest -q

```

