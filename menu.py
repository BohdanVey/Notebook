from notebook import Note, Notebook


class Menu:
    """
    It is a menu for easy work with notebook
    """

    def __init__(self):
        """
        Initialize a menu
        """
        self.notebook = Notebook()

    def __str__(self):
        return """Print "add" to add new note
Print "update" to modify note
Print "search" to Search specific notes
Print "show" to show all notes
Print "quit" to exit"""

    def main(self):
        """
        Function to control your Notebook
        """
        print(self)
        read = input().lower().strip()
        if read == 'search':
            self.search()
        elif read == 'add':
            self.add()
        elif read == 'update':
            self.update()
        elif read == 'show':
            self.show()
        elif read == 'quit':
            print('Thanks for using my program')
            return
        else:
            print('The {} is incorrect input'.format(read))
        self.main()

    def search(self):
        """
        Search specific note in notebook
        """
        to_search = input('Print an filter: ')
        notes = self.notebook.search(to_search)
        for note in notes:
            print(note)

    def add(self):
        """
        Add new note to notebook
        """
        memo = input('Enter a memo: ')
        tags = input('Enter a tags: ')
        self.notebook.new_note(memo, tags)
        print(self.notebook.notes[-1])

    def update(self):
        """
        Update note
        """
        id = int(input('Print note id: '))
        to_change = input('Print memo to change memo, or anything'
                          ' else to change tags: ')
        if to_change.lower().strip() == 'memo':
            memo = input('Enter a memo: ')
            self.notebook.modify_memo(id, memo)
        else:
            tags = input('Enter a tags: ')
            self.notebook.modify_tags(id, tags)

    def show(self):
        """
        Show all notes in Notebook
        """
        for note in self.notebook.notes:
            print(note)


if __name__ == '__main__':
    menu = Menu()
    menu.main()
