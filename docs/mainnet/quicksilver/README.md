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
peers="61d96fee29a9615c208c4db72526d23b45094cb4@65.108.195.30:36656,58fe3a7b075e7302f8b46b8171a0aa19ff4a427a@65.108.195.29:31126,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,e8a9be589ae825aa4368c6a00b50b7031d5de58b@65.108.78.107:21609,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.89.247.21:26656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,cc091c4d385e449a718fb252de800a9caf01913f@95.217.225.212:11656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
