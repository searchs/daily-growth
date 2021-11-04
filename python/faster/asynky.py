from collections import namedtuple
from datetime import datetime
import asyncio
import json

host = "api.github.com"
request_template = """\
  GET /users/{{}} HTTP/1.1
  Host: {}
  User-Agent: python/asyncio
  Connection: Close
  """.format(
    host
)

User = namedtuple("User", "login name joined")


async def user_info_aio(login, acc):
    """Get user information from Github"""
    reader, writer = await asyncio.open_connection(host, 443, ssl=True)
    request = request_template.format(login)
    writer.write(request.encode("utf-8"))

    in_body = False
    body = []

    async for line in reader:
        if line[:1] == b"{":
            in_body = True
            body.append(line)
        elif in_body:
            body.append(line)

        body = b"\n".join(body)
        body = body.decode("utf-8")
        reply = json.loads(body)

        joined = datetime.strftime(reply["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        acc.append(User(login, reply["name"], joined))


def users_info_aio(usernames):
    """Get information for several users from Github API"""
    users = []

    def make_task(login):
        return asyncio.ensure_future(user_info_aio(login, users))

    tasks = [make_task(login) for login in usernames]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    return users


if __name__ == "__main__":
    logins = [
        "gvanrossum",
        "wesm",
        "searchs",
        "torvalds",
    ]
