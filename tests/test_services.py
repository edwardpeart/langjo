import unittest

from sqlalchemy.orm import Session
from backend.app.db.database import SessionLocal
from backend.app.services.journal_service import JournalService
from backend.app.services.vocab_service import VocabService
from backend.app.services.stats_service import StatsService

class TestJournalService(unittest.TestCase):
    def setUp(self):
        self.journal_service = JournalService()
        self.vocab_service = VocabService()
        self.stats_service = StatsService()

    def test_save_entry(self):
        text = "This is a test entry."
        new_entry = self.journal_service.save(text)
        
        # Verify that the entry was saved
        db: Session = SessionLocal()
        try:
            entry = self.journal_service.repo.get_entry(db, new_entry.id)
            self.assertEqual(entry.body, text)
        finally:
            db.close()

    def test_add_vocab(self):
        text = "これはテストです。"
        self.vocab_service.add(text)
        
        # Verify that the vocab was added
        db: Session = SessionLocal()
        try:
            vocab_count = self.stats_service.get_word_count()
            self.assertGreater(vocab_count, 0)
        finally:
            db.close()

    def test_get_streak(self):
        streak = self.stats_service.get_streak()
        self.assertIsInstance(streak, int)

class TestVocabService(unittest.TestCase):
    def setUp(self):
        self.vocab_service = VocabService()

    def test_add_vocab(self):
        text = "これはテストです。"
        self.vocab_service.add(text)
        
        # Verify that the vocab was added
        db: Session = SessionLocal()
        try:
            vocab_count = self.vocab_service.repo.get_vocab_count(db)
            self.assertGreater(vocab_count, 0)
        finally:
            db.close()

    def test_duplicate_vocab_is_not_added_twice(self):
        text = "これはテストです。"
        self.vocab_service.add(text)
        self.vocab_service.add(text)

        db: Session = SessionLocal()
        try:
            vocab_count = self.vocab_service.repo.get_vocab_count(db)
            self.assertEqual(vocab_count, 1)
        finally:
            db.close()

class TestStatsService(unittest.TestCase):
    def setUp(self):
        self.journal_service = JournalService()
        self.stats_service = StatsService()

    def test_update_keeps_same_entry_id_and_appends_body(self):
        entry = self.journal_service.save("first draft")
        updated = self.journal_service.update(entry.id, "second draft")

        self.assertEqual(updated.id, entry.id)
        self.assertIn("first draft", updated.body)
        self.assertIn("second draft", updated.body)

    def test_get_streak(self):
        streak = self.stats_service.get_streak()
        self.assertIsInstance(streak, int)

    def test_get_entry_count(self):
        entry_count = self.stats_service.get_entry_count()
        self.assertIsInstance(entry_count, int)

    def test_get_word_count(self):
        word_count = self.stats_service.get_word_count()
        self.assertIsInstance(word_count, int)
