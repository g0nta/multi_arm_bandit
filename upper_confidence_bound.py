from Arm import Arm
import math

def __init(arms):
    for arm in arms:
        arm.success = 1
    return arms

def __get_score(arm, t):
    ucb = math.sqrt(2*math.log(t) / (arm.success + arm.fail))
    return arm.success / (arm.success + arm.fail) + ucb

def UCB(arms, T):
    __init(arms)
    reward = 0

    for i in range(1, T+1):
        scores = [__get_score(arm, i) for arm in arms]
        max_score_index = scores.index(max(scores))
        reward += arms[max_score_index].play()
    return reward

if __name__=="__main__":
    arms = [Arm(0.3) for i in range(4)]
    arms.append(Arm(0.5))
    UCB(arms=arms, T=10**3)