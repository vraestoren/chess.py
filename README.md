# <img src="https://github.com/user-attachments/assets/d8c20238-e0ab-4384-b74e-25eefef1943b" width="100" style="vertical-align:middle;" /> chess.py

> Web-API for [Chess.com](https://chess.com) to access player profiles, games, leaderboards, news, articles, forums, and more via the Chess.com mobile API.

## Quick Start
```python
from chess import Chess

chess = Chess()
chess.login(email="example@gmail.com", password="password")

# Get your profile
print(chess.get_account_info())
```

---

## Constructor
```python
Chess()
# Automatically generates a device ID on init — no setup needed.
```

---

## Authentication

| Method | Description |
|--------|-------------|
| `login(email, password)` | Sign in and store access token |
| `register(username, email, password)` | Create a new account |

---

## Profile

| Method | Description |
|--------|-------------|
| `get_account_info()` | Get current user's profile |
| `get_user_info(username, user_id)` | Get a user's public profile |
| `get_notifications()` | Get current notifications |
| `edit_profile(first_name, last_name, location, country_id)` | Update profile info |
| `edit_basic_info(skill_level, self_assessed_skill_level)` | Update skill level info |
| `change_status(status)` | Update status text |
| `block_user(username)` | Block a user |
| `unblock_user(username)` | Unblock a user |
| `send_message(username, content)` | Send a private message |

---

## Games

| Method | Description |
|--------|-------------|
| `get_games(start, limit)` | Get top live games |
| `get_game_by_legacy_id(legacy_id)` | Get a game by legacy ID |
| `get_game_chat(game_id, limit)` | Get observer chat for a live game |
| `send_game_message(game_id, content)` | Send a message in game chat |
| `get_daily_puzzles()` | Get today's daily puzzles |

---

## Leaderboards

| Method | Description |
|--------|-------------|
| `get_top_players()` | Get top players for the navbar |
| `get_leaderboard(leaderboard_type, page)` | Get global or variant leaderboard |
| `get_leaderboard_stats(leaderboard_type)` | Get leaderboard stats by game type |

**Leaderboard types:** `global`, `game_live_blitz`, `game_live_bullet`, `game_live_rapid`

---

## News

| Method | Description |
|--------|-------------|
| `get_news_categories()` | Get all news categories |
| `get_news(page, per_page)` | Get paginated news list |
| `get_news_by_id(news_id)` | Get a news item by ID |
| `get_news_comments(news_id, page, per_page)` | Get comments on a news item |
| `comment_news(news_id, content)` | Post a comment on a news item |

---

## Articles

| Method | Description |
|--------|-------------|
| `get_articles(page, per_page)` | Get paginated articles list |
| `get_article(article_id)` | Get an article by ID |
| `get_article_comments(article_id, page, per_page)` | Get comments on an article |
| `comment_article(article_id, content)` | Post a comment on an article |
| `read_article(article_id)` | Mark an article as read |

---

## Forums

| Method | Description |
|--------|-------------|
| `get_forum_categories()` | Get all forum categories |
| `get_forum_topics(category_id, page, per_page)` | Get topics in a category |
| `get_topic_comments(topic_id, page, per_page)` | Get comments on a topic |
