#### Computes an optimal Markov Decision Process (MDP) policy using value iteration.####

Input to the program is an MDP object that has the following functions: 
* mdp.S(): Returns a finite set of states, which you can assume will be hashable.
* mdp.A(): Returns a finite set of actions, which you can assume will be hashable.
* mdp.R(s): Accepts a state and returns the reward for visiting that state.
* mdp.P(s, a, u): Returns the probability of transitioning from state s to state u when taking action a.
* mdp.gamma(): Returns the discount factor that you can assume is in (0, 1).
