from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Add_Tool")

@mcp.tool()
def add(first_num: int, secondNum: int) -> int :

    """
    take two number and return the sum value

    Args:
        first_num: first number
        secondNum: second number
    """

    return first_num + secondNum


