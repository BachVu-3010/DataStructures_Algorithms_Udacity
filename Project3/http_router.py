class RouteTrie:
    """
    Stores the routes and their associated handlers

    E.g. "/about/me"
         (root, None) -> ("about", None) -> ("me", "About Me handler")
    """

    def __init__(self, handler=None):
        """
        Initializes RouteTrie with a root node and a handler (this is the root path or home page node

        :param handler: Handler
        """

        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        """
        Recursively adds nodes and assigns handler to leaf node of path

        :param path: Path
        :param handler: Handler
        :type path: List
        :type handler: String
        :return: None
        """

        node = self.root  # Node used to traverse the RouteTrie

        # Iterate over all parts in path
        for part in path:

            # If part isn't a child of current node
            if part not in node.children:
                # Add part as a child
                node.insert(part)

            # Move traversal node forward
            node = node.children[part]

        # Assign handler to leaf
        node.handler = handler

    def find(self, path):
        """
        Navigates RouteTrie to find a match for path

        :param path: Path
        :type path: List
        :return: Handler if path exists, Otherwise None
        """

        node = self.root  # Node used to traverse the RouteTrie

        # Iterate over all parts in path
        for part in path:

            # If part isn't a child of current node
            if part not in node.children:
                return None

            # Move traversal node forward
            node = node.children[part]

        return node.handler


class RouteTrieNode:
    """RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler"""

    def __init__(self, handler=None):
        """
        Initializes a RouteTrieNode

        :param handler: Handler
        """

        self.children = {}
        self.handler = handler

    def insert(self, part):
        """
        Helper function to RouteTrie.insert

        :param part: Part to insert
        :return: None
        """

        self.children[part] = RouteTrieNode()


class Router:
    """Router wraps Trie and handle"""

    def __init__(self, handler=None, not_found_handler=None):
        """Creates a router"""
        self.routes = RouteTrie(handler)
        # handler for 404 page not found responses
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """
        Adds a handler to a path

        :param path: Path
        :param handler: Handler to be added
        :return: None
        """

        # Call insert from RouteTrie
        self.routes.insert(self.split_path(path), handler)

    def lookup(self, path):
        """
        Looks up path (by parts)

        :param path: Path
        :return: Associated handler, or "not found" handler
        """

        # Remove trailing '/'
        # This is so we treat /about and /about/ the same, and '' and '/' the same
        path = path.rstrip('/')

        # If path is the ''
        if path == '':
            # Return the root's handler
            return self.routes.root.handler

        # Find handler for path
        handler = self.routes.find(self.split_path(path))

        # If a handler was found
        if handler is not None:
            return handler

        return self.not_found_handler

    def split_path(self, path):
        """
        Splits path into parts around '/'

        :param path: Path
        :return: List of parts
        """

        parts = path.split('/')
        return parts


def test_lookup(test_case):
    router = test_case[0]
    input = test_case[1]
    expected_output = test_case[2]

    if router.lookup(input) == expected_output:
        print('Pass')
    else:
        print("Fail")

    print("input:", input)
    print("output:", router.lookup(input))
    print()


# Create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # Add a route

test_lookup([router, "/", 'root handler'])
test_lookup([router, "/home", 'not found handler'])
test_lookup([router, "/home/about", 'about handler'])
test_lookup([router, "/home/about/", 'about handler'])
test_lookup([router, "/home/about/me", 'not found handler'])
