# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

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
* grpc: quicksilver.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="f73b2b887e7d1c01a3d753db359a0058e634e767@65.108.201.154:2090,58fe3a7b075e7302f8b46b8171a0aa19ff4a427a@65.108.195.29:31126,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,55a79e1163cf88e531aa2359038982edfd7b1526@176.9.16.233:11656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,e8a9be589ae825aa4368c6a00b50b7031d5de58b@65.108.78.107:21609,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,1c3db399f804a111efebeeffb5cdc4e751fb8108@65.109.61.113:21609,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,fb1e7a989ff78f0bdd7828dc3ade95dcd67cd5d0@65.109.116.151:15656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,a9e0f3c8e84c575492a2ff454abdad3b4762e712@193.34.212.166:25656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.89.247.21:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,2b73e89e8b8ff83271665a9766eba76dcd15735f@57.128.73.31:32306"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
