import logging
from typing import List
import urllib
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)


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
        logger.critical("Found node!")

        parameters = node.rawsource['parameters']
        docname = node.rawsource['docname']

        ref_node = nodes.reference('', '')
        innernode = nodes.emphasis(parameters, parameters)

        ref_node['refdocname'] = docname
        ref_node['refuri'] = app.builder.get_relative_uri(
            fromdocname, docname)
        ref_node['refuri'] += parameters
        ref_node.append(innernode)
        content = []
        para = nodes.paragraph()
        para += ref_node
        content.append(para)
        node.replace_self(content)


def setup(app):
    app.add_directive("query-param-ref", ButtonQueryParamRefDirective)
    app.connect("doctree-resolved", on_doctree_resolved)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
