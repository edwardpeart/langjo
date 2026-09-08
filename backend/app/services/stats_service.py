from datetime import date

from sqlalchemy.orm import Session

from journal.db.schemas import StatsResponse

from ..db.database import SessionLocal

from ..db.repositories.stats_repo import StatsRepository

class StatsService:
    def __init__(self):
        self.repo = StatsRepository()

    def get_streak(self, user_id=None) -> int:
        db: Session = SessionLocal()
        try:
            entries = self.repo.get_entries_date_desc(db, user_id=user_id)
        finally:
            db.close()

        if not entries:
            return 0

        streak = 1
        for i in range(1, len(entries)):
            delta = (entries[i - 1].created_at - entries[i].created_at).days
            if delta == 1:
                streak += 1
            else:
                break

        return streak

    def get_entry_count(self, user_id=None) -> int:
        db: Session = SessionLocal()
        try:
            return self.repo.get_entry_count(db, user_id=user_id)
        finally:
            db.close()

    def get_word_count(self, user_id=None) -> int:
        db: Session = SessionLocal()
        try:
            return self.repo.get_vocab_count(db, user_id=user_id)
        finally:
            db.close()

    def get_new_words_today(self, user_id=None) -> int:
        db: Session = SessionLocal()
        try:
            today = date.today()
            return self.repo.get_new_vocab_count_by_date(db, today, user_id=user_id)
        finally:
            db.close()

    def get_overview(self, user_id=None) -> StatsResponse:
        db: Session = SessionLocal()
        try:
            return StatsResponse(
                total_entries=self.get_entry_count(user_id=user_id),
                total_vocab=self.get_word_count(user_id=user_id),
                current_streak=self.get_streak(user_id=user_id),
                new_vocab_today=self.get_new_words_today(user_id=user_id),
            )
        finally:
            db.close()

    