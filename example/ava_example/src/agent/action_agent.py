from src.agent.base import BaseGraph
from src.nodes import action_node

class ActionGraph(BaseGraph):
    def __init__(self):
        super().__init__(
            action_node.call_model,
            action_node.should_continue,
            action_node.action_to_agent_condition,
            action_node.tool_node,
        )

action_graph = ActionGraph().get_graph()
