from antlr4 import *

from Parser.c_srcParser import c_srcParser
from Parser.c_srcVisitor import c_srcVisitor
from Parser.c_srcLexer import c_srcLexer
import sys


class PythonCodeGenerator(c_srcVisitor):
    def __init__(self):
        super().__init__()

        # python代码的缩进，用来控制python结构
        self.indentation = 0
        self.python_code = ""

    def increase_indentation(self):
        self.indentation += 1

    def decrease_indentation(self):
        self.indentation -= 1

    def add_line(self, line):
        self.python_code += "    " * self.indentation + line + "\n"

    def get_type(self, node):
        if node.getChild(0).getText() == 'struct':
            return node.getChild(1).getText()
        else:
            return node.getText()

    # 以下是对 c_srcVisitor 中的各个方法的重写，实现具体的代码生成逻辑

    def visitProg(self, ctx:c_srcParser.ProgContext):  # ok
        self.add_line('from utils import *')
        # 处理整个程序的根节点
        for child in ctx.getChildren():
            self.visit(child)
        self.indentation = 0
        self.add_line('main()')
        return self.python_code

    # def visitInclude(self, ctx:c_srcParser.IncludeContext):  # ok
    #     # 处理 include 语句
    #     self.add_line(f"#include {ctx.getText()}")

    def visitInitSentence(self, ctx:c_srcParser.InitSentenceContext):  # ok
        # 处理初始化语句
        self.visit(ctx.getChild(0))

    def visitDefSentence(self, ctx: c_srcParser.DefSentenceContext):  # ok
        # 处理定义语句
        self.visit(ctx.getChild(0))

    def visitStructDef(self, ctx:c_srcParser.StructDefContext):  # ok
        # 处理结构体定义
        struct_name = ctx.getChild(0).getChild(1).getText()
        self.add_line(f"class {struct_name}:")
        self.increase_indentation()
        self.visit(ctx.structParams())
        self.decrease_indentation()

    # Visit a parse tree produced by c_srcParser#structParams.
    def visitStructParams(self, ctx: c_srcParser.StructParamsContext):  # ok
        for child in ctx.getChildren():
            self.visit(child)

    def visitSParam(self, ctx:c_srcParser.SParamContext):  # ok
        # 处理结构体参数
        # if isinstance(ctx.getChild(0), c_srcParser.TypeNameContext):
        #     param_type = ctx.getChild(0).getText()
        # else:
        #     param_type = ctx.getChild(0).getChild(1).getText()
        param_type = self.get_type(ctx.getChild(0))
        for i in range(1, len(ctx.children), 2):
            param_name = ctx.getChild(i).getText()
            self.add_line(f"{param_name}: {param_type}")

    def visitFuncDef(self, ctx:c_srcParser.FuncDefContext):  # ok
        # 处理函数定义
        return_type = self.get_type(ctx.getChild(0))
        if return_type == 'void':
            return_type = None
        elif return_type == 'double':
            return_type = 'float'
        func_name = ctx.getChild(1).getText()
        # params = [f'{param.getChild(1).getText()}: {param.getChild(0).getText()}' for param in ctx.params().getChildren() if param.getText() != ',']
        params = [f'{param.getChild(1).getText()}' for param in ctx.params().getChildren() if param.getText() != ',']
        self.add_line(f"def {func_name}({', '.join(params)}) -> {return_type}:")
        self.increase_indentation()
        self.visit(ctx.funcBody())
        self.decrease_indentation()

    # def visitParams(self, ctx:c_srcParser.ParamsContext):  # ok
    #     # 处理函数参数列表
    #     params = []
    #     for param_ctx in ctx.children:
    #         if isinstance(param_ctx, c_srcParser.ParamContext):
    #             param = self.visit(param_ctx)
    #             params.append(param)
    #     return ", ".join(params)

    # def visitParam(self, ctx:c_srcParser.ParamContext):  # ok
    #     # 处理函数参数
    #     param_type = ctx.typeName.text
    #     param_name = ctx.varName.text
    #     return f"{param_name}: {param_type}"

    def visitFuncBody(self, ctx:c_srcParser.FuncBodyContext):  # ok
        # 处理函数体
        self.visit(ctx.mainBody())
        self.visit(ctx.returnSentence())

    # Visit a parse tree produced by c_srcParser#mainBody.
    def visitMainBody(self, ctx: c_srcParser.MainBodyContext):  # ok
        # mainBody : (block | func)*;
        for child in ctx.getChildren():
            if isinstance(child, c_srcParser.FuncContext):
                self.add_line(self.visit(child))
            else:
                self.visit(child)

    # Visit a parse tree produced by c_srcParser#block.
    def visitBlock(self, ctx: c_srcParser.BlockContext):  # ok
        for child in ctx.getChildren():
            self.visit(child)

    # Visit a parse tree produced by c_srcParser#normalInit.
    def visitNormalInit(self, ctx: c_srcParser.NormalInitContext):  # ok
        type = ctx.getChild(0).getText()
        i = 1
        while i < len(ctx.children):
            node = ctx.getChild(i)
            if ctx.getChild(i+1).getText() == '=':
                self.add_line(f'{node.getText()} = {self.visit(ctx.getChild(i+2))}')
                i = i + 4
            else:
                self.add_line(f'{node.getText()}: {type}')
                i = i + 2

    # Visit a parse tree produced by c_srcParser#arrayInit.
    def visitArrayInit(self, ctx: c_srcParser.ArrayInitContext):  # ok
        # arrayInit : typeName varName '[' intType ']'';';
        if ctx.getChild(0).getText() == 'char':  # 是字符串
            self.add_line(f'{ctx.getChild(1).getText()} = [0 for _ in range({ctx.getChild(3).getText()})]')
        else:
            self.add_line(f'{ctx.getChild(1).getText()} = [None for _ in range({ctx.getChild(3).getText()})]')

    # Visit a parse tree produced by c_srcParser#structInit.
    def visitStructInit(self, ctx: c_srcParser.StructInitContext):  # ok
        if isinstance(ctx.getChild(1), c_srcParser.ArrayNameContext):
            self.add_line(f'{ctx.getChild(1).getChild(0).getText()} = [{ctx.getChild(0).getChild(1).getText()}() for _ in range({ctx.getChild(1).getChild(2).getText()})]')
        else:
            self.add_line(f'{ctx.getChild(1).getText()} = {ctx.getChild(0).getChild(1).getText()}()')

    # Visit a parse tree produced by c_srcParser#assignSentence.
    def visitAssignSentence(self, ctx: c_srcParser.AssignSentenceContext):  # ok
        self.add_line(f'{ctx.getChild(0).getText()} = {self.visit(ctx.getChild(2))}')

    # Visit a parse tree produced by c_srcParser#forBlock.
    def visitForBlock(self, ctx: c_srcParser.ForBlockContext):  # ok
        # forBlock : 'for' '(' firstBlock ';' condition ';' secondBlock ')' ('{' mainBody '}' | ';');
        self.visit(ctx.getChild(2))  # firstBlock
        self.add_line(f'while {self.visit(ctx.getChild(4))}:')
        self.increase_indentation()
        if ctx.getChild(9):
            self.visit(ctx.getChild(9))
        self.visit(ctx.getChild(6))
        self.decrease_indentation()

    # Visit a parse tree produced by c_srcParser#firstBlock.
    def visitFirstBlock(self, ctx: c_srcParser.FirstBlockContext):  # ok
        # firstBlock : varName '=' expression (',' firstBlock)? | ;
        if ctx.children:
            self.add_line(f'{ctx.getChild(0).getText()} = {self.visit(ctx.getChild(2))}')
            if isinstance(ctx.getChild(4), c_srcParser.FirstBlockContext):
                self.visit(ctx.getChild(4))



    # Visit a parse tree produced by c_srcParser#secondBlock.
    def visitSecondBlock(self, ctx: c_srcParser.SecondBlockContext):  # ok
        # secondBlock : varName '=' expression (',' secondBlock)? | ;
        if ctx.children:
            self.add_line(f'{ctx.getChild(0).getText()}={self.visit(ctx.getChild(2))}')
            if isinstance(ctx.getChild(4), c_srcParser.SecondBlockContext):
                self.visit(ctx.getChild(4))

    # Visit a parse tree produced by c_srcParser#ifBlocks.
    def visitIfBlocks(self, ctx: c_srcParser.IfBlocksContext):  # ok
        for i in range(len(ctx.children)):
            self.visit(ctx.getChild(i))

    # Visit a parse tree produced by c_srcParser#ifBlock.  ifBlock : 'if' '(' condition ')' '{' mainBody '}';
    def visitIfBlock(self, ctx: c_srcParser.IfBlockContext):   # ok
        self.add_line(f'if {self.visit(ctx.getChild(2))}:')
        self.increase_indentation()
        self.visit(ctx.getChild(5))
        self.decrease_indentation()

    # Visit a parse tree produced by c_srcParser#elifBlock.
    def visitElifBlock(self, ctx: c_srcParser.ElifBlockContext):  # ok
        # elifBlock : 'else' 'if' '(' condition ')' '{' mainBody '}';
        self.add_line(f'elif {self.visit(ctx.getChild(3))}:')
        self.increase_indentation()
        self.visit(ctx.getChild(6))
        self.decrease_indentation()

    # Visit a parse tree produced by c_srcParser#elseBlock.
    def visitElseBlock(self, ctx: c_srcParser.ElseBlockContext):  # ok
        # elseBlock : 'else' '{' mainBody '}';
        self.add_line(f'else:')
        self.increase_indentation()
        self.visit(ctx.getChild(2))
        self.decrease_indentation()

    # Visit a parse tree produced by c_srcParser#condition.
    def visitCondition(self, ctx: c_srcParser.ConditionContext):  # ok
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by c_srcParser#whileBlock.
    def visitWhileBlock(self, ctx: c_srcParser.WhileBlockContext):  # ok
        # whileBlock : 'while' '(' condition ')' '{' mainBody '}';
        self.add_line(f'while {self.visit(ctx.getChild(2))}:')
        self.increase_indentation()
        self.visit(ctx.getChild(5))
        self.decrease_indentation()

    # Visit a parse tree produced by c_srcParser#returnSentence.
    def visitReturnSentence(self, ctx: c_srcParser.ReturnSentenceContext):  # ok
        if len(ctx.children) > 2:
            self.add_line(f'return {self.visit(ctx.getChild(1))}')
        else:
            self.add_line('return')

    # Visit a parse tree produced by c_srcParser#identifier.
    def visitIdentifier(self, ctx: c_srcParser.IdentifierContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#parens.
    def visitParens(self, ctx: c_srcParser.ParensContext):  # ok
        return f'({self.visit(ctx.getChild(1))})'

    # Visit a parse tree produced by c_srcParser#string.
    def visitString(self, ctx: c_srcParser.StringContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#MulDiv.
    def visitMulDiv(self, ctx: c_srcParser.MulDivContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#AddSub.
    def visitAddSub(self, ctx: c_srcParser.AddSubContext):  # ok
        return f'{self.visit(ctx.getChild(0))} {ctx.getChild(1).getText()} {self.visit(ctx.getChild(2))}'

    # Visit a parse tree produced by c_srcParser#double.
    def visitDouble(self, ctx: c_srcParser.DoubleContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#int.
    def visitInt(self, ctx: c_srcParser.IntContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#Neg.
    def visitNeg(self, ctx: c_srcParser.NegContext):  # ok
        # op='!' expression
        return f'not {self.visit(ctx.getChild(1))}'

    # Visit a parse tree produced by c_srcParser#arrayitem.
    def visitArrayitem(self, ctx: c_srcParser.ArrayitemContext):  # ok
        # arrayItem : varName '[' expression ']';
        # return f'{self.visit(ctx.getChild(0))}[{self.visit(ctx.getChild(2))}]'
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by c_srcParser#function.
    def visitFunction(self, ctx: c_srcParser.FunctionContext):  # ok
        # func;
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by c_srcParser#AND.
    def visitAND(self, ctx: c_srcParser.ANDContext):  # ok
        # expression Logical expression
        logical = ctx.getChild(1).getText()
        if logical == '&&':
            logical = 'and'
        else:
            logical = 'or'
        return f'{self.visit(ctx.getChild(0))} {logical} {self.visit(ctx.getChild(2))}'

    # Visit a parse tree produced by c_srcParser#char.
    def visitChar(self, ctx: c_srcParser.CharContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#structmember.
    def visitStructmember(self, ctx: c_srcParser.StructmemberContext):  # ok
        # structMember : (varName | arrayItem) '.' (varName | arrayItem);
        # return f'{self.visit(ctx.getChild(0))}.{self.visit(ctx.getChild(2))}'
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by c_srcParser#Judge.
    def visitJudge(self, ctx: c_srcParser.JudgeContext):  # ok
        # expression op=('==' | '!=' | '<' | '<=' | '>' | '>=') expression
        return f'{self.visit(ctx.getChild(0))} {ctx.getChild(1).getText()} {self.visit(ctx.getChild(2))}'

    # Visit a parse tree produced by c_srcParser#structItem.
    def visitStructItem(self, ctx: c_srcParser.StructItemContext):  # ok
        # structItem : 'struct' varName;
        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by c_srcParser#arrayName.
    def visitArrayName(self, ctx: c_srcParser.ArrayNameContext):  # ok
        # arrayName : varName '[' intType ']';
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#structMember.
    def visitStructMember(self, ctx: c_srcParser.StructMemberContext):  # ok
        return f'{self.visit(ctx.getChild(0))}.{self.visit(ctx.getChild(2))}'

    # Visit a parse tree produced by c_srcParser#voidType.
    # def visitVoidType(self, ctx: c_srcParser.VoidTypeContext):  # ok
    #     return self.visitChildren(ctx)

    # Visit a parse tree produced by c_srcParser#typeName.
    # def visitTypeName(self, ctx: c_srcParser.TypeNameContext):  # ok
    #     return self.visitChildren(ctx)

    # Visit a parse tree produced by c_srcParser#arrayItem.
    def visitArrayItem(self, ctx: c_srcParser.ArrayItemContext):  # ok
        return f'{self.visit(ctx.getChild(0))}[{self.visit(ctx.getChild(2))}]'

    # Visit a parse tree produced by c_srcParser#func.
    def visitFunc(self, ctx: c_srcParser.FuncContext):  # ok
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by c_srcParser#scanfFunc.
    def visitScanfFunc(self, ctx: c_srcParser.ScanfFuncContext):  # ok
        # scanfFunc : 'scanf' '(' stringType (',' '&' ? (varName | arrayItem | structMember)) ')';
        number = False
        if '%d' in ctx.getChild(2).getText():
            number = True
        if ctx.getChild(4).getText() == '&':
            if number:
                return f'{self.visit(ctx.getChild(5))} = int(input())'
            else:
                return f'{self.visit(ctx.getChild(5))} = input()'
        else:
            if number:
                return f'{self.visit(ctx.getChild(4))} = int(input())'
            else:
                return f'{self.visit(ctx.getChild(4))} = input()'

    # Visit a parse tree produced by c_srcParser#getsFunc.
    def visitGetsFunc(self, ctx: c_srcParser.GetsFuncContext):  # ok
        # getsFunc : 'gets' '(' varName ')';
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#atoiFunc.
    def visitAtoiFunc(self, ctx: c_srcParser.AtoiFuncContext):  # ok
        # atoiFunc : 'atoi' '(' expression ')';
        return f'atoi({self.visit(ctx.getChild(2))})'

    # Visit a parse tree produced by c_srcParser#printfFunc.
    def visitPrintfFunc(self, ctx: c_srcParser.PrintfFuncContext):  # ok
        # printfFunc : 'printf' '(' (stringType | varName) (',' expression)* ')';
        ret = f'print({self.visit(ctx.getChild(2))}'
        if isinstance(ctx.getChild(2), c_srcParser.StringTypeContext):
            i = 3
            values = []
            while ctx.getChild(i).getText() == ',':
                # ret += f', {self.visit(ctx.getChild(i + 1))}'
                values.append(self.visit(ctx.getChild(i + 1)))
                i = i + 2
            values = [str(item) for item in values]
            values = ','.join(values)
            ret += f' % ({values})'
        return ret + ', end=\'\')'

    # Visit a parse tree produced by c_srcParser#selfDefinedFunc.
    def visitSelfDefinedFunc(self, ctx: c_srcParser.SelfDefinedFuncContext):  # ok
        # selfDefinedFunc : varName '(' ((expression) (',' (expression))*)? ')';
        ret = f'{ctx.getChild(0).getText()}('
        if len(ctx.children) > 3:
            ret += self.visit(ctx.getChild(2))
            i = 3
            while ctx.getChild(i).getText() == ',':
                ret += f', {self.visit(ctx.getChild(i+1))}'
                i = i + 2
        return ret+')'

    # Visit a parse tree produced by c_srcParser#strlenFunc.
    def visitStrlenFunc(self, ctx: c_srcParser.StrlenFuncContext):  # ok
        # strlenFunc : 'strlen' '(' varName ')';
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#varName.
    def visitVarName(self, ctx: c_srcParser.VarNameContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#intType.
    def visitIntType(self, ctx: c_srcParser.IntTypeContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#doubleType.
    def visitDoubleType(self, ctx: c_srcParser.DoubleTypeContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#charType.
    def visitCharType(self, ctx: c_srcParser.CharTypeContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#stringType.
    def visitStringType(self, ctx: c_srcParser.StringTypeContext):  # ok
        return ctx.getText()

    # Visit a parse tree produced by c_srcParser#libName.
    # def visitLibName(self, ctx: c_srcParser.LibNameContext):  # ok
    #     return self.visitChildren(ctx)


if __name__ == '__main__':
    c_source_file_path = "test/biTree.c"
    if len(sys.argv) >= 2:
        c_source_file_path = sys.argv[1]


    lexer = c_srcLexer(FileStream(c_source_file_path))
    token_stream = CommonTokenStream(lexer)
    parser = c_srcParser(token_stream)
    tree = parser.prog()
    # 创建代码生成器对象
    python_code_generator = PythonCodeGenerator()

    # 遍历解析树并生成 Python 代码
    python_code = python_code_generator.visit(tree)
    file_name = c_source_file_path.replace('.c', '.py')

    # 使用open函数创建一个文件对象，模式为'w'表示写入，如果文件不存在则创建
    with open(file_name, 'w') as file:
        # 使用write方法将字符串写入文件
        file.write(python_code)

