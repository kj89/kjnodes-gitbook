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
peers="16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,bdf94092f6dc380f6526f7b8b46b63192e95a033@173.212.222.167:29656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
