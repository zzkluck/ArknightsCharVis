import json
import wget
from typing import List, NamedTuple
from pathlib import Path
from urllib.error import HTTPError
import logging

logging.basicConfig(level=logging.INFO)

CHAR_DATA = NamedTuple('CHAR_DATA', [('attack', int), ('defence', int), ('maxHp', int), ('image_path', str)])
ASSETS_DIR = Path("./assets")
CHAR_TABLE_PATH = ASSETS_DIR / "character_table.json"
BATTLE_EQUIP_PATH = ASSETS_DIR / "battle_equip_table.json"
IMAGE_DIR = ASSETS_DIR / "images"
CHAR_TABLE_WEB_URL = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json"
BATTLE_EQUIP_WEB_URL = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/battle_equip_table.json"
IMAGE_WEB_URL = "https://raw.githubusercontent.com/yuanyan3060/ArknightsGameResource/main/avatar"

def fetch_char_data() -> List[CHAR_DATA]:
    # 创建assets目录结构
    ASSETS_DIR.mkdir(exist_ok=True)
    IMAGE_DIR.mkdir(exist_ok=True)

    # 如果本地找不到character_table.json干员信息配置文件，从ArknightsGameData项目获取
    if not CHAR_TABLE_PATH.exists():
        wget.download(CHAR_TABLE_WEB_URL, CHAR_TABLE_PATH.absolute().as_posix())
    with CHAR_TABLE_PATH.open('r', encoding='utf-8')as f:
        char_table_json = json.load(f)

    # 如果本地找不到battle_equip_table.json模组信息配置文件，从ArknightsGameData项目获取   
    if not BATTLE_EQUIP_PATH.exists():
        wget.download(BATTLE_EQUIP_WEB_URL, BATTLE_EQUIP_PATH.absolute().as_posix())
    with BATTLE_EQUIP_PATH.open('r', encoding='utf-8')as f:
        equip_data_json = json.load(f)

    attributeType = {0:'maxHp', 1:'atk', 2:'def'}
    char_table = {}
    for key, info in char_table_json.items():
        # "char_245_cello": { "name": "塑心", ... }
        char_key = key.split('_')[-1]
        # 跳过不能精英二的干员
        if len(info['phases']) < 3:
            continue

        # 下载头像
        image_path = IMAGE_DIR / f"{info['name']}.png"
        if not image_path.exists():
            try:
                wget.download(f"{IMAGE_WEB_URL}/{key}_2.png", image_path.absolute().as_posix(), bar=None)
                logging.info(f"Downloaded {key}_2:{info['name']}.")
            except HTTPError:
                try:
                    wget.download(f"{IMAGE_WEB_URL}/{key}.png", image_path.absolute().as_posix())
                    logging.info(f"Downloaded {key}:{info['name']}.")
                except HTTPError:
                    logging.warning(f"Cant't find image {key}:{info['name']}.")
                
        # 基础
        status = info['phases'][-1]['attributesKeyFrames'][-1]
        char_status = {'maxHp': status['data']['maxHp'],
                    'atk': status['data']['atk'],
                    'def': status['data']['def'],
                    'name': info['name'],
                    'profession': info['profession']}

        # 潜能
        potential = info['potentialRanks']
        for p in potential:
            if p['buff'] is not None:
                for p_modifier in p['buff']['attributes']['attributeModifiers']:
                    if p_modifier['attributeType'] in attributeType:
                        char_status[attributeType[p_modifier['attributeType']]] += p_modifier['value']

        # 信赖
        if info['favorKeyFrames'] is not None:
            favor = info['favorKeyFrames'][-1]['data']
            for f in favor:
                if f in char_status:
                    char_status[f] += favor[f]
        char_table[char_key] = char_status

    # 模组
    for equip_name, equip_info in equip_data_json.items():
        char_name = equip_name.split('_')[-1]
        if char_name in char_table:
            char_info = char_table[char_name]
            attributeBlackboard = equip_info['phases'][-1]['attributeBlackboard']
            for kv in attributeBlackboard:
                if kv['key'] in char_info:
                    char_info[kv['key']] += kv['value']
                elif kv['key'] == 'max_hp':
                    char_info['maxHp'] += kv['value']

    return [(c['atk'], c['def'], c['maxHp'], f"assets/images/{c['name']}.png") for c in char_table.values()]

if __name__ == "__main__":
    fetch_char_data()