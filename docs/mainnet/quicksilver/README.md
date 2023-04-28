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
peers="b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,c2a44958de52a8656eba9eedaf88205f27686ffd@46.4.23.42:11656,271419d3eb3878c902ebb0064490ad702d9d067f@144.76.145.150:26656,3a5d0b97feb595375c24665dcf17d793be129e8b@51.89.155.2:28656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,e8a9be589ae825aa4368c6a00b50b7031d5de58b@65.108.78.107:21609,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,9bed2c944243fd3ee35a6e4e8da0956f61518603@65.109.19.176:26656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,fb1e7a989ff78f0bdd7828dc3ade95dcd67cd5d0@65.109.116.151:15656,d0c81152bc586896c6c2a4dba15a4351742768d2@65.109.90.169:46656,cc091c4d385e449a718fb252de800a9caf01913f@95.217.225.212:11656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@142.132.253.112:15656,50a40c5aba326798ea9520ac0a1207e22a540a0e@95.214.55.100:26556,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
