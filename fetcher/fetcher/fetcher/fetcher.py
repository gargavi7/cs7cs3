import asyncio
import requests
import json
import yaml


class NotImplementedError(Exception):
    pass


async def run_worker(src):
    raise NotImplementedError()


class MockApi(object):
    response_id = 0

    def __init__(self, interval=1, prob_failure=0):
        self.interval = 1
        self.prob_failure = prob_failure

    async def get(self, request):
        await asyncio.sleep(self.interval)
        MockApi.response_id += 1
        return json.loads("{\"response_id\": %d}" % (MockApi.response_id-1))


class Worker(object):
    def __init__(self, data_source, api_fetcher=MockApi()):
        self.data_source = data_source
        self.interval = 1
        self.api_fetcher = api_fetcher

    async def run(self):
        for itcount in range(int(1e9)):
            print("itcount={}".format(itcount))
            response = await self.fetch_once()
            print("run: response={}".format(response))
            await self.store_data(None, response)
            self.process_new_data(None, response)
            await asyncio.sleep(self.interval)

    def process_new_data(self, request, response):
        print("process_new_data {} {}".format(request, response))

    async def fetch_once(self):
        print("Fetching data from {}".format(self.data_source))
        request = self.data_source.url
        response = await self.api_fetcher.get(request)
        # response = await asyncio.sleep(1)
        print("Hello, world!")
        response = response.json()
        print("Response for {}: {}".format(request, response))
        return (request, response)

    async def store_data(self, request, response):
        print("request={}".format(request))
        print("response={}".format(response))
        print("(Stored.)")


class DataSource(object):
    def __init__(self, name, spec):
        print("name={}".format(name))
        print("spec={}".format(spec))
        self.name = name
        self.url = spec["url"]

    @staticmethod
    def get_all_data_sources():
        ans = []
        with open("known_data_sources.yaml") as f:
            specs = yaml.load(f.read())
            for name, spec in specs.items():
                ans.append(DataSource(name, spec))
        return ans


class ExternalFetcher(object):
    def __init__(self):
        self.data_sources = DataSource.get_all_data_sources()

    async def main(self):
        tasks = []
        for src in self.data_sources:
            tasks.append(Worker(src).run())
        await asyncio.gather(*tasks)
        # tasks = []
        # loop = asyncio.get_event_loop()
        # for src in self.data_sources:
        #     worker = Worker(src)
        #     tasks.append(loop.create_task(worker.run()))
        # await asyncio.sleep(3600)


def main():
    fetcher = ExternalFetcher()
    # asyncio.run(fetcher.main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetcher.main())
    loop.close()


if __name__ == "__main__":
    main()
