import math

class Node:
    def __init__(self, value, min_max_node):
        self.value = value

        if min_max_node == "MAX":
            self.maxNode = True
            self.minNode = False
        elif min_max_node == "MIN":
            self.minNode = True
            self.maxNode = False
        else:
            self.maxNode = False
            self.minNode = False

        self.children = []
    
    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, root):
        self.root = root
    
    def add_node(self, node, parent):
        parent.add_child(node)
    
    def print_tree(self, node, level=0):
        if not node:
            return
        
        if not node.value:
            if node.maxNode:
                print("    " * level + "MAX")
            if node.minNode:
                print("    " * level + "MIN")
        else:
            print("    " * level + str(node.value))
        for child in node.children:
            self.print_tree(child, level + 1)
    
    def get_height(self, node):

        if len(node.children) == 0:
            return 0
        
        return 1 + max(self.get_height(child) for child in node.children)
        

class Game:
    def __init__(self, tree):
        self.tree = tree
    
    def minimax(self, node, depth, maximizing):

        if depth == 0 or len(node.children) == 0:
            return node.value, node.value, node.value  # Retorna o valor atual como min, max e propagado

        if maximizing:
            max_val = -math.inf
            min_propagated = math.inf
            for child in node.children:
                val, min_prop, max_prop = self.minimax(child, depth - 1, False)
                max_val = max(max_val, val)
                min_propagated = min(min_propagated, min_prop)
            print("     " * (depth - 1), "Depth:", depth, "Max propagado:", max_val)
            return max_val, min_propagated, max_val
        else:
            min_val = math.inf
            max_propagated = -math.inf
            for child in node.children:
                val, min_prop, max_prop = self.minimax(child, depth - 1, True)
                min_val = min(min_val, val)
                max_propagated = max(max_propagated, max_prop)
            print("     " * (depth - 1), "Depth:", depth, "Min propagado:", min_val)
            return min_val, min_val, max_propagated
        
        
    def minimax_with_alpha_beta(self, node, depth, alpha, beta, maximizing):
        if depth == 0 or len(node.children) == 0:
            return node.value, node.value, node.value  # Retorna o valor atual como min, max e propagado

        if maximizing:
            max_val = -math.inf
            min_propagated = math.inf
            for child in node.children:
                val, min_prop, max_prop = self.minimax_with_alpha_beta(child, depth - 1, alpha, beta, False)
                max_val = max(max_val, val)
                min_propagated = min(min_propagated, min_prop)
                alpha = max(alpha, max_val)
                if beta <= alpha:
                    print("Podando subárvore:")
                    self.tree.print_tree(child)
                    print()
                    break  # Poda alfa-beta
            return max_val, min_propagated, max_val
        else:
            min_val = math.inf
            max_propagated = -math.inf
            for child in node.children:
                val, min_prop, max_prop = self.minimax_with_alpha_beta(child, depth - 1, alpha, beta, True)
                min_val = min(min_val, val)
                max_propagated = max(max_propagated, max_prop)
                beta = min(beta, min_val)
                if beta <= alpha:
                    print("Podando subárvore:")
                    self.tree.print_tree(child)
                    print()
                    break  # Poda alfa-beta
            return min_val, min_val, max_propagated
        
    def minimax_with_alpha_beta_reverse(self, node, depth, alpha, beta, maximizing):
        if depth == 0 or len(node.children) == 0:
            return node.value, node.value, node.value  # Retorna o valor atual como min, max e propagado

        if maximizing:
            max_val = -math.inf
            min_propagated = math.inf
            for child in reversed(node.children):  # Percorre os filhos da direita para a esquerda
                val, min_prop, max_prop = self.minimax_with_alpha_beta_reverse(child, depth - 1, alpha, beta, False)
                max_val = max(max_val, val)
                min_propagated = min(min_propagated, min_prop)
                alpha = max(alpha, max_val)
                if beta <= alpha:
                    print("Podando subárvore:")
                    self.tree.print_tree(child)
                    print()
                    break  # Poda alfa-beta
            return max_val, min_propagated, max_val
        else:
            min_val = math.inf
            max_propagated = -math.inf
            for child in reversed(node.children):  # Percorre os filhos da direita para a esquerda
                val, min_prop, max_prop = self.minimax_with_alpha_beta_reverse(child, depth - 1, alpha, beta, True)
                min_val = min(min_val, val)
                max_propagated = max(max_propagated, max_prop)
                beta = min(beta, min_val)
                if beta <= alpha:
                    print("Podando subárvore:")
                    self.tree.print_tree(child)
                    print()
                    break  # Poda alfa-beta
            return min_val, min_val, max_propagated



def build_tree(value, max_height):
    if value != 0:
        node_value = None
    root = Node(node_value, "MAX")

    build_tree_recursive(root, value, max_height, "MAX")
    return root

def build_tree_recursive(node, current_value, height, min_max_node):
    if height == 0:
        return
    
    child_values = [current_value - 1, current_value - 2, current_value - 3]

    for value in child_values:
        if value > 0:
            if min_max_node == "MAX":
                child = Node(None, "MIN")
                node.add_child(child)
                build_tree_recursive(child, value, height - 1, "MIN")
            elif min_max_node == "MIN":
                child = Node(None, "MAX")
                node.add_child(child)
                build_tree_recursive(child, value, height - 1, "MAX")
        elif value == 0: # o jogador que retirar o ultimo palito perde o jogo
            if min_max_node == "MAX": # se o jogador atual for o MAX, então o MIN ganhou
                child = Node(-1, " ") # se o MIN ganhou, então o valor do nó é -1
                node.add_child(child)
            elif min_max_node == "MIN": # se o jogador atual for o MIN, então o MAX ganhou
                child = Node(1, " ") # se o MAX ganhou, então o valor do nó é 1
                node.add_child(child)
                



value = 5
max_height = value
root = build_tree(value, max_height)
tree = Tree(root)
tree.print_tree(root)
print("\n")

game = Game(tree)

print("------------------   MINIMAX   ------------------")
print("\n")
val, min_prop, max_prop = game.minimax(root, tree.get_height(root), True)
print("\n")
print("Valor final:", val)
print("Min propagado:", min_prop)
print("Max propagado:", max_prop)
print("\n")


print("-----------   MINIMAX COM PODA ALFA-BETA DA ESQUERDA PARA DIREITA   -----------")
print("\n")
val, min_prop, max_prop = game.minimax_with_alpha_beta(root, tree.get_height(root), -math.inf, math.inf, True)
print("\n")
print("Valor final com poda alfa-beta:", val)
print("Min propagado com poda alfa-beta:", min_prop)
print("Max propagado com poda alfa-beta:", max_prop)
print("\n")

print("-----------   MINIMAX COM PODA ALFA-BETA DA DIREITA PARA ESQUERDA   -----------")
print("\n")
val, min_prop, max_prop = game.minimax_with_alpha_beta_reverse(root, tree.get_height(root), -math.inf, math.inf, True)
print("\n")
print("Valor final com poda alfa-beta:", val)
print("Min propagado com poda alfa-beta:", min_prop)
print("Max propagado com poda alfa-beta:", max_prop)
print("\n")



