import cpu_strats

choices = ["rock", "paper", "scissors"]
choice_menu ="\n\
0 - Rock\n\
1 - Paper\n\
2 - Scissors\n\
"


def score(winner):
  global cpu_score
  global usr_score
  # tests if variables are called for first time
  try:
    cpu_score
    usr_score
  except NameError:
    cpu_score = 0
    usr_score = 0

  if winner == "cpu":
    cpu_score += 1
  elif winner == "usr":
    usr_score += 1
  elif winner == "tie":
    pass
  return [cpu_score, usr_score]

def input_func():
  # user input
  try:
    print(choice_menu)
    usr_input = int(input("Enter a number: "))
    usr_input = choices[usr_input]
  except:
    print('Enter a valid input.')
    hold = input_func()
    return hold
  else:
    return usr_input

def determine_winner(cpu, usr):
  # tie
  if cpu == usr:
    print("\nTie!\n")
    print('USR:', usr)
    print('CPU:', cpu, '\n')
    return "tie"
  # cpu wins, usr loses
  elif (cpu == "rock" and usr == "scissors") or (cpu == "paper" and usr == "rock") or (cpu == "scissors" and usr == "paper"):
    print("\nCPU wins!\n")
    print('USR:', usr)
    print('CPU:', cpu, '\n')
    return "cpu"
  # usr wins, cpu loses
  elif (usr == "rock" and cpu == "scissors") or (usr == "paper" and cpu == "rock") or (usr == "scissors" and cpu == "paper"):
    print("\nUser wins!\n")
    print('USR:', usr)
    print('CPU:', cpu, '\n')
    return "usr"
  else:
    print("Unable to determine winner.")

def start():
  usr_input = input_func()
  cpu_guess = cpu_strats.always_win(usr_input)
  cpu_strats.log_usr_input(usr_input)
  winner = determine_winner(cpu_guess, usr_input)

  # score-keeping
  scores = score(winner)
  print("USER:", scores[1], "\nCPU:", scores[0])
  start()
start()
