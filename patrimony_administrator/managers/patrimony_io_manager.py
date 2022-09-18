import json


class PatrimonyIOManager:
    """
    Helper class to help loading and interacting with the data on the database
    file containing the patrimony items.
    """

    def __init__(self, database_file_path) -> None:

        self.database_file_path = database_file_path

        # Load instance variables from file
        with open(database_file_path) as patrimony_file:
            patrimony = json.load(patrimony_file)

            self.count = patrimony["count"]
            self.index = patrimony["index"]
            self.items = patrimony["items"]


    def __str__(self):
        return f" Total item number: {self.count}\n Items = \n {json.dumps(self.items, indent=4)} "


    def __repr__(self):
        return self.__str__()


    def commit_changes(self, print_: bool = False, clear: bool = False) -> str:
        """
        Save changes to the database file

        Parameters:
        -----------

        print_ : bool, defaul: False
            If true print the output json

        clear : bool, defaul: False
            If true wipe the database. To help with development purposes.

        Returns
        -------
        
        str
            Json dump as string

        File Transformations
        --------------------
        
        Save changes to `self.database_file_path`.
        """
        
        if not clear:
            db_json = {
                "count": self.count,
                "index": self.index,
                "items": self.items
            }
        else:
            db_json = {
                "count": 0,
                "index": 0,
                "items": {}
            }

            self.index = 0
            self.count = 0
            self.items = {}

        if print_:
            print(json.dumps(db_json, indent=4))

        with open(self.database_file_path, "w") as patrimony_file:
            json.dump(db_json, patrimony_file, indent=True)

        return json.dumps(db_json, indent=4)

    # CRUD

    # Create
    def create_item(self, item_characteristics: dict) -> int | None:
        """
        Given a dict with the characteristics of a patrimony item writes it
        to the database file.
        """

        self.index += 1
        self.count += 1

        # Some assertions to make the test more realistic
        assert {"type"} <= set(item_characteristics), "Item must have a type key"

        # derived_characteristics = {"id": self.index}
        # item_characteristics = {**derived_characteristics, **item_characteristics}

        self.items[str(self.index)] = item_characteristics

        return self.index

    # Read
    def read_item(self, item_id: str) -> dict | None:
        """Read patrimony item based on id"""

        try:
            return self.items[item_id]
        except KeyError:
            print("Item doesn't exist")
            return None


    # Update
    def update_item(self, item_id: str, update_as_dict: dict) -> dict | None:
        """
        Update item properties using it's id and a dictionary with the key
        representing the property name and value the updated value.
        """
        item = self.items[item_id]

        if "id" in update_as_dict:
            print("Shouldn't update id field!")
            return None

        item.update(update_as_dict)

        self.items[item_id] = item
        return self.items[item_id]

    # Delete
    def delete_item(self, item_id: str) -> dict | None:
        """Delete item based on id"""
        try:
            item = self.items[item_id]
            del self.items[item_id]
            self.count -= 1
            return item
        except KeyError:
            print("This item id doesn't exist")
            return None


def tests():
    
    FILE = "patrimony.json"

    patrimony = PatrimonyIOManager(FILE)

    patrimony.commit_changes(clear=True)

    print("Testing CREATE")

    print(patrimony, end="\n\n")

    patrimony.create_item({"type": "asset", "description": "First item"})
    patrimony.create_item({"type": "asset", "description": "Second item"})
    patrimony.create_item({"type": "liability", "description": "Third item"})

    print(patrimony)

    print("\nTesting READ")

    print(patrimony.read_item(1))
    print()

    print("Testing UPDATE")

    print(patrimony.update_item(1, {"description": "bla"}))
    print(patrimony.read_item(1))
    print(patrimony)
    print()

    print("Testing DELETE")

    print(patrimony.delete_item(1))
    print(patrimony.read_item(1))
    print(patrimony)
    print()

    print("Testing COMMIT")
    patrimony.commit_changes(print_=True)
    # patrimony.commit_changes(clear=True)


if __name__ == "__main__":
    tests()
