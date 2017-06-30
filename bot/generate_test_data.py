import requests
import json
import time
import random

def send_to_kairosdb(data, timestamp):
    ''' send results to kairosdb '''
    #timestamp         = int(time.time()*1000)
    data['timestamp'] = timestamp
    kairosdb_server   = 'http://localhost:14480/api/v1/datapoints'
    headers           = {'Content-Type': 'application/json'}
    response          = requests.post(kairosdb_server, json.dumps([data]), headers=headers)

    return response.status_code


def stats_collector(message, timestamp):
    ''' takes discord message object and sends data to kairosdb '''
    stats = []

    # Count messages
    stats.append({
        'name': 'discord.stats.message_count',
        'value': 1.0,
        'tags': {
            'channel': message['channel'],
            'server' : message['server'],
            'author' : message['author']
        }
    })

    # Count words per message
    stats.append({
        'name': 'discord.stats.word_count',
        'value': message['content'],
        'tags': {
            'channel': message['channel'],
            'server' : message['server'],
            'author' : message['author']
        }
    })

    for stat in stats:
        send_to_kairosdb(stat, timestamp)

    return True


if __name__ == '__main__':
    generate_5minute_time_data = [int(time.time()*1000)-x*1000 for x in range(300, 0, -1)]
    for timestamp in generate_5minute_time_data:
        random.seed = random.randint(1000000, 1001001)
        message = {}
        message['server']  = 'mydiscordserver'
        message['channel'] = random.choice(['general', 'random', 'catgifs'])
        message['author']  = random.choice(['Luke', 'Leia', 'Vader', 'Chewbacca', 'Solo', 'Yoda','Fett', 'Kenobi', 'R2D2', 'C-3PO', 'Jabba', 'Lando', 'Ackbar', 'Greedo'])
        message['content'] = random.randint(1, 150)
        stats_collector(message, timestamp)
        print(message)
