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

**live-peers** (20)
```bash
peers="2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,ab3ba67d06d109e135f5cd22a3d4d6b1784e3a70@161.97.65.170:36656,eab7a70812ba39094fc8bbf4f69f099123863b38@81.30.157.35:11656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,a81cf8f7f330e2e09bec93c866214f7b3b336849@65.109.87.88:26356,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
