# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.1 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)


## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: [https://quicksilver.grpc.kjnodes.com](https://quicksilver.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (33)
```bash
peers="a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,6f7f00cc445627c68435d0c27394afab5fb41919@65.21.200.224:11156,f73b2b887e7d1c01a3d753db359a0058e634e767@65.108.201.154:2090,4a550b5e8bfa7260e6775ea3ebd61f36f1480fa4@65.109.37.58:12656,5f0c0411e34e1c7d0b9c53749d90a923b5e8c625@65.21.133.125:35656,ee14b4bbeb436056952c8e4e7c84826dfb92143b@65.109.105.17:26656,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,4559f4c24037bfad4791b2a6d6d5c769a16cad53@65.109.92.79:15656,162325861a80df7709aeacb1cbb52e033ba6438e@65.109.82.249:31656,0c1d930abb6561cab37b9df5bc6af285e311ab0f@65.108.109.240:26656,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,0b9833206c8967ac8ac0e1a407bedfe378b1a5f3@5.135.140.46:26656,0a3860f9d3c27b34910fe8660240ae55699b55c2@84.244.95.245:26656,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,3a5d0b97feb595375c24665dcf17d793be129e8b@51.89.155.2:28656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,c0beca70dbd3ef5bb433f7aa280d56d2a150bbd3@95.214.52.144:26656,1fa96b3e411a4ec5c6dd54389b6e7dff034f45c9@91.223.3.188:26656,063cc6b75194c4f943d32c549667ba210a7f2de1@195.3.222.240:26856,8b7b58ba8850175fea561851a2d525bdb0076c8d@206.72.198.246:26656,8dde859ce090bc669f028edfc69ccdaa973614ea@35.198.192.234:26656,eb5f2e57f6c69d1a37baad737248287666acba58@164.92.75.85:31786,e0c595bd21c4f08391b5c2a4736d1be9d907133c@65.108.229.102:35656,3394976851c8a06002989572119925f6d839a980@51.195.234.250:26656,96bd0e87a5e5b88e8ce637aa3c7aa4f4803b1d03@51.195.234.240:26656,644ab79faf40192e874a9852d147d1897f3fd38f@165.232.68.110:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,9bb9b69768308bbaf2edc092a4b6cea76490422a@176.9.98.24:30572,0453c08d4e19d9a310961d7a64c2c1dda9fc5616@95.214.53.37:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
