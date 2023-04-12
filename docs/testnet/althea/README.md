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
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
