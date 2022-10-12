from linkedlist import LinkedList


class Branch(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.head = None

    def commit(self, obj: object) -> None:
        if not self.head:
            self.head = LinkedList(obj)
        else:
            self.head.push(obj)

    def status(self) -> None:
        print(f"Branch: {self.name}")
        print(self.head)


class Git(object):
    def __init__(self) -> None:
        self.branches = {}
        self.current_branch = None

    def branch(self) -> None:
        print("📌", self.current_branch.name)
        for branch in self.branches:
            if branch != self.current_branch.name:
                print("✖️ ", branch)

    def checkout(self, branch_name: str) -> None:
        if branch_name not in self.branches:
            self.branches[branch_name] = Branch(branch_name)
        self.current_branch = self.branches[branch_name]
        print(f"Switched to branch {branch_name}")

    def commit(self, obj: object) -> None:
        if not self.current_branch:
            raise Exception("No branch selected")
        self.current_branch.commit(obj)
        print(f"Committed {obj}")

    def log(self) -> None:
        if not self.current_branch:
            raise Exception("No branch selected")
        print(self.current_branch.head)

    def status(self) -> None:
        if not self.current_branch:
            raise Exception("No branch selected")
        self.current_branch.status()
        print("")

    def revert(self) -> None:
        if not self.current_branch:
            raise Exception("No branch selected")
        self.current_branch.head.pop()

    def merge(self, branch_name: str) -> None:
        if branch_name not in self.branches:
            raise Exception(f"Branch {branch_name} does not exist")
        if not self.current_branch:
            raise Exception("No branch selected")

        branch = self.branches[branch_name]
        current = self.current_branch.head.node

        while current.next:
            current = current.next
        current.next = branch.head.node

        print(f"Merged {branch_name} into {self.current_branch.name}")


if __name__ == "__main__":
    git = Git()
    git.checkout("main")
    git.commit("Initial commit")
    git.status()

    git.checkout("dev")
    git.commit("Initial commit")
    git.status()

    git.checkout("main")
    git.commit("Add README.md")
    git.commit("Add LICENSE")
    git.status()

    git.checkout("dev")
    git.commit("Add .gitignore")
    git.status()

    git.checkout("main")
    git.merge("dev")
    git.status()

    git.branch()
