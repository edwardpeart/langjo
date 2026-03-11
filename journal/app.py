from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, TabbedContent, TabPane, TextArea, DirectoryTree, Markdown
from pathlib import Path
from .ui.file_tree import FileTreePanel
from .ui.stats_panel import StatsPanel
from .ui.editor import Editor
from .ui.history import History
from .logic.journal_logic import JournalService
from .logic.vocab_logic import VocabLogic



class LangjoApp(App):
    def __init__(self):
        super().__init__()
        self.journal_logic = JournalService()
        self.vocab_logic = VocabLogic()
    
    BINDINGS = [
        ("ctrl+s", "save_entry", "Save entry")
    ]
    TITLE = "LANGJO"
    CSS_PATH = "styles/langjo.tcss"
    THEME = "textual-dark"

    def on_mount(self) -> None:
        initial_entries = self.journal_logic.count_entries()
        initial_vocab = self.vocab_logic.count_words()

        stats = self.query_one(StatsPanel)
        stats.update_stats(initial_vocab, initial_entries)

    def compose(self) -> ComposeResult:
        yield Header("Langjo")

        with Horizontal(id="main"):

            # LEFT PANE
            with Vertical(id="left-pane"):
                yield FileTreePanel(id="file-tree", path="./data/entries")
                yield StatsPanel(id="stats")

            # RIGHT PANE
            with Vertical(id="right-pane"):
                with TabbedContent(id="editor-tabs"):
                    with TabPane("New Entry", id="tab-new"):
                        yield Editor("", id="editor")

                    with TabPane("History", id="tab-history"):
                        yield History("", id="history-view")

        yield Footer()

    def action_save_entry(self) -> None:
        editor = self.query_one("#editor", TextArea)
        content = editor.text
        
        self.journal_logic.save_entry(content)

        self.vocab_logic.add_from_text(content)

        vocab_count = self.vocab_logic.count_words()
        entry_count = self.journal_logic.count_entries()

        tree = self.query_one(FileTreePanel)
        tree.reload()
        
        stats = self.query_one(StatsPanel)
        stats.update_stats(vocab_count, entry_count)

        self.notify("Entry saved!", severity="information")
        editor.text = ""


    def on_directory_tree_file_selected(
        self, event: DirectoryTree.FileSelected
        ) -> None:
        file_path: Path = event.path

        content = self.journal_logic.read_entry(file_path)

        history_widget = self.query_one("#history-view", Markdown)
        history_widget.update(content)

        tabs = self.query_one("#editor-tabs", TabbedContent)
        tabs.active = "tab-history"
