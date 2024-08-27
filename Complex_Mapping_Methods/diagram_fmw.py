from graphviz import Digraph

# Define the workflow
workflow = {
    'Start': ['Read Data'],
    'Read Data': ['Transform Data'],
    'Transform Data': ['Write Data'],
    'Write Data': ['End']
}

# Create a Digraph object
dot = Digraph(comment='FME Workflow')

# Add nodes and edges
for node, edges in workflow.items():
    dot.node(node, node)
    for edge in edges:
        dot.edge(node, edge)

# Save and render the diagram
dot.render('fmw_workflow_diagram', format='png')

print("FME workflow diagram has been generated.")