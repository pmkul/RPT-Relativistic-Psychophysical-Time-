
import numpy as np

c = 299_792_458.0

def run_demo(T_total=1800.0, dt=0.5, alpha=0.6, beta=-0.3, gamma=0.5, seed=42):
    rng = np.random.default_rng(seed)
    t = np.arange(0, T_total, dt)
    n = t.size
    v = np.zeros(n)
    v[(t>=0)&(t<600)] = 1.0
    v[(t>=600)&(t<1200)] = 0.8*c
    v[(t>=1200)&(t<1800)] = 1.0
    g=9.80665
    h = np.zeros(n)
    h[(t>=600)&(t<1200)] = 100.0*((t[(t>=600)&(t<1200)]-600.0)/600.0)
    Phi = g*h
    gamma_rel = 1.0/np.sqrt(1.0-(v/c)**2+1e-18)
    d_tau = dt*(1.0+Phi/c**2)/gamma_rel
    tau = np.cumsum(d_tau)
    I = np.zeros(n)
    pulse_times = rng.choice(n, size=20, replace=False)
    I[pulse_times] = rng.uniform(2.0, 4.0, size=20)
    kernel = np.exp(-np.linspace(0,5,50)); kernel/=kernel.sum()
    I = np.convolve(I, kernel, mode='same')
    C = np.zeros(n)
    C[(t>=200)&(t<500)] = 0.6
    C[(t>=900)&(t<1300)] = 0.9
    C[(t>=1400)&(t<1650)] = 0.3
    A = 0.3 + 0.6*(I/(I.max()+1e-9)) + rng.normal(0,0.03,size=n)
    A = np.clip(A, 0.05, None)
    Lambda = 1.0 + alpha*I + beta*C + gamma*A
    dT = Lambda * d_tau
    T = np.cumsum(dT)
    return T, tau, Lambda
