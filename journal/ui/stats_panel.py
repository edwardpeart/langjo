from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.containers import Vertical

class StatsPanel(Static):
    BORDER_TITLE = "Stats"

    def compose(self) -> ComposeResult:
        with Vertical(id="stats-container"):
            
            # These labels start with placeholder text
            yield Label("Vocabulary: 0", id="stat-vocab", classes="stat-line")
            yield Label("Total Entries: 0", id="stat-entries", classes="stat-line")
            # yield Label("Current Streak: 0", id="stat-streak", classes="stat-line")

    def update_stats(self, vocab_count, entry_count, streak=None):
        """Update the combined text of each label."""
        self.query_one("#stat-vocab").update(f"Vocabulary: [b]{vocab_count} words[/b]")
        self.query_one("#stat-entries").update(f"Total Entries: [b]{entry_count}[/b]")
        # self.query_one("#stat-streak").update(f"Current Streak: [b]{streak} days[/b]")