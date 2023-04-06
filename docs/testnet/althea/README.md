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
peers="cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
