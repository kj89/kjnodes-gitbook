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
peers="2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,eb69783b7e38059a58abaf342eb64f704de37636@23.88.66.239:31656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,ab3ba67d06d109e135f5cd22a3d4d6b1784e3a70@161.97.65.170:36656,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
