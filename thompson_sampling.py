from numpy.random import beta
import matplotlib.pyplot as plt
from Arm import Arm

# Thompson Samplingでは、アームを一回引く度にパラメータの事後分布を更新する。
# ここでパラメータと言っているのはコインの表の出る確率のこと（ベルヌーイ分布のパラメータ）。これは問題設定によっていろいろ変わる。
# 今は明示的に0.5とか0.4とか設定してるが、アームを引く人は分からない。
# パラメータの事前分布はbeta(1,1)とする。事後分布はbeta(1+arm.success, 1+arm.fail)となる。

def thompson_sampling(arms, T):
    reward = 0
    reward_hist = []

    for i in range(1, T+1):
        rand_gened_params = [beta(a=arm.success+1, b=arm.fail+1) for arm in arms]
        max_index = rand_gened_params.index(max(rand_gened_params))
        reward += arms[max_index].play()
        reward_hist.append(reward/i)

    plt.plot(reward_hist)
    plt.savefig('Thompson_Sampling.png')
    print('Reward: ' + str(reward))

if __name__ == "__main__":
    arms = [Arm(0.3) for i in range(4)]
    arms.append(Arm(0.5))
    thompson_sampling(arms=arms, T=10**3)
