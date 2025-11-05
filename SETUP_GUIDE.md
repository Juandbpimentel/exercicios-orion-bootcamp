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

Para enviar as branches criadas para o repositório remoto, execute:

```bash
git push origin dev stage production
```

Ou use o script de configuração:

```bash
./setup-branches.sh
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
