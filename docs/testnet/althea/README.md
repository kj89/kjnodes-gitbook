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
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,3f9a20277d68b7fe52efbe84dad231af472d0190@162.55.235.69:29656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,ab3ba67d06d109e135f5cd22a3d4d6b1784e3a70@161.97.65.170:36656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,dc67cbe058b802aa34f64715b44474c462b4317b@65.108.237.224:36656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
