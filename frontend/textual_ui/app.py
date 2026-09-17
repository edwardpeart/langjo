from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, TabbedContent, TabPane, TextArea, Tree

from backend.app.db.database import init_db
from backend.app.services.journal_service import JournalService
from backend.app.services.vocab_service import VocabService
from backend.app.services.stats_service import StatsService

from frontend.textual_ui.entry_tree import EntryTreePanel
from frontend.textual_ui.stats_panel import StatsPanel
from frontend.textual_ui.editor import Editor
from frontend.textual_ui.history import History

class LangjoApp(App):
    def __init__(self):
        super().__init__()
        init_db()
        self.journal_service = JournalService()
        self.vocab_service = VocabService()
        self.stats_service = StatsService()
        self.selected_entry_id = None

    
    BINDINGS = [
        ("ctrl+s", "save_entry", "Save Entry")
    ]
    TITLE = "LANGJO"
    CSS_PATH = "styles/langjo.tcss"
    THEME = "textual-dark"

    def on_mount(self) -> None:
        initial_entries = self.stats_service.get_entry_count()
        initial_vocab = self.stats_service.get_word_count()
        current_streak = self.stats_service.get_streak()

        stats = self.query_one(StatsPanel)
        stats.update_stats(initial_vocab, initial_entries, current_streak)

    def compose(self) -> ComposeResult:
        yield Header("Langjo")

        with Horizontal(id="main"):

            # LEFT PANE
            with Vertical(id="left-pane"):
                yield EntryTreePanel(id="file-tree")
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

        if self.selected_entry_id is not None:
            entry = self.journal_service.update(self.selected_entry_id, content)
        else:
            entry = self.journal_service.save(content)
            self.vocab_service.add(content, entry_id=entry.id)

        vocab_count = self.stats_service.get_word_count()
        entry_count = self.stats_service.get_entry_count()
        current_streak = self.stats_service.get_streak()

        tree = self.query_one(EntryTreePanel)
        tree.populate()

        stats = self.query_one(StatsPanel)
        stats.update_stats(vocab_count, entry_count, current_streak)

        self.notify("Entry saved!", severity="information")
        editor.text = ""
        self.selected_entry_id = None


    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        entry_id = event.node.data
        if not isinstance(entry_id, int):
            return

        self.selected_entry_id = entry_id
        entry = self.journal_service.get_entry(entry_id)
        if entry is None:
            return

        history_widget = self.query_one("#history-view", History)
        history_widget.update(entry.body)

        tabs = self.query_one("#editor-tabs", TabbedContent)
        tabs.active = "tab-history"
