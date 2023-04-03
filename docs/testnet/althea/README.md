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
peers="cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,ab3ba67d06d109e135f5cd22a3d4d6b1784e3a70@161.97.65.170:36656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,8203297aacaea1d889fcf36240484c9efc217bbd@116.202.156.106:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,3b4e352fe0164b220bae482225641b01aa6475d9@141.95.97.28:11356,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
