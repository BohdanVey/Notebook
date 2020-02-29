import datetime

last_id = 0


class Note:
    """
    Save inforation about Notes in our notebook
    """

    def __init__(self, memo, tags):
        self.memo = memo
        self.tags = tags
        self.creation_data = str(datetime.datetime.now())
        print(self.creation_data)
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, search_filter):
        """
        Check if this note have some text.
        Return True if it have,
        else False
        Search is case sensitive and matches both text and tags.
        """

        return search_filter in self.memo or search_filter in self.tags

    def __str__(self):
        return 'ID: {}, Tags: {}:\n{}\n{}'.format(str(self.id), ', '.join(self.tags),self.creation_data, self.memo)


class Notebook:
    def __init__(self):
        """
        Create a notebook
        """
        self.notes = []

    def search(self, search_filter):
        '''Find all notes that match the given filter
        string.'''

        return list(filter(lambda note: note.match(search_filter), self.notes))

    def new_note(self, memo, tags):
        """
        Add new note to out notebook
        """
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """
        Modify memo in given note
        """
        note = list(filter(lambda note: note.id == note_id, self.notes))
        if len(note) != 0:
            note[0].memo = memo

    def modify_tags(self, note_id, tags):
        """
        Modify tags in given note
        """
        note = list(filter(lambda note: note.id == note_id, self.notes))[0]
        note.tags = tags


if __name__ == '__main__':
    print(Note('my new note',['1','2','3']))
