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

**live-peers** (37)
```bash
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,29dbc6241210d67e3460e2994e803bb2695dd71a@27.79.176.141:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,ab3ba67d06d109e135f5cd22a3d4d6b1784e3a70@161.97.65.170:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
