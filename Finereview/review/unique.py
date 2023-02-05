import os
import ast

def unique_variables(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            with open(os.path.join(directory, filename), "r") as f:
                code = f.read()
                try:
                    tree = ast.parse(code)
                    variables = set()
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                            variables.add(node.id)
                    print("Unique variables in {}: {}".format(filename, ", ".join(variables)))
                except SyntaxError:
                    continue

unique_variables("D:/Hacathon/permisson less/finyash/Finereview/review/codes")