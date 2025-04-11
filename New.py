import sys
import threading

sys.setrecursionlimit(1 << 25)

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child

    def remove_child(self, child_name):
        if child_name in self.children:
            self.children[child_name].parent = None
            del self.children[child_name]

class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.path_map = {"root": self.root}

    def get_node(self, path):
        return self.path_map.get(path)

    def add_path(self, parent_path, *child_names):
        parent = self.get_node(parent_path)
        if not parent:
            return
        for name in child_names:
            full_path = f"{parent_path}/{name}"
            node = Directory(name)
            parent.add_child(node)
            self.path_map[full_path] = node

    def count_descendants(self, path):
        node = self.get_node(path)
        if not node:
            return "Invalid command"

        def dfs(n):
            total = 0
            for child in n.children.values():
                total += 1 + dfs(child)
            return total

        return dfs(node)

    def is_ancestor(self, src, dest):
        while dest:
            if dest == src:
                return True
            dest = dest.parent
        return False

    def cut_paste(self, src_path, dest_path):
        src = self.get_node(src_path)
        dest = self.get_node(dest_path)

        if not src or not dest or src == dest:
            return "Invalid command"
        if self.is_ancestor(src, dest):
            return "Invalid command"
        if src.name in dest.children:
            return "Invalid command"

        def remove_paths(n, cur_path):
            if cur_path in self.path_map:
                del self.path_map[cur_path]
            for child in n.children.values():
                remove_paths(child, f"{cur_path}/{child.name}")

        remove_paths(src, src_path)

        src.parent.remove_child(src.name)
        dest.add_child(src)

        new_path = f"{dest_path}/{src.name}"

        def update_paths(n, cur_path):
            self.path_map[cur_path] = n
            for child in n.children.values():
                update_paths(child, f"{cur_path}/{child.name}")

        update_paths(src, new_path)
        return "OK"

    def copy_paste(self, src_path, dest_path):
        src = self.get_node(src_path)
        dest = self.get_node(dest_path)

        if not src or not dest or src == dest:
            return "Invalid command"
        if self.is_ancestor(src, dest):
            return "Invalid command"
        if src.name in dest.children:
            return "Invalid command"

        def clone_tree(node):
            new_node = Directory(node.name)
            for child in node.children.values():
                new_node.add_child(clone_tree(child))
            return new_node

        copied = clone_tree(src)
        dest.add_child(copied)

        new_path = f"{dest_path}/{src.name}"

        def register_paths(n, cur_path):
            self.path_map[cur_path] = n
            for child in n.children.values():
                register_paths(child, f"{cur_path}/{child.name}")

        register_paths(copied, new_path)

        if len(self.path_map) > 10**6:
            return "Invalid command"

        return "OK"

def main():
    fs = FileSystem()
    n, q = map(int, input().split())

    for _ in range(n):
        parts = input().split()
        fs.add_path(parts[0], *parts[1:])

    for _ in range(q):
        parts = input().split()
        if parts[0] == "countDescendants":
            result = fs.count_descendants(parts[1])
            print(result)
        elif parts[0] == "cutPaste":
            result = fs.cut_paste(parts[1], parts[2])
            print(result)
        elif parts[0] == "copyPaste":
            result = fs.copy_paste(parts[1], parts[2])
            print(result)
        else:
            print("Invalid command")

threading.Thread(target=main).start()
