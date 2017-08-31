import inspect
import ast


class Pygredients:

    def __init__(self, area):
        """

        :param area: Module, class, function, source_code which should be explored
                     source_code must be a string, all others must use the related python type class.
        """
        if inspect.ismodule(area):
            self.type = "module"
        elif inspect.isclass(area):
            self.type = "class"
        elif inspect.isfunction(area):
            self.type = "function"
        elif inspect.iscode(area):
            self.type = "code"
        else:
            raise UnknownAreaTypeException("Could not determine type of given area")

        self.area = area
        self._parse_area()

    def _parse_area(self):
        if self.type == "code":
            self.code = self.area
        else:
            try:
                self.code = inspect.getsource(self.area)
            except OSError:
                raise SourceCodeNotAvailableException("Could not retrieve source code for given area")

        # Maybe we need to arrange the code, because ast.render() does not allow whitespaces at the beginning
        # of the first line. But this my be the case, if e.g. a function is part of a class.
        # So we calculated the leading spaces and remove the same amount of whitespaces from each code line
        code_lines = self.code.split("\n")
        leading_whitespaces = len(code_lines[0]) - len(code_lines[0].lstrip(' '))
        self.code = "\n".join(line[leading_whitespaces:] for line in code_lines)

        try:
            self.ast = ast.parse(self.code)
        except Exception as e:
            raise SourceCodeNotValid("Retrieved area source code could not "
                                     "be rendered to an abstract syntax tree (ast)")

    # def analyse(self):
    #     # calc_src = inspect.getsource(sys.modules[__name__])
    #     calc_src = inspect.getsource(manage)
    #     print(calc_src)
    #     calc_ast = ast.parse(calc_src)
    #     test = calc_ast.body[0].body[2]
    #
    #     # ast_rec(calc_ast.body[0].body[2])
    #
    #     visitor = ast.NodeVisitor()
    #     test_return = visitor.visit(test)
    #
    #     pass

    def explore(self, variable):
        """
        Starts the Exploration of the given variable
        :param variable:
        :return:
        """
        pass

    def ast_rec(self, node, space=0):
        # https://stackoverflow.com/questions/5533662/is-it-possible-to-visit-nodes-in-python-ast-with-ast-nodevisitor-twice-or-change
        for child in ast.walk(node):
            # for child in ast.iter_child_nodes(node):
            print(" " * space, child)
            # if isinstance(child, ast.Call):
            #     ast_rec(child, space+2)


    def _variable_assignments(self, source_tree, variables=None):
        """
        Detects assignments for specified variables.

        Examples:

        my_var = 5
        my_var = 2 + 4
        my_var = calculate(5,6,7,8)

        :param variables: List of variable names as string
        :return:
        """
        for var in variables:
            pass


    def _variable_usages(self, source_tree, variables):
        """
        Detects usages of specified variables.

        Analyses:

         - where a variable is used
         - what kind of usages it is (assignment, func call, return, ...)
         - what file/imports need to be analysed to follow variable data

        Examples:

        another_var = my_var
        another_var = my_var + 5
        another_var = calculate(my_var, 10)


        :param variables:
        :return:
        """
        for var in variables:
            pass

    def _variable_tracings(self, source_tree, variables):
        """
        Traces the variable its caller (function).
        Tries to receive source code and renders it as abstract source tree (ast)

        :param variables:
        :return:
        """

        for var in variables:
            pass


class UnknownAreaTypeException(BaseException):
    pass


class SourceCodeNotAvailableException(BaseException):
    pass


class SourceCodeNotValid(BaseException):
    pass

