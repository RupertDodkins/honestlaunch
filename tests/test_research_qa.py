from __future__ import annotations

import unittest

from honestlaunch.research_qa import build_qa_packet, find_archive_entry_by_slug


class ResearchQATests(unittest.TestCase):
    def test_find_archive_entry_by_slug(self) -> None:
        entry = find_archive_entry_by_slug("gemini-35-flash")

        self.assertIsNotNone(entry)
        self.assertEqual(entry["lab"], "Google")
        self.assertEqual(entry["artifactHtml"], "gemini_35_flash_report.html")

    def test_build_qa_packet(self) -> None:
        packet = build_qa_packet("anthropic-sonnet-45")

        self.assertEqual(packet["slug"], "anthropic-sonnet-45")
        self.assertEqual(packet["launch"]["lab"], "Anthropic")
        self.assertEqual(len(packet["discovery"]["providers"]), 2)
        self.assertEqual(packet["discovery"]["providers"][0]["status"], "pending")
        self.assertEqual(packet["humanDecision"]["publishStatus"], "pending")


if __name__ == "__main__":
    unittest.main()
