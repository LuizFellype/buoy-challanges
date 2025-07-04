from rest_framework.pagination import CursorPagination

class IDCursorPagination(CursorPagination):
    ordering = "id"
    page_size_query_param = "size"
    page_size = 1
    
