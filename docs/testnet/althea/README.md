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

**live-peers** (15)
```bash
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,c831cd6ac278ab971eca94dda0c29191e8f39036@195.201.22.133:26656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,31e4e58aed75f099eb5b71fd9fd48b48e4bf721a@5.75.170.207:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
