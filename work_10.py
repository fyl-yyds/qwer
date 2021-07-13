import torch
import random
import matplotlib.pyplot as plt
from torch import optim
from torch import  nn

xs=torch.unsqueeze(torch.range(-20,20),dim=1)
ys=[e.pow(3)*random.randint(1,6) for e in xs]
ys=torch.stack(ys)

class line(nn.Module):
    def __init__(self):
        super(line, self).__init__()
        self.layer=nn.Sequential(
            nn.Linear(1,20),
            nn.ReLU(),
            nn.Linear(20,64),
            nn.ReLU(),
            nn.Linear(64,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,1)
        )
    def forward(self,x):
        return self.layer(x)

if __name__ == '__main__':
    net=line()
    opt=optim.Adam(net.parameters())
    loss_fun=nn.MSELoss()
    plt.ion()
    for epoch in range(100000):
        out=net.forward(xs)
        loss=loss_fun(out,ys)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if epoch%5==0:
            plt.cla()
            print(loss.item())
            plt.plot(xs,ys,'.')
            plt.plot(xs,out.detach().numpy())
            plt.pause(0.001)
            print("loss=%.4f"%loss.item())
    plt.ioff()
    plt.show()

