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
peers="cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,ab3ba67d06d109e135f5cd22a3d4d6b1784e3a70@161.97.65.170:36656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
