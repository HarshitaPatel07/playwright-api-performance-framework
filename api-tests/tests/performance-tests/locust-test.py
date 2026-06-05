import random
import logging

from locust import HttpUser, task, between

from config import BASE_URL
from tests.data.user_data import create_user_payload, update_user_payload

logger = logging.getLogger(__name__)


class UsersPerformanceUser(HttpUser):
    """Locust user that exercises the Users API endpoints."""

    host = BASE_URL
    wait_time = between(1, 3)

    def on_start(self):
        self.user_ids = []
        self._bootstrap_users(count=2)

    def on_stop(self):
        for user_id in list(self.user_ids):
            self._delete_user(user_id)

    def _bootstrap_users(self, count: int = 2):
        for _ in range(count):
            self._create_user()

    def _create_user(self):
        payload = create_user_payload()
        with self.client.post("/users", json=payload, name="/users", catch_response=True) as response:
            if response.status_code == 201:
                data = response.json()
                self.user_ids.append(data["id"])
            else:
                response.failure(
                    f"Create user failed: {response.status_code} {response.text}"
                )

    def _delete_user(self, user_id: int):
        with self.client.delete(f"/users/{user_id}", name="/users/[id]", catch_response=True) as response:
            if response.status_code in (204, 404):
                if user_id in self.user_ids:
                    self.user_ids.remove(user_id)
            else:
                response.failure(
                    f"Delete user failed: {response.status_code} {response.text}"
                )

    @task(4)
    def list_users(self):
        with self.client.get("/users", name="/users", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(
                    f"List users failed: {response.status_code} {response.text}"
                )

    @task(3)
    def get_user_by_id(self):
        if not self.user_ids:
            self._create_user()
            return

        user_id = random.choice(self.user_ids)
        with self.client.get(f"/users/{user_id}", name="/users/[id]", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(
                    f"Get user by id failed: {response.status_code} {response.text}"
                )

    @task(2)
    def create_user(self):
        self._create_user()

    @task(1)
    def update_user(self):
        if not self.user_ids:
            self._create_user()
            return

        user_id = random.choice(self.user_ids)
        payload = update_user_payload()
        with self.client.patch(f"/users/{user_id}", json=payload, name="/users/[id]", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(
                    f"Update user failed: {response.status_code} {response.text}"
                )

    @task(1)
    def delete_user_task(self):
        if not self.user_ids:
            self._create_user()
            return

        user_id = self.user_ids[0]
        self._delete_user(user_id)
