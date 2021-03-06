# =======================================================
# Hidden Markov Models with Gaussian emissions
# =======================================================
# Ning Ma, University of Sheffield 
# n.ma@sheffield.ac.uk

import numpy as np
from sklearn.mixture import GaussianMixture

class HMM:
    """ A left-to-right no-skip Hidden Markov Model with Gaussian emissions

    Attributes:
        num_states: total number of HMM states (including two non-emitting states)
        states: a list of HMM states
        log_transp: transition probability matrix (log domain): a[i,j] = log_transp[i,j]
    """

    def __init__(self, num_states=3, num_mixtures=1, self_transp=0.9):
        """Performs GMM evaluation given a list of GMMs and utterances

        Args:
            num_states: number of emitting states
            num_mixture: number of Gaussian mixture components for each state
            self_transp: initial self-transition probability for each state
        """
        self.num_states = num_states
        self.states = [GaussianMixture(n_components=num_mixtures, covariance_type='diag', 
            init_params='kmeans', max_iter=10) for state_id in range(self.num_states)]

        # Initialise transition probability for a left-to-right no-skip HMM   
        # For a 3-state HMM, this looks like
        #   [0.9, 0.1, 0. ],
        #   [0. , 0.9, 0.1],
        #   [0. , 0. , 0.9]
        self.transp = np.diag((1-self_transp)*np.ones(self.num_states-1,),1) + np.diag(self_transp*np.ones(self.num_states,))

        # Deal with log(0)...
        #offset = 0.01
        #mask = self.transp == 0
        #self.transp[mask] = offset
        #self.transp[np.logical_not(mask)] = offset/(self.num_states-1)

        # Finally take the log
        self.log_transp = np.log(self.transp)


    def viterbi_decoding(self, obs):
        """Performs Viterbi decoding

        Args:
            obs: a sequence of observations [T x dim]
            
        Returns:
            log_prob: log-likelihood
            state_seq: most probable state sequence
        """

        # Length of obs sequence
        T = obs.shape[0]

        # Precompute log output probabilities [num_states x T]
        log_outp = np.array([self.states[state_id].score_samples(obs).T for state_id in range(self.num_states)])

        # Initial state probs PI
        initial_dist = np.zeros(self.num_states) # prior prob = log(1) for the first state
        initial_dist[1:] = -float('inf') # prior prob = log(0) for all the other states

        # Back-tracing matrix [num_states x T]
        back_pointers = np.zeros((self.num_states, T), dtype='int')

        # -----------------------------------------------------------------
        # INITIALISATION
        # YOU MAY WANT TO DEFINE THE DELTA VARIABLE AS A MATRIX INSTEAD 
        # OF AN ARRAY FOR AN EASIER IMPLEMENTATION.
        # -----------------------------------------------------------------
        # Initialise the Delta probability (Viterbi matrix) 
        v = log_outp[:,0] + initial_dist # Stores the last column of the viterbi matrix
        new_v = np.zeros(self.num_states) # Stores the new transitions probs

        # -----------------------------------------------------------------
        # RECURSION
        # -----------------------------------------------------------------
        for t in range(1, T):

            # STEP 1. Add all transitions to previous best probs

            # STEP 2. Select the previous best state from all transitions into a state

            # STEP 3. Record back-trace information in back_pointers

            # STEP 4. Add output probs to previous best probs


        # -----------------------------------------------------------------
        # SAVE THE GLOBAL LOG LIKELIHOOD IN log_prob AS A RETURN VALUE.
        # THE GLOBAL LOG LIKELIHOOD WILL BE THE VALUE FROM THE LAST STATE 
        # AT TIME T (THE LAST FRAME).
        # -----------------------------------------------------------------
        log_prob = v[-1] # Likelihood is locatd at the finishing state



        # -----------------------------------------------------------------
        # BACK-TRACING: SAVE THE MOST PROBABLE STATE SEQUENCE IN state_seq
        # AS A RETURN VALUE.
        # -----------------------------------------------------------------
        # Allocate state_seq for saving the best state sequence
        state_seq = np.zeros((T,), dtype='int')

        # Make sure we finish in the last state
        state_seq[:] = self.num_states - 1
        
        # ====>>>>
        # ====>>>> FILL WITH YOUR CODE HERE FOR BACK-TRACING
        # ====>>>>


        # -----------------------------------------------------------------
        # RETURN THE OVERAL LOG LIKELIHOOD log_prob AND THE MOST PROBABLE
        # STATE SEQUENCE state_seq
        # YOU MAY WANT TO CHECK IF THE STATE SEQUENCE LOOKS REASONABLE HERE
        # E.G. FOR A 5-STATE HMM IT SHOULD LOOK SOMETHING LIKE
        #     0 0 0 0 1 1 1 2 2 2 2 3 3 3 3 3 3 3 4 4
        # -----------------------------------------------------------------
        return log_prob, state_seq


