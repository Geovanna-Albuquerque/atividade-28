
# Função para encontrar produtos com estoque zerado
def produtos_zerados(produtos, estoque):
    produtos_sem_estoque = []
    
    for produto, quantidade in zip(produtos, estoque):
        if quantidade == 0:
            produtos_sem_estoque.append(produto)
    
    return produtos_sem_estoque

# Lista de produtos e quantidades em estoque
produtos = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
estoque = [10, 0, 5, 0, 20]
# Chamando a função e exibindo os resultados
zerados = produtos_zerados(produtos, estoque)
print("Produtos com estoque zerado:", ', '.join(zerados))