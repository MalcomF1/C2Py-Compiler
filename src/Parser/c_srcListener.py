# Generated from c_src.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .c_srcParser import c_srcParser
else:
    from c_srcParser import c_srcParser

# This class defines a complete listener for a parse tree produced by c_srcParser.
class c_srcListener(ParseTreeListener):

    # Enter a parse tree produced by c_srcParser#prog.
    def enterProg(self, ctx:c_srcParser.ProgContext):
        pass

    # Exit a parse tree produced by c_srcParser#prog.
    def exitProg(self, ctx:c_srcParser.ProgContext):
        pass


    # Enter a parse tree produced by c_srcParser#include.
    def enterInclude(self, ctx:c_srcParser.IncludeContext):
        pass

    # Exit a parse tree produced by c_srcParser#include.
    def exitInclude(self, ctx:c_srcParser.IncludeContext):
        pass


    # Enter a parse tree produced by c_srcParser#initSentence.
    def enterInitSentence(self, ctx:c_srcParser.InitSentenceContext):
        pass

    # Exit a parse tree produced by c_srcParser#initSentence.
    def exitInitSentence(self, ctx:c_srcParser.InitSentenceContext):
        pass


    # Enter a parse tree produced by c_srcParser#defSentence.
    def enterDefSentence(self, ctx:c_srcParser.DefSentenceContext):
        pass

    # Exit a parse tree produced by c_srcParser#defSentence.
    def exitDefSentence(self, ctx:c_srcParser.DefSentenceContext):
        pass


    # Enter a parse tree produced by c_srcParser#structDef.
    def enterStructDef(self, ctx:c_srcParser.StructDefContext):
        pass

    # Exit a parse tree produced by c_srcParser#structDef.
    def exitStructDef(self, ctx:c_srcParser.StructDefContext):
        pass


    # Enter a parse tree produced by c_srcParser#structParams.
    def enterStructParams(self, ctx:c_srcParser.StructParamsContext):
        pass

    # Exit a parse tree produced by c_srcParser#structParams.
    def exitStructParams(self, ctx:c_srcParser.StructParamsContext):
        pass


    # Enter a parse tree produced by c_srcParser#sParam.
    def enterSParam(self, ctx:c_srcParser.SParamContext):
        pass

    # Exit a parse tree produced by c_srcParser#sParam.
    def exitSParam(self, ctx:c_srcParser.SParamContext):
        pass


    # Enter a parse tree produced by c_srcParser#funcDef.
    def enterFuncDef(self, ctx:c_srcParser.FuncDefContext):
        pass

    # Exit a parse tree produced by c_srcParser#funcDef.
    def exitFuncDef(self, ctx:c_srcParser.FuncDefContext):
        pass


    # Enter a parse tree produced by c_srcParser#params.
    def enterParams(self, ctx:c_srcParser.ParamsContext):
        pass

    # Exit a parse tree produced by c_srcParser#params.
    def exitParams(self, ctx:c_srcParser.ParamsContext):
        pass


    # Enter a parse tree produced by c_srcParser#param.
    def enterParam(self, ctx:c_srcParser.ParamContext):
        pass

    # Exit a parse tree produced by c_srcParser#param.
    def exitParam(self, ctx:c_srcParser.ParamContext):
        pass


    # Enter a parse tree produced by c_srcParser#funcBody.
    def enterFuncBody(self, ctx:c_srcParser.FuncBodyContext):
        pass

    # Exit a parse tree produced by c_srcParser#funcBody.
    def exitFuncBody(self, ctx:c_srcParser.FuncBodyContext):
        pass


    # Enter a parse tree produced by c_srcParser#mainBody.
    def enterMainBody(self, ctx:c_srcParser.MainBodyContext):
        pass

    # Exit a parse tree produced by c_srcParser#mainBody.
    def exitMainBody(self, ctx:c_srcParser.MainBodyContext):
        pass


    # Enter a parse tree produced by c_srcParser#block.
    def enterBlock(self, ctx:c_srcParser.BlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#block.
    def exitBlock(self, ctx:c_srcParser.BlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#normalInit.
    def enterNormalInit(self, ctx:c_srcParser.NormalInitContext):
        pass

    # Exit a parse tree produced by c_srcParser#normalInit.
    def exitNormalInit(self, ctx:c_srcParser.NormalInitContext):
        pass


    # Enter a parse tree produced by c_srcParser#arrayInit.
    def enterArrayInit(self, ctx:c_srcParser.ArrayInitContext):
        pass

    # Exit a parse tree produced by c_srcParser#arrayInit.
    def exitArrayInit(self, ctx:c_srcParser.ArrayInitContext):
        pass


    # Enter a parse tree produced by c_srcParser#structInit.
    def enterStructInit(self, ctx:c_srcParser.StructInitContext):
        pass

    # Exit a parse tree produced by c_srcParser#structInit.
    def exitStructInit(self, ctx:c_srcParser.StructInitContext):
        pass


    # Enter a parse tree produced by c_srcParser#assignSentence.
    def enterAssignSentence(self, ctx:c_srcParser.AssignSentenceContext):
        pass

    # Exit a parse tree produced by c_srcParser#assignSentence.
    def exitAssignSentence(self, ctx:c_srcParser.AssignSentenceContext):
        pass


    # Enter a parse tree produced by c_srcParser#forBlock.
    def enterForBlock(self, ctx:c_srcParser.ForBlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#forBlock.
    def exitForBlock(self, ctx:c_srcParser.ForBlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#firstBlock.
    def enterFirstBlock(self, ctx:c_srcParser.FirstBlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#firstBlock.
    def exitFirstBlock(self, ctx:c_srcParser.FirstBlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#secondBlock.
    def enterSecondBlock(self, ctx:c_srcParser.SecondBlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#secondBlock.
    def exitSecondBlock(self, ctx:c_srcParser.SecondBlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#ifBlocks.
    def enterIfBlocks(self, ctx:c_srcParser.IfBlocksContext):
        pass

    # Exit a parse tree produced by c_srcParser#ifBlocks.
    def exitIfBlocks(self, ctx:c_srcParser.IfBlocksContext):
        pass


    # Enter a parse tree produced by c_srcParser#ifBlock.
    def enterIfBlock(self, ctx:c_srcParser.IfBlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#ifBlock.
    def exitIfBlock(self, ctx:c_srcParser.IfBlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#elifBlock.
    def enterElifBlock(self, ctx:c_srcParser.ElifBlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#elifBlock.
    def exitElifBlock(self, ctx:c_srcParser.ElifBlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#elseBlock.
    def enterElseBlock(self, ctx:c_srcParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#elseBlock.
    def exitElseBlock(self, ctx:c_srcParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#condition.
    def enterCondition(self, ctx:c_srcParser.ConditionContext):
        pass

    # Exit a parse tree produced by c_srcParser#condition.
    def exitCondition(self, ctx:c_srcParser.ConditionContext):
        pass


    # Enter a parse tree produced by c_srcParser#whileBlock.
    def enterWhileBlock(self, ctx:c_srcParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by c_srcParser#whileBlock.
    def exitWhileBlock(self, ctx:c_srcParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by c_srcParser#returnSentence.
    def enterReturnSentence(self, ctx:c_srcParser.ReturnSentenceContext):
        pass

    # Exit a parse tree produced by c_srcParser#returnSentence.
    def exitReturnSentence(self, ctx:c_srcParser.ReturnSentenceContext):
        pass


    # Enter a parse tree produced by c_srcParser#identifier.
    def enterIdentifier(self, ctx:c_srcParser.IdentifierContext):
        pass

    # Exit a parse tree produced by c_srcParser#identifier.
    def exitIdentifier(self, ctx:c_srcParser.IdentifierContext):
        pass


    # Enter a parse tree produced by c_srcParser#parens.
    def enterParens(self, ctx:c_srcParser.ParensContext):
        pass

    # Exit a parse tree produced by c_srcParser#parens.
    def exitParens(self, ctx:c_srcParser.ParensContext):
        pass


    # Enter a parse tree produced by c_srcParser#string.
    def enterString(self, ctx:c_srcParser.StringContext):
        pass

    # Exit a parse tree produced by c_srcParser#string.
    def exitString(self, ctx:c_srcParser.StringContext):
        pass


    # Enter a parse tree produced by c_srcParser#MulDiv.
    def enterMulDiv(self, ctx:c_srcParser.MulDivContext):
        pass

    # Exit a parse tree produced by c_srcParser#MulDiv.
    def exitMulDiv(self, ctx:c_srcParser.MulDivContext):
        pass


    # Enter a parse tree produced by c_srcParser#AddSub.
    def enterAddSub(self, ctx:c_srcParser.AddSubContext):
        pass

    # Exit a parse tree produced by c_srcParser#AddSub.
    def exitAddSub(self, ctx:c_srcParser.AddSubContext):
        pass


    # Enter a parse tree produced by c_srcParser#double.
    def enterDouble(self, ctx:c_srcParser.DoubleContext):
        pass

    # Exit a parse tree produced by c_srcParser#double.
    def exitDouble(self, ctx:c_srcParser.DoubleContext):
        pass


    # Enter a parse tree produced by c_srcParser#int.
    def enterInt(self, ctx:c_srcParser.IntContext):
        pass

    # Exit a parse tree produced by c_srcParser#int.
    def exitInt(self, ctx:c_srcParser.IntContext):
        pass


    # Enter a parse tree produced by c_srcParser#Neg.
    def enterNeg(self, ctx:c_srcParser.NegContext):
        pass

    # Exit a parse tree produced by c_srcParser#Neg.
    def exitNeg(self, ctx:c_srcParser.NegContext):
        pass


    # Enter a parse tree produced by c_srcParser#arrayitem.
    def enterArrayitem(self, ctx:c_srcParser.ArrayitemContext):
        pass

    # Exit a parse tree produced by c_srcParser#arrayitem.
    def exitArrayitem(self, ctx:c_srcParser.ArrayitemContext):
        pass


    # Enter a parse tree produced by c_srcParser#function.
    def enterFunction(self, ctx:c_srcParser.FunctionContext):
        pass

    # Exit a parse tree produced by c_srcParser#function.
    def exitFunction(self, ctx:c_srcParser.FunctionContext):
        pass


    # Enter a parse tree produced by c_srcParser#AND.
    def enterAND(self, ctx:c_srcParser.ANDContext):
        pass

    # Exit a parse tree produced by c_srcParser#AND.
    def exitAND(self, ctx:c_srcParser.ANDContext):
        pass


    # Enter a parse tree produced by c_srcParser#char.
    def enterChar(self, ctx:c_srcParser.CharContext):
        pass

    # Exit a parse tree produced by c_srcParser#char.
    def exitChar(self, ctx:c_srcParser.CharContext):
        pass


    # Enter a parse tree produced by c_srcParser#structmember.
    def enterStructmember(self, ctx:c_srcParser.StructmemberContext):
        pass

    # Exit a parse tree produced by c_srcParser#structmember.
    def exitStructmember(self, ctx:c_srcParser.StructmemberContext):
        pass


    # Enter a parse tree produced by c_srcParser#Judge.
    def enterJudge(self, ctx:c_srcParser.JudgeContext):
        pass

    # Exit a parse tree produced by c_srcParser#Judge.
    def exitJudge(self, ctx:c_srcParser.JudgeContext):
        pass


    # Enter a parse tree produced by c_srcParser#structItem.
    def enterStructItem(self, ctx:c_srcParser.StructItemContext):
        pass

    # Exit a parse tree produced by c_srcParser#structItem.
    def exitStructItem(self, ctx:c_srcParser.StructItemContext):
        pass


    # Enter a parse tree produced by c_srcParser#arrayName.
    def enterArrayName(self, ctx:c_srcParser.ArrayNameContext):
        pass

    # Exit a parse tree produced by c_srcParser#arrayName.
    def exitArrayName(self, ctx:c_srcParser.ArrayNameContext):
        pass


    # Enter a parse tree produced by c_srcParser#structMember.
    def enterStructMember(self, ctx:c_srcParser.StructMemberContext):
        pass

    # Exit a parse tree produced by c_srcParser#structMember.
    def exitStructMember(self, ctx:c_srcParser.StructMemberContext):
        pass


    # Enter a parse tree produced by c_srcParser#voidType.
    def enterVoidType(self, ctx:c_srcParser.VoidTypeContext):
        pass

    # Exit a parse tree produced by c_srcParser#voidType.
    def exitVoidType(self, ctx:c_srcParser.VoidTypeContext):
        pass


    # Enter a parse tree produced by c_srcParser#typeName.
    def enterTypeName(self, ctx:c_srcParser.TypeNameContext):
        pass

    # Exit a parse tree produced by c_srcParser#typeName.
    def exitTypeName(self, ctx:c_srcParser.TypeNameContext):
        pass


    # Enter a parse tree produced by c_srcParser#arrayItem.
    def enterArrayItem(self, ctx:c_srcParser.ArrayItemContext):
        pass

    # Exit a parse tree produced by c_srcParser#arrayItem.
    def exitArrayItem(self, ctx:c_srcParser.ArrayItemContext):
        pass


    # Enter a parse tree produced by c_srcParser#func.
    def enterFunc(self, ctx:c_srcParser.FuncContext):
        pass

    # Exit a parse tree produced by c_srcParser#func.
    def exitFunc(self, ctx:c_srcParser.FuncContext):
        pass


    # Enter a parse tree produced by c_srcParser#scanfFunc.
    def enterScanfFunc(self, ctx:c_srcParser.ScanfFuncContext):
        pass

    # Exit a parse tree produced by c_srcParser#scanfFunc.
    def exitScanfFunc(self, ctx:c_srcParser.ScanfFuncContext):
        pass


    # Enter a parse tree produced by c_srcParser#getsFunc.
    def enterGetsFunc(self, ctx:c_srcParser.GetsFuncContext):
        pass

    # Exit a parse tree produced by c_srcParser#getsFunc.
    def exitGetsFunc(self, ctx:c_srcParser.GetsFuncContext):
        pass


    # Enter a parse tree produced by c_srcParser#atoiFunc.
    def enterAtoiFunc(self, ctx:c_srcParser.AtoiFuncContext):
        pass

    # Exit a parse tree produced by c_srcParser#atoiFunc.
    def exitAtoiFunc(self, ctx:c_srcParser.AtoiFuncContext):
        pass


    # Enter a parse tree produced by c_srcParser#printfFunc.
    def enterPrintfFunc(self, ctx:c_srcParser.PrintfFuncContext):
        pass

    # Exit a parse tree produced by c_srcParser#printfFunc.
    def exitPrintfFunc(self, ctx:c_srcParser.PrintfFuncContext):
        pass


    # Enter a parse tree produced by c_srcParser#selfDefinedFunc.
    def enterSelfDefinedFunc(self, ctx:c_srcParser.SelfDefinedFuncContext):
        pass

    # Exit a parse tree produced by c_srcParser#selfDefinedFunc.
    def exitSelfDefinedFunc(self, ctx:c_srcParser.SelfDefinedFuncContext):
        pass


    # Enter a parse tree produced by c_srcParser#strlenFunc.
    def enterStrlenFunc(self, ctx:c_srcParser.StrlenFuncContext):
        pass

    # Exit a parse tree produced by c_srcParser#strlenFunc.
    def exitStrlenFunc(self, ctx:c_srcParser.StrlenFuncContext):
        pass


    # Enter a parse tree produced by c_srcParser#varName.
    def enterVarName(self, ctx:c_srcParser.VarNameContext):
        pass

    # Exit a parse tree produced by c_srcParser#varName.
    def exitVarName(self, ctx:c_srcParser.VarNameContext):
        pass


    # Enter a parse tree produced by c_srcParser#intType.
    def enterIntType(self, ctx:c_srcParser.IntTypeContext):
        pass

    # Exit a parse tree produced by c_srcParser#intType.
    def exitIntType(self, ctx:c_srcParser.IntTypeContext):
        pass


    # Enter a parse tree produced by c_srcParser#doubleType.
    def enterDoubleType(self, ctx:c_srcParser.DoubleTypeContext):
        pass

    # Exit a parse tree produced by c_srcParser#doubleType.
    def exitDoubleType(self, ctx:c_srcParser.DoubleTypeContext):
        pass


    # Enter a parse tree produced by c_srcParser#charType.
    def enterCharType(self, ctx:c_srcParser.CharTypeContext):
        pass

    # Exit a parse tree produced by c_srcParser#charType.
    def exitCharType(self, ctx:c_srcParser.CharTypeContext):
        pass


    # Enter a parse tree produced by c_srcParser#stringType.
    def enterStringType(self, ctx:c_srcParser.StringTypeContext):
        pass

    # Exit a parse tree produced by c_srcParser#stringType.
    def exitStringType(self, ctx:c_srcParser.StringTypeContext):
        pass


    # Enter a parse tree produced by c_srcParser#libName.
    def enterLibName(self, ctx:c_srcParser.LibNameContext):
        pass

    # Exit a parse tree produced by c_srcParser#libName.
    def exitLibName(self, ctx:c_srcParser.LibNameContext):
        pass



del c_srcParser