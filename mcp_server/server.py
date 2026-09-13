import psycopg2
from psycopg2.extras import RealDictCursor
from fastmcp import FastMCP
from contextlib import contextmanager

# Create the MCP app instance
mcp = FastMCP("employee_server")

# DB Configuration
DB_CONFIG = {
    "user": "<your-db-user>",
    "password": "<your-db-password>",
    "host": "<your-db-ip-address>",
    "port": "5432",
    "database": "<your-db-name>"
}

@contextmanager
def get_db_connection():
    """Context manager to handle connection setup and teardown."""
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        yield conn
    except Exception as e:
        print(f"Database error: {e}")
        raise
    finally:
        if conn:
            conn.close()
            
            


@mcp.tool
def get_pending_leave_details() -> list:
    """
    Get employee leave details whose leave applications are pending
    Returns leave id, name, leave start date, leave end date, number of days on leave and leave reason.
    """
    
    query = """
        SELECT
            leave_id,
            employee_name, 
            TO_CHAR(leave_start_date, 'YYYY-MM-DD'),
            TO_CHAR(leave_end_date, 'YYYY-MM-DD'),
            (leave_end_date - leave_start_date + 1),
            reason
        FROM employee_leave_info
        WHERE approval_status='Pending';
    """
    
    try:
        # The 'with' statement automatically closes the connection for you
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query)
                return cursor.fetchall()
                    
    except Exception as error:
        print(f"Failed to fetch leave details: {error}")
    
@mcp.tool
def get_all_leave_details() -> list:
    """
    Get all the applied leave details in the databse
    Returns name, leave start date, leave end date, number of days on leave and leave reason, approval_status.
    """

    query = """
        SELECT 
            employee_name, 
            TO_CHAR(leave_start_date, 'YYYY-MM-DD'),
            TO_CHAR(leave_end_date, 'YYYY-MM-DD'),
            (leave_end_date - leave_start_date + 1),
            reason,
            approval_status
        FROM employee_leave_info;
    """

    try:
        # The 'with' statement automatically closes the connection for you
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    except Exception as error:
        print(f"Failed to fetch leave details: {error}")


@mcp.tool
def get_employee_details_for_name(emp_name: str) -> list:
    """
    Get employee details for an employee for the supplied name.
    Returns name, email id and contact number of the employee
    """

    query = """
        SELECT 
            employee_name, 
            email_id,
            contact_number
        FROM employee_info
        where employee_name ILIKE %s;
    """

    try:
        # The 'with' statement automatically closes the connection for you
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                search_term = f"%{emp_name}%"
                cursor.execute(query, (search_term,))
                return cursor.fetchall()

    except Exception as error:
        print(f"Failed to fetch leave details: {error}")

@mcp.tool
def update_employee_leave_request(leave_id: str, approval_status: str) -> dict:
    """
    Updates an employee's leave request status.
    Args:
        leave_id: The unique ID of the leave record.
        status: The new status ('Approved' or 'Rejected').
    """

    query = """
        UPDATE employee_leave_info 
        SET approval_status = %s 
        WHERE leave_id = %s;
    """

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (approval_status, leave_id))
                
                if cursor.rowcount == 0:
                    return {"error": f"No leave record found with ID {leave_id}"}
                
                conn.commit()
                return {
                    "success": True, 
                    "message": f"Leave ID {leave_id} successfully set to {approval_status}"
                }

    except Exception as e:
        return {"error": f"Database error: {str(e)}"}


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)