# Guia de Configuração das Branches

## Objetivo
Criar uma estrutura de branches para o repositório com:
- **main** - Branch principal (já existe)
- **dev** - Branch de desenvolvimento
- **stage** - Branch de homologação
- **production** - Branch de produção

## Status Atual

### ✓ Branches Criadas Localmente
As seguintes branches foram criadas localmente a partir da branch `main`:
- `dev`
- `stage`
- `production`

### Próximo Passo: Enviar para o Remoto

Existem três formas de criar as branches no repositório remoto:

#### Opção 1: GitHub Actions (Recomendado)
1. Vá para a aba "Actions" no GitHub
2. Selecione o workflow "Setup Repository Branches"
3. Clique em "Run workflow"
4. Digite "yes" no campo de confirmação
5. Clique em "Run workflow"

#### Opção 2: Script de Configuração
Execute o script fornecido:
```bash
./setup-branches.sh
```

#### Opção 3: Comandos Git Manuais
```bash
git push origin dev stage production
```

## Verificação

Para verificar as branches locais:
```bash
git branch
```

Para verificar as branches remotas:
```bash
git branch -r
```

## Estrutura Final

Após o push, o repositório terá a seguinte estrutura de branches:

```
main (principal)
├── dev (desenvolvimento)
├── stage (homologação)
└── production (produção)
```

Todas as branches auxiliares são baseadas na branch `main`.
