from app.database.db_manipulation import db_consult
from datetime import datetime

results = db_consult()

remetente = " "
password = " "
destinatario = " " 
subject = "RELAÇÃO DE PREÇOS"

def formatar_relatorio_email(results):
    """
    Formata os resultados da consulta para o corpo do email
    """
    if not results:
        return "📭 Nenhum produto encontrado para análise."
    
    message = f"""🚀 *RELATÓRIO DOS MELHORES PREÇOS* 🚀

📊 RESUMO DA ANÁLISE
====================
"""

    for i, produto in enumerate(results, 1):
        message += f"""
📦 PRODUTO {i:02d}
├── 🏷️  Nome: {produto.product_name}
├── 🏪 Loja: {produto.store_name} 
├── 🔗 URL: {produto.product_url}
├── 💰 À VISTA: R$ {produto.menor_preco_avista:,.2f}
├── 💳 PARCELADO: R$ {produto.menor_preco_parcelado:,.2f}
└── 📅 DATA DE EXTRAÇÃO: {produto.insert_date.strftime('%d/%m/%Y às %H:%M')}
{'='*50}"""

    message += f"""

📈 ESTATÍSTICAS
├── 📦 Total de produtos analisados: {len(results)}
├── 💵 Menor preço à vista: R$ {min(p.menor_preco_avista for p in results):,.2f}
├── 💵 Maior preço à vista: R$ {max(p.menor_preco_avista for p in results):,.2f}
└── ⏰ Relatório gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}

"""

    return message

message = formatar_relatorio_email(results)
print(message)