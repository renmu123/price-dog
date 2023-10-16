from src import MasadoraSuruga, Task, Suruga, scheduler, server
from lxml import etree
import json


def test():
    suruga = Suruga()
    data = suruga.get_response("438009073")
    # print(data.text)
    root = etree.HTML(data.content)
    el = root.xpath("//script[@type='application/ld+json']")[1]
    data = json.loads(el.text)
    print(data)


def main():
    suruga = MasadoraSuruga()
    # data = suruga.parse("602247898")

    scheduler.add_job(suruga.parse, "interval", minutes=1, args=["602247898"])
    print("start")
    scheduler.start()
    # try:
    #     # 让程序一直运行，直到手动停止
    #     while True:
    #         pass
    # except (KeyboardInterrupt, SystemExit):
    #     # 捕获Ctrl+C或系统退出信号，然后停止调度器
    #     scheduler.shutdown()
    # task = Task("masadora", "602247898")


if __name__ == "__main__":
    # main()
    server()
