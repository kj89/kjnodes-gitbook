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
peers="d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,3f9a20277d68b7fe52efbe84dad231af472d0190@162.55.235.69:29656,eb69783b7e38059a58abaf342eb64f704de37636@23.88.66.239:31656,31e4e58aed75f099eb5b71fd9fd48b48e4bf721a@5.75.170.207:26656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,c1d2d254a903b58692046b573dd06d2aa629266c@65.109.156.208:02656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,4ff3241de49fa01129b3fe38b3aeefc699f07cc7@58.187.173.207:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,4a8c845bdffc8bae0ed0e91a476bc57720adec15@65.108.206.74:26656,706f4ef87ae9c3b83fb48dcae1b10255f8f7dfa4@116.202.227.117:52656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,856ac01afa0163c27b69e1b25464427310120924@85.25.134.23:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,69a83a484a8e47a4a25f833aea64b3dbec51bb2b@68.118.40.145:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
