from random import choice
from curl_cffi import requests

class Chess:
    def __init__(self) -> None:
        self.api = "https://api.chess.com"
        self.web_api = "https://www.chess.com/service"
        self.device_id = self.generate_device_id()
        self.client_id = "1bc9f2f2-4961-11ed-8971-f9a8d47c7a48"
        self.user_id = None
        self.access_token = None
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Chesscom-Android/4.9.17-googleplay (Android/9; ASUS_I003DD; ru_RU; contact #android in Slack)",
            "x-chesscom-bucketing-id": self.device_id,
            "x-chesscom-device-id": self.device_id,
            "X-Client-Version": "Android4.9.17"
        }

    def _post(self, endpoint: str, data: dict = None, use_json: bool = False) -> dict:
        kwargs = {"json": data} if use_json else {"data": data}
        return self.session.post(
            f"{self.api}{endpoint}", **kwargs).json()

    def _get(self, endpoint: str, base: str = None) -> dict:
        base = base or self.api
        return self.session.get(f"{base}{endpoint}").json()

    def _put(self, endpoint: str) -> dict:
        return self.session.put(f"{self.api}{endpoint}").json()

    def _delete(self, endpoint: str) -> dict:
        return self.session.delete(f"{self.api}{endpoint}").json()

    def generate_device_id(self) -> str:
        return "".join(choice("abcdef0123456789") for _ in range(32))

    def login(self, email: str, password: str) -> dict:
        data = {
            "factorIdentifier": email,
            "password": password,
            "deviceId": self.device_id,
            "clientId": self.client_id
        }
        response = self._post("/v1/users/login", data)
        if response["status"]:
            self.user_id = response["data"]["uuid"]
            self.access_token = response["data"]["oauth"]["access_token"]
            self.session.headers["Authorization"] = f"Bearer {self.access_token}"
        return response

    def register(
            self, username: str, email: str, password: str) -> dict:
        data = {
            "username": username,
            "password": password,
            "email": email,
            "deviceId": self.device_id,
            "bucketingId": self.device_id,
            "clientId": self.client_id
        }
        return self._post("/v1/users", data)

    def get_account_info(self) -> dict:
        return self._get("/v1/users")

    def get_user_info(
            self,
            username: str = None,
            user_id: str = None) -> dict:
        if username:
            return self._get(f"/v1/users?username={username}")
        return self._get(f"/v1/users?userUuid={user_id}")

    def get_notifications(self) -> dict:
        return self._get("/v1/users/notifications/current")

    def edit_profile(
            self,
            first_name: str = None,
            last_name: str = None,
            location: str = None,
            country_id: int = None) -> dict:
        data = {}
        if first_name:
            data["firstName"] = first_name
        if last_name:
            data["lastName"] = last_name
        if location:
            data["location"] = location
        if country_id:
            data["countryId"] = country_id
        return self._post("/v1/users", data, use_json=True)

    def edit_basic_info(
            self,
            skill_level: int = None,
            self_assessed_skill_level: int = None) -> dict:
        data = {}
        if skill_level:
            data["skillLevel"] = skill_level
        if self_assessed_skill_level:
            data["selfAssessedSkillLevel"] = self_assessed_skill_level
        return self._post("/v1/users/profile", data, use_json=True)

    def change_status(self, status: str) -> dict:
        data = {
            "status": status
        }
        return self._post("/v1/users/status", data)

    def get_top_players(self) -> dict:
        return self._get("/topplayers/navbar", base=self.web_api)

    def get_daily_puzzles(self) -> dict:
        return self._get("/v1/puzzles/daily/today")

    def get_leaderboard(
            self, leaderboard_type: str = "global", page: int = 0) -> dict:
        return self._get(
            f"/v1/leaderboard?type={leaderboard_type}&page={page}")

    def get_leaderboard_stats(
            self, leaderboard_type: str = "game_live_blitz") -> dict:
        return self._get(
            f"/v1/users/leaderboard-stats/{leaderboard_type}")

    def get_forum_categories(self) -> dict:
        return self._get("/v1/forums/categories")

    def get_forum_topics(
            self,
            category_id: int,
            page: int = 0,
            per_page: int = 20) -> dict:
        return self._get(
            f"/v1/forums/topics?forumCategoryId={category_id}&page={page}&topicsPerPage={per_page}")

    def get_topic_comments(
            self,
            topic_id: int,
            page: int = 0,
            per_page: int = 20) -> dict:
        return self._get(
            f"/v1/forums/comments?forumTopicId={topic_id}&page={page}&commentsPerPage={per_page}")

    def get_news_categories(self) -> dict:
        return self._get("/v1/news/categories")

    def get_news(self, page: int = 0, per_page: int = 20) -> dict:
        return self._get(f"/v1/news?page={page}&itemsPerPage={per_page}")

    def get_news_by_id(self, news_id: int) -> dict:
        return self._get(f"/v1/news/{news_id}")

    def get_news_comments(
            self,
            news_id: int,
            page: int = 0,
            per_page: int = 20) -> dict:
        return self._get(
            f"/v1/news/{news_id}/comments?page={page}&itemsPerPage={per_page}")

    def comment_news(self, news_id: int, content: str) -> dict:
        data = {
            "commentBody": f"<p>{content}</p>"
        }
        return self._post(f"/v1/news/{news_id}/comments", data)

    def get_articles(self, page: int = 0, per_page: int = 20) -> dict:
        return self._get(
            f"/v1/articles/list?page={page}&itemsPerPage={per_page}")

    def get_article(self, article_id: int) -> dict:
        return self._get(f"/v1/articles/{article_id}")

    def get_article_comments(
            self,
            article_id: int,
            page: int = 0,
            per_page: int = 20) -> dict:
        return self._get(
            f"/v1/articles/{article_id}/comments?page={page}&itemsPerPage={per_page}")

    def comment_article(self, article_id: int, content: str) -> dict:
        data = {
            "commentBody": f"<p>{content}</p>"
        }
        return self._post(f"/v1/articles/{article_id}/comments", data)

    def read_article(self, article_id: int) -> dict:
        return self._put(f"/v1/articles/{article_id}/read")

    def block_user(self, username: str) -> dict:
        data = {
            "username": username
        }
        return self._post("/v1/users/blocked", data)

    def unblock_user(self, username: str) -> dict:
        return self._delete(f"/v1/users/blocked?username={username}")

    def send_message(self, username: str, content: str) -> dict:
        data = {
            "username": username,
            "content": f"<p>{content}</p>"
        }
        return self._post("/v1/messages", data)

    def get_games(self, start: int = 0, limit: int = 10) -> dict:
        return self._get(
            f"/gamelist/top?from={start}&limit={limit}",
            base=self.web_api)

    def get_game_by_legacy_id(self, legacy_id: int) -> dict:
        return self._get(f"/play/games/{legacy_id}", base=self.web_api)

    def get_game_chat(self, game_id: str, limit: int = 50) -> dict:
        return self._get(
            f"/chat/game/live/{game_id}/observers/messages?limit={limit}",
            base=self.web_api)

    def send_game_message(self, game_id: str, content: str) -> dict:
        data = {
            "content": content
        }
        return self.session.post(
            f"{self.web_api}/chat/game/live/{game_id}/observers/messages?uid={self.user_id}",
            json=data).json()
