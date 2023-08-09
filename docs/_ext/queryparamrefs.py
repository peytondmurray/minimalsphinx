from docutils import nodes
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class URLQueryParamRefNode(nodes.General, nodes.Element):
    pass


class URLQueryParamRefDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        "parameters": directives.unchanged_required,
        "classes": directives.class_option,
        "ref-type": lambda choice: directives.choice(choice, ["any", "ref", "doc", "myst"]),
    }

    def run(self):
        ref_type = self.options.get('ref-type', 'any')
        return [
            URLQueryParamRefNode(
                {
                    'docname': self.env.docname,
                    'parameters': self.options.get('parameters', None),
                    "classes": self.options.get('class', ''),
                    "reftarget": directives.uri(self.arguments[0]),
                    "refdoc": self.env.docname,
                    "refdomain": "std" if ref_type in {"ref", "doc"} else "",
                    "reftype": ref_type,
                    "refexplicit": self.content,
                    "refwarn": True,
                }
            )
        ]


def on_doctree_resolved(app, doctree, fromdocname):
    """Replace

    Args:
        app ():
        doctree ():
        fromdocname ():
    """
    for node in doctree.traverse(URLQueryParamRefNode):
        parameters = node.rawsource['parameters']
        docname = node.rawsource['docname']

        ref_node = nodes.reference(docname, docname)
        ref_node['refdocname'] = docname
        ref_node['refuri'] = app.builder.get_relative_uri(fromdocname, docname) + parameters

        wrapper = nodes.paragraph()
        wrapper += ref_node
        node.replace_self([wrapper])


def setup(app):
    app.add_directive("query-param-ref", URLQueryParamRefDirective)
    app.connect("doctree-resolved", on_doctree_resolved)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class ButtonQueryParamRefNode(nodes.General, nodes.Element):
    pass


class ButtonQueryParamRefDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        "parameters": directives.unchanged_required,
    }

    def run(self):
        breakpoint()
        return [
            ButtonQueryParamRefNode(
                {
                    'docname': self.env.docname,
                    'parameters': self.options.get('parameters', None)
                }
            )
        ]


def on_doctree_resolved(app, doctree, fromdocname):
    for node in doctree.traverse(ButtonQueryParamRefNode):
        parameters = node.rawsource['parameters']
        docname = node.rawsource['docname']

        breakpoint()

        ref_node = nodes.reference(docname, docname)
        ref_node['refdocname'] = docname
        ref_node['refuri'] = app.builder.get_relative_uri(fromdocname, docname) + parameters

        para = nodes.paragraph()
        para += ref_node
        node.replace_self([para])


def setup(app):
    app.add_directive("query-param-ref", ButtonQueryParamRefDirective)
    app.connect("doctree-resolved", on_doctree_resolved)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
