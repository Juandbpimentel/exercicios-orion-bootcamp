#!/bin/bash
# Script para configurar as branches do repositório
# Este script cria e envia as branches auxiliares para o repositório remoto

set -e

echo "Configurando branches do repositório..."

# Certifique-se de que estamos no diretório correto
cd "$(dirname "$0")"

# Verificar se a branch main existe
if ! git show-ref --verify --quiet refs/heads/main; then
    echo "Criando branch main localmente..."
    git fetch origin main:main 2>/dev/null || git branch main
fi

# Criar branches auxiliares a partir de main
echo "Criando branches auxiliares..."
git branch dev main 2>/dev/null || echo "Branch dev já existe"
git branch stage main 2>/dev/null || echo "Branch stage já existe"
git branch production main 2>/dev/null || echo "Branch production já existe"

# Listar branches criadas
echo ""
echo "Branches locais:"
git branch

# Enviar branches para o remoto
echo ""
echo "Enviando branches para o repositório remoto..."
git push origin main dev stage production

echo ""
echo "✓ Configuração de branches concluída!"
echo ""
echo "Branches disponíveis:"
echo "  - main (principal)"
echo "  - dev (desenvolvimento)"
echo "  - stage (homologação)"
echo "  - production (produção)"
