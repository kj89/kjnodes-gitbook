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

**live-peers** (33)
```bash
peers="6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,6655b2be870706c16d417ab15dd82a60fda0a0bd@78.46.61.117:01656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,29dbc6241210d67e3460e2994e803bb2695dd71a@27.79.250.190:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,26e70e13195b0d04cda0fca1f7b16b8746a620ed@65.109.28.226:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
