import os
import random
import requests

map_api = "https://cat-match.easygame2021.com/sheep/v1/game/map_info?map_id=%s"

finish_api = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=%s&rank_time=%s&rank_role=1&skin=1"

CONFIG = {
    "header_t": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQzNTQ2NjgsIm5iZiI6MTY2MzI1MjQ2OCwiaWF0IjoxNjYzMjUwNjY4LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjoxMTY0MDc4MzAsImRlYnVnIjoiIiwibGFuZyI6IiJ9.xnOgJByCm01faaI9NgUYpMKtMH2ehxXBnb-oPbK5wy8",
    "header_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN",
}


def finish_game(state, rank_time):
    return True
    request_header = {
        "Host": "cat-match.easygame2021.com",
        "User-Agent": CONFIG["header_user_agent"],
        "t": CONFIG["header_t"],
    }
    res = requests.get(finish_api % (state, rank_time), headers=request_header)

    if res.json()["err_code"] == 0:    # 0 -> success 
        print("状态update成功")
        return True
    else:
        print(res.json())
        print("double check head_t param in Stream")
        return False

def game_over(header_t=CONFIG["header_t"], header_user_agent=CONFIG["header_user_agent"]):
    time = random.randint(1, 1800)
    err = finish_game(1, time)
    print("羊了个羊闯关结束, 耗时{} s".format(time))
    return err, time