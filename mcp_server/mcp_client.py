from fastmcp import Client
import asyncio

client = Client("http://127.0.0.1:8080/mcp")

async def call_pending_get_leaves():
    print("Getting Pending Employee Leaves")
    async with client:
        # Calling the tool we just created
        result = await client.call_tool("get_pending_leave_details")
        print("Employees pending leave details:")
        print(result)

async def call_all_get_leaves():
    print("Getting All Employee Leaves")
    async with client:
        # Calling the tool we just created
        result = await client.call_tool("get_all_leave_details")
        print("Employees currently on leave:")
        print(result)

async def call_employee_details(emp_name: str):
    print("Getting Employee Details")
    async with client:
        # Calling the tool we just created
        result = await client.call_tool("get_employee_details_for_name",{"emp_name": emp_name})
        print("Employees currently on leave:")
        print(result)

async def call_leave_status_update(leave_id: int, approval_status: str):
    print("Updating Leave status")
    async with client:
        # Calling the tool we just created
        result = await client.call_tool("update_employee_leave_request",{"leave_id": leave_id, "approval_status":approval_status})
        print("Updated Leave Status:")
        print(result)

if __name__ == "__main__":
    asyncio.run(call_all_get_leaves())
    #asyncio.run(call_leave_status_update('1','Pending'))
   # asyncio.run(call_employee_details('Arjun'))