# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.9-hotfix.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="71f722098fc28c2f39026af58d539f387451ddb0@65.109.86.210:27656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.98:26656,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,96b7605dbf13dbf0df2c3ac4f076397a9f351c6b@88.98.195.228:26656,50a40c5aba326798ea9520ac0a1207e22a540a0e@95.214.55.100:26556,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,4aa6607f87ad0b458526d3405731e71553cf275c@219.100.163.35:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,b00a1e8869d0a8327f12f12d6b63bacf15527525@213.239.207.175:32656,58fe3a7b075e7302f8b46b8171a0aa19ff4a427a@65.108.195.29:31126,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,a87f48e433160970318d181bb69c378f4564cd2d@107.155.67.202:26736,1c3db399f804a111efebeeffb5cdc4e751fb8108@65.109.61.113:21609,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,bdbb005129890e3b656841415b3b728d1e4529e6@142.132.138.18:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
