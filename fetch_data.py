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
ENEMY_DATABASE_PATH = ASSETS_DIR / "enemy_database.json"

IMAGE_DIR = ASSETS_DIR / "images"
CHAR_AVATAR_DIR = IMAGE_DIR / "char"
ENEMY_AVATAR_DIR = IMAGE_DIR / "enemy"

CHAR_TABLE_WEB_URL = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json"
BATTLE_EQUIP_WEB_URL = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/battle_equip_table.json"
ENEMY_DATABASE_WEB_URL = "https://github.com/Kengxxiao/ArknightsGameData/raw/master/zh_CN/gamedata//levels/enemydata/enemy_database.json"
AVATAR_WEB_URL = "https://raw.githubusercontent.com/yuanyan3060/ArknightsGameResource/main/avatar"
ENEMY_AVATAR_WEB_URL = "https://raw.githubusercontent.com/yuanyan3060/ArknightsGameResource/main/enemy"

def fetch_char_data() -> List[CHAR_DATA]:
    ASSETS_DIR.mkdir(exist_ok=True)
    CHAR_AVATAR_DIR.mkdir(exist_ok=True, parents=True)

    if not CHAR_TABLE_PATH.exists():
        wget.download(CHAR_TABLE_WEB_URL, CHAR_TABLE_PATH.absolute().as_posix())
    with CHAR_TABLE_PATH.open('r', encoding='utf-8')as f:
        char_table_json = json.load(f)

    
    if not BATTLE_EQUIP_PATH.exists():
        wget.download(BATTLE_EQUIP_WEB_URL, BATTLE_EQUIP_PATH.absolute().as_posix())
    with BATTLE_EQUIP_PATH.open('r', encoding='utf-8')as f:
        equip_data_json = json.load(f)

    attributeType = {0:'maxHp', 1:'atk', 2:'def'}
    char_table = {}
    for key, info in char_table_json.items():
        char_key = key.split('_')[-1]
        if len(info['phases']) < 3:
            continue

        # 下载头像
        image_path = CHAR_AVATAR_DIR / f"{info['name']}.png"
        if not image_path.exists():
            try:
                wget.download(f"{AVATAR_WEB_URL}/{key}_2.png", image_path.absolute().as_posix(), bar=None)
                logging.info(f"Downloaded {key}_2:{info['name']}.")
            except HTTPError:
                try:
                    wget.download(f"{AVATAR_WEB_URL}/{key}.png", image_path.absolute().as_posix())
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

    return [(c['atk'], c['def'], c['maxHp'], (CHAR_AVATAR_DIR / f"{c['name']}.png").as_posix()) for c in char_table.values()]

def fetch_enemy_data(download_images: bool=True) -> List[CHAR_DATA]:
    ASSETS_DIR.mkdir(exist_ok=True)
    ENEMY_AVATAR_DIR.mkdir(exist_ok=True, parents=True)

    if not ENEMY_DATABASE_PATH.exists():
        wget.download(ENEMY_DATABASE_WEB_URL, ENEMY_DATABASE_PATH.absolute().as_posix())
    with ENEMY_DATABASE_PATH.open('r', encoding='utf-8')as f:
        enemy_database_json = json.load(f)
    enemy_data_json = enemy_database_json['enemies']
    enemy_table = {}
    for e_dict in enemy_data_json:
        key = e_dict['Key']
        if len(e_dict['Value']) == 0:
            logging.warning(f"Enemy {key} doesn't have infomation dict.")
            continue

        info = e_dict['Value'][0]
        enemy_status = {
            'maxHp': info['enemyData']['attributes']['maxHp']['m_value'],
            'atk': info['enemyData']['attributes']['atk']['m_value'],
            'def': info['enemyData']['attributes']['def']['m_value'],
            'name': info['enemyData']['name']['m_value']
            }
        enemy_table[key] = enemy_status

        if len(e_dict['Value']) == 1:
            logging.info(f"Enemy {enemy_status['name']} doesn't have multi levels.")

        # 下载头像
        if download_images:
            image_path = ENEMY_AVATAR_DIR / f"{enemy_status['name']}.png"
            if not image_path.exists():
                try:
                    wget.download(f"{ENEMY_AVATAR_WEB_URL}/{key}.png", image_path.absolute().as_posix(), bar=None)
                    logging.info(f"Downloaded {key}:{enemy_status['name']}.")
                except HTTPError:
                    logging.warning(f"Cant't find image {key}:{enemy_status['name']}.")
    return [(e['atk'], e['def'], e['maxHp'], (ENEMY_AVATAR_DIR / f"{e['name']}.png").as_posix()) for e in enemy_table.values()]



