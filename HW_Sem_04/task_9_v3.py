import asyncio
import aiohttp
import argparse
import time
import os

IMAGE_DIR = 'images'
image_urls = [
    'https://img3.fonwall.ru/o/yi/beach-landscape-sea-coast-liek.jpeg',
    'https://img3.fonwall.ru/o/sx/portrait-girl-neural-network-jehg.jpg',
    'https://i.7fon.org/1000/z162178.jpg',
    'https://i.7fon.org/1000/r1638851.jpg',
    'https://cdn1.ozone.ru/s3/multimedia-l/6106905441.jpg',
    'https://zastavok.net/main/animals/1436664361.jpg'
]


async def loading_image(url, target_dir: str):
    start_process_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            filename = url.split('/')[-1]
            with open(os.path.join(target_dir, filename), 'wb') as img:
                img.write(data)
            print(f"Изображение загружено с <<{url}>> за {time.time() - start_process_time:.2f} сек")


async def main():
    tasks = []
    for img_url in urls:
        tasks.append(asyncio.create_task(loading_image(img_url, IMAGE_DIR)))
    await asyncio.gather(*tasks)


def parse():
    parser = argparse.ArgumentParser(description='Загружает изображения из заданного списка URL-адресов')
    parser.add_argument('-u', '--urls', nargs='+', type=str, help='URL-адреса вводить через пробел')
    return parser.parse_args()


if __name__ == '__main__':
    urls = parse().urls or image_urls
    if not os.path.exists(IMAGE_DIR):
        os.mkdir(IMAGE_DIR)
    start_time = time.time()
    asyncio.run(main())
    print(f'Общее время загрузки (асинхронный подход) => {time.time() - start_time:.2f} сек')
