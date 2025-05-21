class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        def dfs(current_room):
            if current_room in visited:
                return 
            visited.add(current_room)
            for room in rooms[current_room]:
                dfs(room)

        dfs(0)
        if len(visited) == n:
            return True
        return False 
