from typing import Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list[object]] = None,
        props: Optional[dict[str, str]] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return f' href="{self.props["href"]}" target="{self.props["target"]}"'
        else:
            return ""

    def __repr__(self) -> str:
        return (
            f"HTMLNode({self.tag},{self.value},{str(self.children)},{str(self.props)})"
        )

    def __eq__(self, obj: object) -> bool:
        return (
            True
            if (self.tag == obj.tag)
            and (self.value == obj.value)
            and (self.children == obj.children)
            and (self.props == obj.props)
            else False
        )


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str, value: str, props: Optional[dict[str, str]] = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Missing value")
        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[object], props: Optional[dict[str, str]] = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if not self.children:
            raise ValueError("Missing children")
        
        return f'<{self.tag}{self.props_to_html()}>{"".join([a.to_html() for a in self.children])}</{self.tag}>'
