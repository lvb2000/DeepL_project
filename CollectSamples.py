import subprocess

# define docker command
docker_command = 'docker run --gpus all --shm-size=30g pydreamer --configs defaults atari --batch_size 8 --data_workers 0 --n_env_steps 10_000_000'

# list games to train
games = ['Atari-Air_Raid',
         'Atari-Assault',
         'Atari-BattleZone',
         'Atari-BeamRider',
         'Atari-Berzerk',
         'Atari-Breakout',
         'Atari-Centipede',
         'Atari-Darkchambers',
         'Atari-Defender',
         'Atari-DemonAttack',
         'Atari-Entombed',
         'Atari-Galaxian',
         'Atari-Pong',
         'Atari-Pooyan',
         'Atari-RIverRaid',
         'Atari-Robotank',
         'Atari-Seaquest',
         'Atari-SpaceInvaders',
         'Atari-SpaceWar',
         'Atari-StarGunner'
]

# init commands with directory change
#commands = ['cd D:\\DeepL_project\\pydreamer\\']
commands = ['conda activate dreamerV2']
# concat commands and games
for game in games:
    commands.append(docker_command + ' --env_id ' + game)

shell = 'powershell'

for idx,command in enumerate(commands):
    if idx>1:
        break
    # run command
    proc = subprocess.Popen([shell,command],stdout=subprocess.PIPE)
    proc.wait()
    print(f'Finished {idx} game.')
