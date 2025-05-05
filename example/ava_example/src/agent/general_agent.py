from src.agent.base import BaseGraph
from src.nodes import general_node

class GeneralGraph(BaseGraph):
    def __init__(self):
        super().__init__(
            general_node.call_model,
            general_node.should_continue,
            general_node.action_to_agent_condition,
            general_node.tool_node
        )

general_graph = GeneralGraph().get_graph()