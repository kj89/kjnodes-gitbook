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
peers="ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
