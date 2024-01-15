# Generated from c_src.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .c_srcParser import c_srcParser
else:
    from c_srcParser import c_srcParser

# This class defines a complete generic visitor for a parse tree produced by c_srcParser.

class c_srcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by c_srcParser#prog.
    def visitProg(self, ctx:c_srcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#include.
    def visitInclude(self, ctx:c_srcParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#initSentence.
    def visitInitSentence(self, ctx:c_srcParser.InitSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#defSentence.
    def visitDefSentence(self, ctx:c_srcParser.DefSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#structDef.
    def visitStructDef(self, ctx:c_srcParser.StructDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#structParams.
    def visitStructParams(self, ctx:c_srcParser.StructParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#sParam.
    def visitSParam(self, ctx:c_srcParser.SParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#funcDef.
    def visitFuncDef(self, ctx:c_srcParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#params.
    def visitParams(self, ctx:c_srcParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#param.
    def visitParam(self, ctx:c_srcParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#funcBody.
    def visitFuncBody(self, ctx:c_srcParser.FuncBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#mainBody.
    def visitMainBody(self, ctx:c_srcParser.MainBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#block.
    def visitBlock(self, ctx:c_srcParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#normalInit.
    def visitNormalInit(self, ctx:c_srcParser.NormalInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#arrayInit.
    def visitArrayInit(self, ctx:c_srcParser.ArrayInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#structInit.
    def visitStructInit(self, ctx:c_srcParser.StructInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#assignSentence.
    def visitAssignSentence(self, ctx:c_srcParser.AssignSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#forBlock.
    def visitForBlock(self, ctx:c_srcParser.ForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#firstBlock.
    def visitFirstBlock(self, ctx:c_srcParser.FirstBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#secondBlock.
    def visitSecondBlock(self, ctx:c_srcParser.SecondBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#ifBlocks.
    def visitIfBlocks(self, ctx:c_srcParser.IfBlocksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#ifBlock.
    def visitIfBlock(self, ctx:c_srcParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#elifBlock.
    def visitElifBlock(self, ctx:c_srcParser.ElifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#elseBlock.
    def visitElseBlock(self, ctx:c_srcParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#condition.
    def visitCondition(self, ctx:c_srcParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#whileBlock.
    def visitWhileBlock(self, ctx:c_srcParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#returnSentence.
    def visitReturnSentence(self, ctx:c_srcParser.ReturnSentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#identifier.
    def visitIdentifier(self, ctx:c_srcParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#parens.
    def visitParens(self, ctx:c_srcParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#string.
    def visitString(self, ctx:c_srcParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#MulDiv.
    def visitMulDiv(self, ctx:c_srcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#AddSub.
    def visitAddSub(self, ctx:c_srcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#double.
    def visitDouble(self, ctx:c_srcParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#int.
    def visitInt(self, ctx:c_srcParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#Neg.
    def visitNeg(self, ctx:c_srcParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#arrayitem.
    def visitArrayitem(self, ctx:c_srcParser.ArrayitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#function.
    def visitFunction(self, ctx:c_srcParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#AND.
    def visitAND(self, ctx:c_srcParser.ANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#char.
    def visitChar(self, ctx:c_srcParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#structmember.
    def visitStructmember(self, ctx:c_srcParser.StructmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#Judge.
    def visitJudge(self, ctx:c_srcParser.JudgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#structItem.
    def visitStructItem(self, ctx:c_srcParser.StructItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#arrayName.
    def visitArrayName(self, ctx:c_srcParser.ArrayNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#structMember.
    def visitStructMember(self, ctx:c_srcParser.StructMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#voidType.
    def visitVoidType(self, ctx:c_srcParser.VoidTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#typeName.
    def visitTypeName(self, ctx:c_srcParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#arrayItem.
    def visitArrayItem(self, ctx:c_srcParser.ArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#func.
    def visitFunc(self, ctx:c_srcParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#scanfFunc.
    def visitScanfFunc(self, ctx:c_srcParser.ScanfFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#getsFunc.
    def visitGetsFunc(self, ctx:c_srcParser.GetsFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#atoiFunc.
    def visitAtoiFunc(self, ctx:c_srcParser.AtoiFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#printfFunc.
    def visitPrintfFunc(self, ctx:c_srcParser.PrintfFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#selfDefinedFunc.
    def visitSelfDefinedFunc(self, ctx:c_srcParser.SelfDefinedFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#strlenFunc.
    def visitStrlenFunc(self, ctx:c_srcParser.StrlenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#varName.
    def visitVarName(self, ctx:c_srcParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#intType.
    def visitIntType(self, ctx:c_srcParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#doubleType.
    def visitDoubleType(self, ctx:c_srcParser.DoubleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#charType.
    def visitCharType(self, ctx:c_srcParser.CharTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#stringType.
    def visitStringType(self, ctx:c_srcParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by c_srcParser#libName.
    def visitLibName(self, ctx:c_srcParser.LibNameContext):
        return self.visitChildren(ctx)



del c_srcParser