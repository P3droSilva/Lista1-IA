import math

class Node:
    def __init__(self, value, min_max_node):
        self.value = value

        if min_max_node == "MAX":
            self.maxNode = True
            self.minNode = False

        if min_max_node == "MIN":
            self.minNode = True
            self.maxNode = False

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
                print("  " * level + "MAX")
            if node.minNode:
                print("  " * level + "MIN")
        else:
            print("  " * level + str(node.value))
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


        
# Function to build the tree dynamically
def build_tree(values, index=0):
    if index >= len(values):
        return None
    node = Node(values[index][0], values[index][1])
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    left_child = build_tree(values, left_child_index)
    right_child = build_tree(values, right_child_index)
    if left_child:
        node.children.append(left_child)

    if right_child:
        node.children.append(right_child)

    return node


values = [[None, "MAX"], [None, "MIN"], [None, "MIN"], [None, "MAX"], [None, "MAX"], [None, "MAX"], [None, "MAX"], [None, "MIN"], [None, "MIN"], [None, "MIN"], [None, "MIN"], [None, "MIN"], [None, "MIN"], [None, "MIN"], [None, "MIN"], [20, " "], [33, " "], [-45, " "], [-31, " "], [24, " "], [25, " "], [-10, " "], [20, " "], [40, " "], [-25, " "], [18, " "], [-42, " "], [24, " "], [-19, " "], [36, " "], [-41, " "]]
root = build_tree(values)
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



