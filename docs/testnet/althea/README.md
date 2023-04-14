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

**live-peers** (19)
```bash
peers="16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,31e4e58aed75f099eb5b71fd9fd48b48e4bf721a@5.75.170.207:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
