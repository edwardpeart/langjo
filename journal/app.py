from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, TabbedContent, TabPane
from .ui.file_tree import FileTreePanel
from .ui.stats_panel import StatsPanel
from .ui.editor import Editor
from .ui.history import History



class LangjoApp(App):
    BINDINGS = [
        ("ctrl+n", "new_entry", "New entry"),
        ("ctrl+s", "save_entry", "Save entry")
    ]
    TITLE = "LANGJO"
    CSS_PATH = "styles/langjo.tcss"
    THEME = "textual-dark"

    def compose(self) -> ComposeResult:
        yield Header("Langjo")
        
        with Horizontal(id="main"):
            yield FileTreePanel(id="file-tree", path="journal")

            with Vertical(id="right-pane"):
                
                with TabbedContent(id="editor-tabs"):
                    with TabPane("New Entry", id="tab-new"):
                        yield Editor("", id="editor")
                    with TabPane("History", id="tab-history"):
                        yield History("previous entries will be displayed here", id="history-view")
            
                yield StatsPanel("Stats will go here", id="stats")
        
        yield Footer()

