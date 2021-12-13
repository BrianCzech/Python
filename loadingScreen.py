import time
from tqdm import tqdm

print('Prepare for hacking')
def loading():
    for _ in tqdm(range(100), desc='Loading...',ascii=False, ncols=75):
        time.sleep(0.01)
    print('Hacking Successful!')

if __name__ =='__main__':
    loading()