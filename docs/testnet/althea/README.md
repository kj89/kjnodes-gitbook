# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" width="150" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:52090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:52656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:52659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (42)
```bash
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,13747f1f9960d19b72610cf7b59c2ec6d4eca27f@103.107.183.89:52656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,53a4fe2e8eb17b307dfed6a88cbe5573617e34b5@89.71.164.109:28656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,4a8c845bdffc8bae0ed0e91a476bc57720adec15@65.108.206.74:26656,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,4ff3241de49fa01129b3fe38b3aeefc699f07cc7@58.187.173.207:26656,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,26e70e13195b0d04cda0fca1f7b16b8746a620ed@65.109.28.226:26656,9ec70a79ddb2956f3d5e70bf74635f1500712b94@66.172.36.137:14656,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656,c1d2d254a903b58692046b573dd06d2aa629266c@65.109.156.208:02656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
