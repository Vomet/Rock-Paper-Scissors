from random import randint

def log_usr_input(usr_input = None):
  global usr_input_log
  # checks if usr_input_log exists
  try:
    usr_input_log
  except NameError:
    usr_input_log = []
  # if usr_input = None, then return log
  if usr_input == None:
    return usr_input_log

  usr_input_log.append(usr_input)
  return usr_input_log

choices = ["rock", "paper", "scissors"]
# randomly picks
def random():
  return choices[randint(0, 2)]
# mirrors previous usr_input
def mirror():
  usr_input_list = log_usr_input()
  
  try:
    last_input = usr_input_list[-1]
  # checks if this is first time usr is playing
  except IndexError:
    random_guess = random()
    return random_guess
  return last_input
# counters previous usr_input
def beat_last():
  last_input = mirror()
  if last_input == "rock":
    return "paper"
  elif last_input == "paper":
    return "scissors"
  elif last_input == "scissors":
    return "rock"
# counters beat_last()
def counter_beat_last():
  b_l = beat_last()
  if b_l == "rock":
    return "paper"
  elif b_l == "paper":
    return "scissors"
  elif b_l == "scissors":
    return "rock"

# cpu will always win. chooses after usr_input
def always_win(usr_input):
  if usr_input == "rock":
    return "paper"
  elif usr_input == "paper":
    return "scissors"
  elif usr_input == "scissors":
    return "rock"
