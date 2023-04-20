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

**live-peers** (39)
```bash
peers="ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,eb69783b7e38059a58abaf342eb64f704de37636@23.88.66.239:31656,3f9a20277d68b7fe52efbe84dad231af472d0190@162.55.235.69:29656,31e4e58aed75f099eb5b71fd9fd48b48e4bf721a@5.75.170.207:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,93fa6dee174ed6f119223542ed0f622087adab7e@24.199.116.190:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,c1d2d254a903b58692046b573dd06d2aa629266c@65.109.156.208:02656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,a544cb496604839c93ace95167d90a5497e520fc@86.48.2.235:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,a7b4e2ab0e3334bd2986c09cd5dafbc938ef23bf@65.108.78.101:52656,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,766377592cbaae65d8e6df5120bd8b4fdfc8a372@98.63.20.2:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:12456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
