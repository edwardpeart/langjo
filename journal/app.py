from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, TabbedContent, TabPane, TextArea, DirectoryTree, Markdown
from pathlib import Path
from .ui.file_tree import FileTreePanel
from .ui.stats_panel import StatsPanel
from .ui.editor import Editor
from .ui.history import History
from .logic.journal import save_entry



class LangjoApp(App):
    BINDINGS = [
        ("ctrl+s", "save_entry", "Save entry")
    ]
    TITLE = "LANGJO"
    CSS_PATH = "styles/langjo.tcss"
    THEME = "textual-dark"

    def compose(self) -> ComposeResult:
        yield Header("Langjo")
        
        with Horizontal(id="main"):
            yield FileTreePanel(id="file-tree", path="./data/entries")

            with Vertical(id="right-pane"):
                
                with TabbedContent(id="editor-tabs"):
                    with TabPane("New Entry", id="tab-new"):
                        yield Editor("", id="editor")
                    with TabPane("History", id="tab-history"):
                        yield History("", id="history-view")
            
                yield StatsPanel("Stats will go here", id="stats")
        
        yield Footer()

    def action_save_entry(self) -> None:
        editor = self.query_one("#editor", TextArea)
        content = editor.text
        save_entry(content)

        tree = self.query_one(FileTreePanel)
        tree.reload()


    def on_directory_tree_file_selected(
        self, event: DirectoryTree.FileSelected
    ) -> None:
        file_path: Path = event.path

        # Only handle files (ignore directories)
        if file_path.is_file():
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            history_widget = self.query_one("#history-view", Markdown)
            history_widget.update(content)

            tabs = self.query_one("#editor-tabs", TabbedContent)
            tabs.active = "tab-history"
