from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag,  children):
        if children is None:
            raise ValueError("Children must be provided")

        super().__init__(tag)
        self.children = children

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")

        if not self.children:
            raise ValueError("No children")

        child_html = ''.join((child.to_html()) for child in self.children)
                

        return f"<{self.tag}>{child_html}</{self.tag}>"


