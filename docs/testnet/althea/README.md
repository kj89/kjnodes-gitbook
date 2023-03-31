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
peers="2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,3f9a20277d68b7fe52efbe84dad231af472d0190@162.55.235.69:29656,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,d26fddea7ceb8cb5a52223702a23757cb09fad37@207.180.199.115:31656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,856ac01afa0163c27b69e1b25464427310120924@85.25.134.23:26656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,dc67cbe058b802aa34f64715b44474c462b4317b@65.108.237.224:36656,11e8f38e3c5601e4ab2333d5a5bbb108a39b8e1c@159.69.110.238:26656,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
