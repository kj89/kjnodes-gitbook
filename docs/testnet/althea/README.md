# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:15290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:15256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:15259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (38)
```bash
peers="856ac01afa0163c27b69e1b25464427310120924@85.25.134.23:26656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,7a69ca211e4dca2c8c5e5ad2582e81db6adb9f3c@65.108.70.119:29656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,4ff3241de49fa01129b3fe38b3aeefc699f07cc7@42.119.159.212:26656,93fa6dee174ed6f119223542ed0f622087adab7e@24.199.116.190:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
