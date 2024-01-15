import json
from antlr4 import *
from Parser.c_srcLexer import c_srcLexer
from Parser.c_srcParser import c_srcParser
from Parser.c_srcListener import c_srcListener
import sys

class JsonTreeListener(c_srcListener):
    def __init__(self):
        self.tree = {}

    def enterProg(self, ctx):
        self.tree["prog"] = self.visitChildren(ctx)

    def enterInclude(self, ctx):
        self.tree["include"] = ctx.getText()

    def visitTerminal(self, node):
        return node.getText()

    def visitChildren(self, node):
        result = []
        for child in node.getChildren():
            child_data = child.accept(self)
            child_name = type(child).__name__
            result.append({child_name: child_data})
        return result


def parse(input_file):
    lexer = c_srcLexer(FileStream(input_file))
    token_stream = CommonTokenStream(lexer)

    parser = c_srcParser(token_stream)
    parser.removeErrorListeners()
    # errorListener = syntaxErrorListener()
    # parser.addErrorListener(errorListener)

    tree = parser.prog()

    json_listener = JsonTreeListener()
    walker = ParseTreeWalker()
    walker.walk(json_listener, tree)

    return json_listener.tree

if __name__ == "__main__":
    # 替换为实际的C源文件路径
    c_source_code = "test/quickSort.c"
    if len(sys.argv) >= 2:
        c_source_code = sys.argv[1]

    parse_tree = parse(c_source_code)['prog']
    json_output = json.dumps(parse_tree, indent=2)
    print(json_output)
