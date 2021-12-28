#Cây
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}
#Lưu lại các nút đã thăm
visit = set() 
#Thuật toán tìm kiếm theo chiều sâu
def dfs(graph, start, end, path, visit):
    path.append(start)
    visit.add(start)
    if start == end:
        return path
    for child in graph[start]:
        if child not in visit:
            result = dfs(graph,child,end,path,visit)
            if result is not None:
                return result
    path.pop()
    return None

#Phần main của bài
#Người dùng nhập vào dữ liệu cho điểm bắt đầu và điểm kết thúc
start = (input("Nhập điểm bắt đầu: "))
start = start.upper()
while start not in graph:
    print("Điểm bắt đầu phải có trong cây!")
    start = input("Nhập lại điểm bắt đầu: ")
    start = start.upper()
end = input("Nhập điểm cần đến: ")
end = end.upper()
while end not in graph:
    print("Điểm đến phải có trong cây!")
    end = input("Nhập lại điểm cần đến: ")
    end = end.upper()

#Tạo 1 list để lưu lại đường đi từ điểm bắt đầu tới nút đích
path = []
#Chạy thuật toán để tìm đường đi
path = dfs(graph,start,end,path,visit)
#Đường đi tới nút đích
if path == None:
    print("Không tìm thấy đường đi")
else:
    print("Đường đi:")
    for x in path:
        if x == start:
            print(x,end="")
        else:
            print("->",x,end="")
