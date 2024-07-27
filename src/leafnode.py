from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, attrs=None):
        if attrs is None:
            attrs = {}       
        
        self.attrs = attrs

        super().__init__(tag, value, attrs)

        if value == "":
            raise ValueError("A Value is required.")



    def to_html(self):
        if self.value == "":
            raise ValueError("A Value is required")

        if self.tag is None:
            return f"{self.value}"
        
        attrs_str = ' '.join(f'{key}="{value}"' for key, value in self.attrs.items())
        opening_tag = f"{self.tag} {attrs_str}".strip() 
        return f"<{opening_tag}>{self.value}</{self.tag}>"
